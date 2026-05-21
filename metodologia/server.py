#!/usr/bin/env python3
"""
Servidor HTTP simple para el Sistema de Administración de Inventario
Permite ejecutar automáticamente los gráficos de inventario
"""

import http.server
import socketserver
import os
import subprocess
import json
import sys
from pathlib import Path
from urllib.parse import urlparse, parse_qs

PORT = 8000
DIRECTORY = Path(__file__).parent

class InventoryHandler(http.server.SimpleHTTPRequestHandler):
    """Manejador HTTP personalizado para soportar ejecución de scripts"""
    
    def do_GET(self):
        """Manejar peticiones GET"""
        # Verificar si es una petición para ejecutar gráficos
        if self.path == '/run_charts':
            self.run_charts()
            return
        
        # Cambiar al directorio correcto
        self.directory = str(DIRECTORY)
        
        # Manejar normalmente
        super().do_GET()
    
    def do_POST(self):
        """Manejar peticiones POST"""
        # Cambiar al directorio correcto
        self.directory = str(DIRECTORY)
        
        # Verificar si es una petición para ejecutar gráficos
        if self.path == '/run_charts':
            self.run_charts()
            return
        
        # Manejar normalmente
        super().do_POST()
    
    def run_charts(self):
        """Ejecutar el generador de gráficos"""
        try:
            # Cambiar al directorio del proyecto
            os.chdir(DIRECTORY)
            
            # Ejecutar el script de gráficos
            result = subprocess.run(
                [sys.executable, 'inventory_charts.py'],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            # Enviar respuesta
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            response = {
                'success': result.returncode == 0,
                'message': result.stdout if result.returncode == 0 else result.stderr,
                'file': 'inventory_chart.html'
            }
            
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
            
        except subprocess.TimeoutExpired:
            self.send_error(504, 'Script timeout')
        except Exception as e:
            self.send_error(500, f'Error: {str(e)}')
    
    def log_message(self, format, *args):
        """Log personalizado"""
        print(f"[{self.log_date_time_string()}] {format % args}")

def main():
    """Función principal"""
    os.chdir(DIRECTORY)
    
    handler = InventoryHandler
    
    print("\n" + "="*60)
    print("   SISTEMA DE ADMINISTRACIÓN DE INVENTARIO")
    print("="*60)
    print(f"\n📍 Directorio: {DIRECTORY}")
    print(f"🌐 Servidor iniciado en: http://localhost:{PORT}")
    print(f"\n📝 Presiona CTRL+C para detener el servidor\n")
    print("="*60 + "\n")
    
    try:
        with socketserver.TCPServer(("", PORT), handler) as httpd:
            # Intentar ejecutar los gráficos al iniciar
            print("📊 Ejecutando generador de gráficos automáticamente...\n")
            try:
                subprocess.run(
                    [sys.executable, 'inventory_charts.py'],
                    cwd=DIRECTORY
                )
            except Exception as e:
                print(f"⚠️ No se pudo ejecutar automáticamente: {e}\n")
            
            print(f"\n✓ Servidor listo. Accede a http://localhost:{PORT}\n")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✓ Servidor detenido")
    except OSError as e:
        print(f"\n✗ Error: {e}")
        print(f"\nPuerto {PORT} posiblemente en uso. Intenta cambiar el puerto en el código.")
        sys.exit(1)

if __name__ == '__main__':
    main()
