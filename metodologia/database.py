#!/usr/bin/env python3
"""
Módulo de base de datos para el Sistema de Administración de Inventario
Usa SQLite como base de datos y proporciona funciones para gestionar usuarios y productos
"""

import sqlite3
import json
from pathlib import Path
from typing import List, Dict, Optional, Tuple

DATABASE_FILE = Path(__file__).parent / 'inventory.db'

class DatabaseManager:
    """Gestor de base de datos SQLite"""
    
    def __init__(self, db_path: str = str(DATABASE_FILE)):
        self.db_path = db_path
        self.init_db()
    
    def get_connection(self):
        """Obtener conexión a la base de datos"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_db(self):
        """Inicializar la base de datos con las tablas necesarias"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Tabla de usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL,
                fullName TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabla de productos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                quantity INTEGER DEFAULT 0,
                price REAL DEFAULT 0,
                category TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabla de carrito
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cart_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity INTEGER DEFAULT 1,
                price REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(product_id) REFERENCES products(id)
            )
        ''')
        
        # Tabla de logs/auditoría
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activity_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                action TEXT NOT NULL,
                details TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        
        conn.commit()
        
        # Insertar usuarios por defecto si no existen
        self._insert_default_users(conn)
        
        # Insertar productos por defecto si no existen
        self._insert_default_products(conn)
        
        conn.close()
    
    def _insert_default_users(self, conn):
        """Insertar usuarios por defecto"""
        cursor = conn.cursor()
        
        default_users = [
            ('owner', 'owner123', 'owner', 'Owner'),
            ('admin', 'admin123', 'admin', 'Administrador'),
            ('tester', 'tester123', 'tester', 'Inspector'),
            ('tesorera', 'tesorera123', 'tesorera', 'Tesorera'),
            ('buyer', 'buyer123', 'buyer', 'Comprador')
        ]
        
        for username, password, role, fullName in default_users:
            try:
                cursor.execute(
                    'INSERT INTO users (username, password, role, fullName) VALUES (?, ?, ?, ?)',
                    (username, password, role, fullName)
                )
            except sqlite3.IntegrityError:
                # Usuario ya existe
                pass
        
        conn.commit()
    
    def _insert_default_products(self, conn):
        """Insertar productos por defecto"""
        cursor = conn.cursor()
        
        default_products = [
            ('Laptop Dell XPS', 'Laptop de alto rendimiento', 5, 800, 'Electrónicos'),
            ('Mouse Logitech MX', 'Mouse inalámbrico de precisión', 50, 25, 'Accesorios'),
            ('Teclado Mecánico', 'Teclado gaming RGB', 30, 120, 'Accesorios'),
            ('Monitor LG 27" 4K', 'Monitor ultra HD', 8, 300, 'Electrónicos'),
            ('Camiseta Algodón', 'Camiseta 100% algodón', 100, 20, 'Ropa'),
            ('Pantalón Denim', 'Pantalón blue jean', 75, 40, 'Ropa'),
            ('Arroz Premium', 'Arroz basmati 5kg', 200, 2, 'Alimentos'),
            ('Aceite de Oliva', 'Aceite premium 1L', 50, 8, 'Alimentos')
        ]
        
        cursor.execute('SELECT COUNT(*) FROM products')
        if cursor.fetchone()[0] == 0:
            for name, description, quantity, price, category in default_products:
                cursor.execute(
                    'INSERT INTO products (name, description, quantity, price, category) VALUES (?, ?, ?, ?, ?)',
                    (name, description, quantity, price, category)
                )
            conn.commit()
    
    # ============ OPERACIONES DE USUARIOS ============
    def login(self, username: str, password: str) -> Optional[Dict]:
        """Verificar credenciales y retornar usuario"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                'id': row['id'],
                'username': row['username'],
                'role': row['role'],
                'fullName': row['fullName']
            }
        return None
    
    def get_all_users(self) -> List[Dict]:
        """Obtener todos los usuarios"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, username, role, fullName FROM users ORDER BY id')
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def add_user(self, username: str, password: str, role: str, fullName: str) -> Optional[Dict]:
        """Agregar nuevo usuario"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                'INSERT INTO users (username, password, role, fullName) VALUES (?, ?, ?, ?)',
                (username, password, role, fullName)
            )
            conn.commit()
            user_id = cursor.lastrowid
            conn.close()
            
            return {
                'id': user_id,
                'username': username,
                'role': role,
                'fullName': fullName
            }
        except sqlite3.IntegrityError:
            conn.close()
            return None
    
    def update_user(self, user_id: int, **kwargs) -> bool:
        """Actualizar usuario"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        allowed_fields = ['username', 'password', 'role', 'fullName']
        updates = {k: v for k, v in kwargs.items() if k in allowed_fields}
        
        if not updates:
            conn.close()
            return False
        
        set_clause = ', '.join([f'{k} = ?' for k in updates.keys()])
        values = list(updates.values()) + [user_id]
        
        cursor.execute(f'UPDATE users SET {set_clause} WHERE id = ?', values)
        conn.commit()
        conn.close()
        
        return cursor.rowcount > 0
    
    def delete_user(self, user_id: int) -> bool:
        """Eliminar usuario"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
        
        return cursor.rowcount > 0
    
    def reset_users(self):
        """Resetear usuarios a los valores por defecto"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users')
        conn.commit()
        self._insert_default_users(conn)
        conn.close()
    
    # ============ OPERACIONES DE PRODUCTOS ============
    def get_all_products(self) -> List[Dict]:
        """Obtener todos los productos"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products ORDER BY id')
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def get_product(self, product_id: int) -> Optional[Dict]:
        """Obtener un producto por ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
        row = cursor.fetchone()
        conn.close()
        
        return dict(row) if row else None
    
    def add_product(self, name: str, description: str, quantity: int, price: float, category: str) -> Optional[Dict]:
        """Agregar nuevo producto"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            'INSERT INTO products (name, description, quantity, price, category) VALUES (?, ?, ?, ?, ?)',
            (name, description, quantity, price, category)
        )
        conn.commit()
        product_id = cursor.lastrowid
        conn.close()
        
        return self.get_product(product_id)
    
    def update_product(self, product_id: int, **kwargs) -> bool:
        """Actualizar producto"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        allowed_fields = ['name', 'description', 'quantity', 'price', 'category']
        updates = {k: v for k, v in kwargs.items() if k in allowed_fields}
        
        if not updates:
            conn.close()
            return False
        
        updates['updated_at'] = 'CURRENT_TIMESTAMP'
        set_clause = ', '.join([f'{k} = ?' if k != 'updated_at' else f'{k} = CURRENT_TIMESTAMP' for k in updates.keys()])
        values = [v for k, v in updates.items() if k != 'updated_at'] + [product_id]
        
        cursor.execute(f'UPDATE products SET {set_clause} WHERE id = ?', values)
        conn.commit()
        conn.close()
        
        return cursor.rowcount > 0
    
    def delete_product(self, product_id: int) -> bool:
        """Eliminar producto"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        conn.commit()
        conn.close()
        
        return cursor.rowcount > 0
    
    def reset_products(self):
        """Resetear productos a los valores por defecto"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM products')
        conn.commit()
        self._insert_default_products(conn)
        conn.close()
    
    # ============ OPERACIONES DE CARRITO ============
    def get_cart(self) -> List[Dict]:
        """Obtener el carrito"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT ci.id, ci.product_id, p.name, p.description, p.category, 
                   ci.quantity, ci.price, (ci.quantity * ci.price) as total
            FROM cart_items ci
            JOIN products p ON ci.product_id = p.id
            ORDER BY ci.created_at
        ''')
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def add_to_cart(self, product_id: int, quantity: int) -> Optional[Dict]:
        """Agregar producto al carrito"""
        product = self.get_product(product_id)
        if not product:
            return None
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Verificar si el producto ya está en el carrito
        cursor.execute('SELECT * FROM cart_items WHERE product_id = ?', (product_id,))
        existing = cursor.fetchone()
        
        if existing:
            new_quantity = existing['quantity'] + quantity
            cursor.execute('UPDATE cart_items SET quantity = ? WHERE product_id = ?', (new_quantity, product_id))
        else:
            cursor.execute(
                'INSERT INTO cart_items (product_id, quantity, price) VALUES (?, ?, ?)',
                (product_id, quantity, product['price'])
            )
        
        conn.commit()
        conn.close()
        
        return {'product_id': product_id, 'quantity': quantity}
    
    def remove_from_cart(self, cart_item_id: int) -> bool:
        """Eliminar producto del carrito"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM cart_items WHERE id = ?', (cart_item_id,))
        conn.commit()
        conn.close()
        
        return cursor.rowcount > 0
    
    def clear_cart(self) -> bool:
        """Limpiar el carrito"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM cart_items')
        conn.commit()
        conn.close()
        
        return True
    
    # ============ OPERACIONES DE AUDITORÍA ============
    def log_activity(self, user_id: Optional[int], action: str, details: str = None) -> bool:
        """Registrar actividad"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO activity_log (user_id, action, details) VALUES (?, ?, ?)',
            (user_id, action, details)
        )
        conn.commit()
        conn.close()
        
        return True
    
    def get_activity_log(self, limit: int = 100) -> List[Dict]:
        """Obtener el log de actividades"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT al.id, al.user_id, u.username, al.action, al.details, al.created_at
            FROM activity_log al
            LEFT JOIN users u ON al.user_id = u.id
            ORDER BY al.created_at DESC
            LIMIT ?
        ''', (limit,))
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]


# Instancia global
db = DatabaseManager()
