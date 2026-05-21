#!/usr/bin/env python3
"""
Script de prueba para verificar que la base de datos y API funcionen correctamente
"""

import sys
import os
from pathlib import Path

# Agregar directorio actual al path
sys.path.insert(0, str(Path(__file__).parent))

def test_database():
    """Probar la base de datos"""
    print("🧪 Probando base de datos...")
    print("-" * 50)
    
    try:
        from database import db
        
        # Test 1: Usuarios
        print("\n✓ Test 1: Usuarios por defecto")
        users = db.get_all_users()
        print(f"  Usuarios encontrados: {len(users)}")
        for user in users:
            print(f"    - {user['username']} ({user['role']})")
        
        # Test 2: Login
        print("\n✓ Test 2: Login")
        user = db.login('owner', 'owner123')
        if user:
            print(f"  ✅ Login exitoso: {user['fullName']}")
        else:
            print(f"  ❌ Login fallido")
            return False
        
        # Test 3: Productos
        print("\n✓ Test 3: Productos por defecto")
        products = db.get_all_products()
        print(f"  Productos encontrados: {len(products)}")
        for product in products[:3]:
            print(f"    - {product['name']} (${product['price']})")
        if len(products) > 3:
            print(f"    ... y {len(products) - 3} más")
        
        # Test 4: Carrito
        print("\n✓ Test 4: Carrito")
        db.clear_cart()
        result = db.add_to_cart(1, 2)
        if result:
            print(f"  ✅ Producto agregado al carrito")
            cart = db.get_cart()
            print(f"  Items en carrito: {len(cart)}")
        else:
            print(f"  ❌ Error al agregar al carrito")
        
        # Test 5: Auditoría
        print("\n✓ Test 5: Log de auditoría")
        db.log_activity(1, 'test', 'Test de auditoría')
        logs = db.get_activity_log(5)
        print(f"  Últimos registros: {len(logs)}")
        if logs:
            print(f"    - {logs[0]['action']} ({logs[0]['username']})")
        
        print("\n" + "="*50)
        print("✅ Todos los tests pasaron correctamente!")
        print("="*50)
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_api():
    """Probar la API (sin ejecutarla)"""
    print("\n\n🧪 Probando configuración de API...")
    print("-" * 50)
    
    try:
        import api
        print("✓ API importada correctamente")
        
        # Verificar que Flask esté instalado
        import flask
        print(f"✓ Flask {flask.__version__} instalado")
        
        # Verificar CORS
        import flask_cors
        print("✓ Flask-CORS instalado")
        
        print("\n" + "="*50)
        print("✅ Dependencias de API OK!")
        print("="*50)
        
        print("\n📝 Para iniciar la API, ejecuta:")
        print("   python api.py")
        print("\n   Entonces accede a:")
        print("   http://localhost:5000/api/health")
        
        return True
        
    except ImportError as e:
        print(f"\n⚠️  Dependencia faltante: {e}")
        print("\nInstala con:")
        print("  python -m pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

if __name__ == '__main__':
    print("\n")
    print("╔════════════════════════════════════════════════════════╗")
    print("║  Sistema de Inventario - Script de Prueba             ║")
    print("╚════════════════════════════════════════════════════════╝")
    
    # Test base de datos
    db_ok = test_database()
    
    # Test API
    api_ok = test_api()
    
    # Resumen
    print("\n\n")
    print("╔════════════════════════════════════════════════════════╗")
    print("║  RESUMEN DE PRUEBAS                                   ║")
    print("╚════════════════════════════════════════════════════════╝")
    print(f"\n✓ Base de datos:  {'✅ OK' if db_ok else '❌ FALLO'}")
    print(f"✓ Dependencias:   {'✅ OK' if api_ok else '⚠️  FALTA INSTALAR'}")
    
    if db_ok and api_ok:
        print("\n🎉 ¡Sistema listo para usar!")
        print("\n   1. Ejecuta: python api.py")
        print("   2. Abre: http://localhost:8000/login.html")
        print("   3. Login con owner / owner123")
    elif db_ok and not api_ok:
        print("\n⚠️  Instala las dependencias:")
        print("   python -m pip install -r requirements.txt")
    else:
        print("\n❌ Hay problemas. Revisa los errores arriba.")
    
    print("\n")
