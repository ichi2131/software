# 🗄️ Sistema de Base de Datos - Guía de Implementación

## 📋 Resumen de Cambios

Se ha migrado el sistema de inventario de **localStorage** (almacenamiento local del navegador) a una **arquitectura cliente-servidor con base de datos SQLite**.

### Arquitectura Anterior (localStorage)
```
Frontend (HTML/JS) ──→ localStorage (datos locales)
```

### Arquitectura Nueva (Base de datos + API)
```
Frontend (HTML/JS) ──→ API Flask ──→ SQLite Database
           ↓
    (api-client.js)
```

## 🗂️ Archivos Nuevos Creados

### 1. **database.py**
- Módulo principal de base de datos con SQLite
- Gestiona todas las operaciones CRUD
- Tablas: `users`, `products`, `cart_items`, `activity_log`
- **Funciones principales:**
  - Login/registro de usuarios
  - Gestión de productos (CRUD)
  - Carrito de compras
  - Log de auditoría

### 2. **api.py**
- Servidor Flask con API RESTful
- Endpoints para todas las operaciones
- Manejo de sesiones y autenticación
- **Puerto por defecto:** `5000`

**Endpoints principales:**
```
POST   /api/login              - Iniciar sesión
POST   /api/logout             - Cerrar sesión
POST   /api/signup             - Registro de nuevo usuario

GET    /api/users              - Listar usuarios (admin)
PUT    /api/users/<id>         - Actualizar usuario (admin)
DELETE /api/users/<id>         - Eliminar usuario (admin)
POST   /api/reset-users        - Resetear usuarios (owner)

GET    /api/products           - Listar productos
POST   /api/products           - Crear producto
PUT    /api/products/<id>      - Actualizar producto
DELETE /api/products/<id>      - Eliminar producto
POST   /api/reset-products     - Resetear productos (owner)

GET    /api/cart               - Ver carrito
POST   /api/cart               - Agregar al carrito
DELETE /api/cart/<id>          - Eliminar del carrito
POST   /api/cart/clear         - Limpiar carrito

GET    /api/activity-log       - Ver auditoría (admin)
GET    /api/health             - Estado de la API
```

### 3. **api-client.js**
- Cliente JavaScript para comunicarse con la API
- Reemplaza las funciones de `app.js`
- Usa `fetch()` para llamadas HTTP
- Mantiene compatibilidad con código existente

### 4. **requirements.txt**
- Dependencias de Python necesarias:
  - Flask 3.0.0
  - Flask-CORS 4.0.0
  - Werkzeug 3.0.1

### 5. **start_api.ps1**
- Script PowerShell para iniciar el sistema
- Instala dependencias automáticamente
- Inicia la API y abre el navegador

## 🚀 Cómo Iniciar

### Opción 1: Script PowerShell (Recomendado)
```powershell
.\start_api.ps1
```

### Opción 2: Manualmente
```bash
# Instalar dependencias
pip install -r requirements.txt

# Iniciar API
python api.py

# En otra ventana, iniciar servidor web
python server.py  # o http-server si tienes Node.js
```

## 📁 Base de Datos SQLite

### Ubicación
```
C:\Users\shado\OneDrive\Desktop\chamba\metodologia\inventory.db
```

### Tablas

#### 1. **users**
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL,
    fullName TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

#### 2. **products**
```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    quantity INTEGER DEFAULT 0,
    price REAL DEFAULT 0,
    category TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
)
```

#### 3. **cart_items**
```sql
CREATE TABLE cart_items (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    price REAL NOT NULL,
    created_at TIMESTAMP,
    FOREIGN KEY(product_id) REFERENCES products(id)
)
```

#### 4. **activity_log**
```sql
CREATE TABLE activity_log (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    action TEXT NOT NULL,
    details TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
```

## 🔐 Usuarios por Defecto

| Usuario | Contraseña | Rol |
|---------|-----------|-----|
| owner | owner123 | Owner |
| admin | admin123 | Admin |
| tester | tester123 | Inspector |
| tesorera | tesorera123 | Tesorera |
| buyer | buyer123 | Comprador |

## ⚙️ Configuración

### Variables de Entorno (Opcional)
```bash
export FLASK_ENV=development  # o production
export FLASK_PORT=5000
export DATABASE_PATH=/ruta/a/inventory.db
```

### Archivo de Configuración (si necesitas)
Crea `config.py`:
```python
class Config:
    DEBUG = False
    TESTING = False
    DATABASE = 'inventory.db'
    SECRET_KEY = 'tu-clave-secreta'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
```

## 🔄 Migración desde localStorage

### Cambios en el Frontend

**Antes (localStorage):**
```javascript
function login(username, password) {
    const users = JSON.parse(localStorage.getItem('users')) || [];
    const user = users.find(u => u.username === username && u.password === password);
    if (user) {
        setCurrentUser(user);
        return true;
    }
    return false;
}
```

**Después (API):**
```javascript
async function login(username, password) {
    const response = await fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ username, password })
    });
    
    if (response.ok) {
        const data = await response.json();
        localStorage.setItem('currentUser', JSON.stringify(data.user));
        return true;
    }
    return false;
}
```

## ✅ Ventajas de esta Implementación

1. **Persistencia Real**: Datos guardados en base de datos, no en localStorage
2. **Seguridad**: Las contraseñas se validan en el servidor
3. **Escalabilidad**: Fácil de agregar más funcionalidades
4. **Auditoría**: Log de todas las actividades
5. **Multi-dispositivo**: Los datos son compartidos entre dispositivos
6. **Control de Acceso**: Validación de permisos en el servidor
7. **Facilidad de Backup**: Puedes hacer backup de la BD

## 🐛 Solución de Problemas

### Error: "API no disponible"
- Verifica que la API está corriendo: `http://localhost:5000/api/health`
- Instala las dependencias: `pip install -r requirements.txt`
- Ejecuta: `python api.py`

### Error: CORS (Cross-Origin)
- La API tiene CORS habilitado, pero verifica que los puertos sean correctos
- Frontend: `http://localhost:8000`
- API: `http://localhost:5000`

### Error: "Base de datos bloqueada"
- Cierra todas las instancias de la aplicación
- Elimina `inventory.db` y reinicia (perderás datos)

### La contraseña no funciona
- Resetea usuarios desde login: botón "🔄 Resetear Usuarios"
- O ejecuta en Python:
  ```python
  from database import db
  db.reset_users()
  ```

## 📊 Monitoreo

### Ver logs de la API
- Los logs se muestran en la consola donde ejecutaste `python api.py`
- Para ver actividades de usuarios: `GET /api/activity-log`

### Consultar Base de Datos Directamente
```bash
sqlite3 inventory.db
> SELECT * FROM users;
> SELECT * FROM products;
> SELECT * FROM activity_log;
```

## 🔄 Próximas Mejoras (Opcionales)

1. Agregar autenticación JWT
2. Implementar perfiles de usuario más detallados
3. Agregar búsqueda y filtrado avanzado
4. Implementar paginación
5. Agregar exportación a CSV/Excel
6. Crear panel de estadísticas
7. Implementar backup automático

## 📚 Estructura Completa del Proyecto

```
metodologia/
├── database.py              ← Capa de base de datos
├── api.py                   ← API Flask
├── api-client.js            ← Cliente JavaScript
├── app.js                   ← (opcional, puede mantenerse para compatibilidad)
├── requirements.txt         ← Dependencias Python
├── start_api.ps1            ← Script de inicio
├── inventory.db             ← BD SQLite (se crea automáticamente)
├── login.html
├── index.html
├── config.html
├── user_management.html
└── ... (otros archivos HTML)
```

## 🎯 Próximos Pasos

1. Ejecutar `.\start_api.ps1` para iniciar todo
2. Acceder a `http://localhost:8000/login.html`
3. Probar login con credenciales por defecto
4. Verificar que los datos persisten en la BD

¡Sistema listo para producción! 🚀
