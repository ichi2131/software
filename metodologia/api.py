#!/usr/bin/env python3
"""
API Flask para el Sistema de Administración de Inventario
Proporciona endpoints REST para acceder a la base de datos SQLite
"""

from flask import Flask, jsonify, request, session
from flask_cors import CORS
from database import db
import json
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = 'chamba-inventory-secret-key-2024'
CORS(app)

# Middleware para verificar autenticación
def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = session.get('user')
        if not user:
            return jsonify({'error': 'No autenticado'}), 401
        return f(*args, **kwargs)
    return decorated_function

# ============ AUTENTICACIÓN ============
@app.route('/api/login', methods=['POST'])
def api_login():
    """Login de usuario"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = db.login(username, password)
    if user:
        session['user'] = user
        db.log_activity(user['id'], 'login', f'Usuario {username} inició sesión')
        return jsonify({
            'success': True,
            'user': user,
            'message': 'Autenticación exitosa'
        })
    
    return jsonify({
        'success': False,
        'error': 'Usuario o contraseña incorrectos'
    }), 401

@app.route('/api/logout', methods=['POST'])
@require_auth
def api_logout():
    """Logout de usuario"""
    user = session.get('user')
    if user:
        db.log_activity(user['id'], 'logout', f'Usuario {user["username"]} cerró sesión')
    session.clear()
    
    return jsonify({
        'success': True,
        'message': 'Sesión cerrada'
    })

@app.route('/api/current-user', methods=['GET'])
def api_current_user():
    """Obtener usuario actual"""
    user = session.get('user')
    if user:
        return jsonify({'user': user})
    return jsonify({'user': None})

@app.route('/api/signup', methods=['POST'])
def api_signup():
    """Registrar nuevo usuario"""
    data = request.get_json()
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    fullName = data.get('fullName', '').strip()
    
    # Validaciones
    if not username or not password or not fullName:
        return jsonify({'error': 'Todos los campos son requeridos'}), 400
    
    if len(password) < 6:
        return jsonify({'error': 'La contraseña debe tener al menos 6 caracteres'}), 400
    
    user = db.add_user(username, password, 'buyer', fullName)
    if not user:
        return jsonify({'error': 'El usuario ya existe'}), 400
    
    db.log_activity(user['id'], 'signup', f'Nuevo usuario registrado: {username}')
    
    return jsonify({
        'success': True,
        'user': user,
        'message': 'Cuenta creada exitosamente'
    })

# ============ GESTIÓN DE USUARIOS (Admin) ============
@app.route('/api/users', methods=['GET'])
@require_auth
def api_get_users():
    """Obtener todos los usuarios"""
    user = session.get('user')
    if user['role'] not in ['owner', 'admin']:
        return jsonify({'error': 'No tienes permiso'}), 403
    
    users = db.get_all_users()
    return jsonify({'users': users})

@app.route('/api/users/<int:user_id>', methods=['PUT'])
@require_auth
def api_update_user(user_id):
    """Actualizar usuario"""
    user = session.get('user')
    if user['role'] not in ['owner', 'admin']:
        return jsonify({'error': 'No tienes permiso'}), 403
    
    data = request.get_json()
    success = db.update_user(user_id, **data)
    
    if success:
        db.log_activity(user['id'], 'update_user', f'Actualizó usuario ID: {user_id}')
        return jsonify({'success': True, 'message': 'Usuario actualizado'})
    
    return jsonify({'error': 'No se pudo actualizar el usuario'}), 400

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
@require_auth
def api_delete_user(user_id):
    """Eliminar usuario"""
    user = session.get('user')
    if user['role'] not in ['owner', 'admin']:
        return jsonify({'error': 'No tienes permiso'}), 403
    
    if user['id'] == user_id:
        return jsonify({'error': 'No puedes eliminarte a ti mismo'}), 400
    
    success = db.delete_user(user_id)
    if success:
        db.log_activity(user['id'], 'delete_user', f'Eliminó usuario ID: {user_id}')
        return jsonify({'success': True, 'message': 'Usuario eliminado'})
    
    return jsonify({'error': 'No se pudo eliminar el usuario'}), 400

@app.route('/api/reset-users', methods=['POST'])
@require_auth
def api_reset_users():
    """Resetear usuarios a valores por defecto"""
    user = session.get('user')
    if user['role'] != 'owner':
        return jsonify({'error': 'Solo el owner puede resetear usuarios'}), 403
    
    db.reset_users()
    db.log_activity(user['id'], 'reset_users', 'Reseteó todos los usuarios')
    
    return jsonify({
        'success': True,
        'message': 'Usuarios reseteados a valores por defecto'
    })

# ============ GESTIÓN DE PRODUCTOS ============
@app.route('/api/products', methods=['GET'])
def api_get_products():
    """Obtener todos los productos"""
    products = db.get_all_products()
    return jsonify({'products': products})

@app.route('/api/products/<int:product_id>', methods=['GET'])
def api_get_product(product_id):
    """Obtener un producto"""
    product = db.get_product(product_id)
    if product:
        return jsonify({'product': product})
    return jsonify({'error': 'Producto no encontrado'}), 404

@app.route('/api/products', methods=['POST'])
@require_auth
def api_add_product():
    """Agregar nuevo producto"""
    user = session.get('user')
    if not user['role'] in ['owner', 'admin', 'buyer']:
        return jsonify({'error': 'No tienes permiso'}), 403
    
    data = request.get_json()
    product = db.add_product(
        name=data.get('name'),
        description=data.get('description', ''),
        quantity=data.get('quantity', 0),
        price=data.get('price', 0),
        category=data.get('category', '')
    )
    
    if product:
        db.log_activity(user['id'], 'add_product', f'Agregó producto: {product["name"]}')
        return jsonify({'success': True, 'product': product}), 201
    
    return jsonify({'error': 'Error al agregar producto'}), 400

@app.route('/api/products/<int:product_id>', methods=['PUT'])
@require_auth
def api_update_product(product_id):
    """Actualizar producto"""
    user = session.get('user')
    if user['role'] not in ['owner', 'admin']:
        return jsonify({'error': 'No tienes permiso'}), 403
    
    data = request.get_json()
    success = db.update_product(product_id, **data)
    
    if success:
        db.log_activity(user['id'], 'update_product', f'Actualizó producto ID: {product_id}')
        return jsonify({'success': True, 'message': 'Producto actualizado'})
    
    return jsonify({'error': 'No se pudo actualizar el producto'}), 400

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
@require_auth
def api_delete_product(product_id):
    """Eliminar producto"""
    user = session.get('user')
    if user['role'] not in ['owner', 'admin']:
        return jsonify({'error': 'No tienes permiso'}), 403
    
    success = db.delete_product(product_id)
    if success:
        db.log_activity(user['id'], 'delete_product', f'Eliminó producto ID: {product_id}')
        return jsonify({'success': True, 'message': 'Producto eliminado'})
    
    return jsonify({'error': 'No se pudo eliminar el producto'}), 400

@app.route('/api/reset-products', methods=['POST'])
@require_auth
def api_reset_products():
    """Resetear productos a valores por defecto"""
    user = session.get('user')
    if user['role'] != 'owner':
        return jsonify({'error': 'Solo el owner puede resetear productos'}), 403
    
    db.reset_products()
    db.log_activity(user['id'], 'reset_products', 'Reseteó todos los productos')
    
    return jsonify({
        'success': True,
        'message': 'Productos reseteados a valores por defecto'
    })

# ============ GESTIÓN DE CARRITO ============
@app.route('/api/cart', methods=['GET'])
def api_get_cart():
    """Obtener carrito"""
    cart = db.get_cart()
    return jsonify({'cart': cart})

@app.route('/api/cart', methods=['POST'])
def api_add_to_cart():
    """Agregar producto al carrito"""
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    result = db.add_to_cart(product_id, quantity)
    if result:
        return jsonify({'success': True, 'message': 'Producto agregado al carrito'}), 201
    
    return jsonify({'error': 'Producto no encontrado'}), 404

@app.route('/api/cart/<int:cart_item_id>', methods=['DELETE'])
def api_remove_from_cart(cart_item_id):
    """Eliminar producto del carrito"""
    success = db.remove_from_cart(cart_item_id)
    
    if success:
        return jsonify({'success': True, 'message': 'Producto eliminado del carrito'})
    
    return jsonify({'error': 'Artículo no encontrado'}), 404

@app.route('/api/cart/clear', methods=['POST'])
def api_clear_cart():
    """Limpiar carrito"""
    db.clear_cart()
    return jsonify({'success': True, 'message': 'Carrito vaciado'})

# ============ AUDITORÍA ============
@app.route('/api/activity-log', methods=['GET'])
@require_auth
def api_get_activity_log():
    """Obtener log de actividades"""
    user = session.get('user')
    if user['role'] not in ['owner', 'admin']:
        return jsonify({'error': 'No tienes permiso'}), 403
    
    limit = request.args.get('limit', 100, type=int)
    logs = db.get_activity_log(limit)
    
    return jsonify({'logs': logs})

# ============ HEALTH CHECK ============
@app.route('/api/health', methods=['GET'])
def api_health():
    """Verificar estado de la API"""
    return jsonify({
        'status': 'ok',
        'message': 'API de inventario funcionando correctamente',
        'timestamp': datetime.now().isoformat()
    })

# ============ MANEJO DE ERRORES ============
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint no encontrado'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Error interno del servidor'}), 500

if __name__ == '__main__':
    print("🚀 Iniciando API de Inventario...")
    print("📡 Servidor en: http://localhost:5000")
    print("📚 Documentación: http://localhost:5000/api/health")
    app.run(debug=True, host='localhost', port=5000)
