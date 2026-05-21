#!/usr/bin/env python3
"""
Servidor simple para ejecutar automáticamente el generador de gráficos de inventario
Este script inicia un servidor local y ejecuta el generador de gráficos en background
"""

import subprocess
import sys
import os
import time
from pathlib import Path

def run_inventory_charts():
    """Ejecuta el generador de gráficos de inventario"""
    try:
        print("\n" + "="*50)
        print("📊 Iniciando generador de gráficos de inventario")
        print("="*50 + "\n")
        
        result = subprocess.run(
            [sys.executable, 'inventory_charts.py'],
            cwd=Path(__file__).parent,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(result.stdout)
            print("\n✓ Gráficos generados exitosamente\n")
        else:
            print(result.stderr)
            print("\n✗ Error al generar gráficos\n")
            
    except Exception as e:
        print(f"\n✗ Error: {e}\n")

def main():
    """Función principal"""
    print("\n" + "="*60)
    print("   SISTEMA DE ADMINISTRACIÓN DE INVENTARIO")
    print("="*60 + "\n")
    
    # Cambiar al directorio del script
    os.chdir(Path(__file__).parent)
    
    # Ejecutar generador de gráficos automáticamente
    run_inventory_charts()
    
    # Mostrar instrucciones
    print("\n" + "="*60)
    print("   PRÓXIMOS PASOS")
    print("="*60)
    print("\n1. Abre tu navegador y accede a: http://localhost:8000")
    print("2. Usa las credenciales de prueba:")
    print("   - Owner: owner / owner123")
    print("   - Admin: admin / admin123")
    print("   - Inspector: tester / tester123")
    print("   - Tesorera: tesorera / tesorera123")
    print("   - Comprador: buyer / buyer123")
    print("\n3. Los gráficos se han guardado en: inventory_chart.html")
    print("\n" + "="*60 + "\n")

if __name__ == '__main__':
    main()
