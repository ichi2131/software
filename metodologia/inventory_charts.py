#!/usr/bin/env python3
"""
Generador de Gráficos de Inventario
Crea visualizaciones de pastel y barras del inventario en formato HTML
"""

import json
import os
from pathlib import Path
from datetime import datetime

class InventoryCharts:
    def __init__(self, inventory_data=None):
        """Inicializa el generador de gráficos"""
        self.inventory_data = inventory_data or []
        self.load_inventory_from_storage()
    
    def load_inventory_from_storage(self):
        """Carga el inventario desde localStorage.json si existe"""
        try:
            # Buscar archivo de inventario en el directorio actual
            if os.path.exists('inventory.json'):
                with open('inventory.json', 'r', encoding='utf-8') as f:
                    self.inventory_data = json.load(f)
        except Exception as e:
            print(f"Error cargando inventario: {e}")
            self.inventory_data = []
    
    def generate_pie_chart_html(self, output_file='inventory_chart.html'):
        """
        Genera un gráfico de pastel del inventario por categoría
        """
        # Agrupar por categoría
        categories = {}
        total_value = 0
        
        for product in self.inventory_data:
            category = product.get('category', 'Sin categoría')
            quantity = product.get('quantity', 0)
            price = product.get('price', 0)
            value = quantity * price
            
            if category not in categories:
                categories[category] = {'quantity': 0, 'value': 0}
            
            categories[category]['quantity'] += quantity
            categories[category]['value'] += value
            total_value += value
        
        # Preparar datos para Chart.js
        labels = list(categories.keys())
        values = [categories[cat]['value'] for cat in labels]
        quantities = [categories[cat]['quantity'] for cat in labels]
        
        # Colores para el gráfico
        colors = [
            '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
            '#FF9F40', '#FF6384', '#C9CBCF', '#4BC0C0', '#FF6384'
        ]
        colors = (colors * (len(labels) // len(colors) + 1))[:len(labels)]
        
        # HTML del gráfico
        html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📊 Gráfico de Inventario</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        h1 {{
            color: white;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .charts-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .chart-card {{
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        
        .chart-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0,0,0,0.2);
        }}
        
        .chart-card h2 {{
            color: #333;
            margin-bottom: 20px;
            font-size: 1.5em;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }}
        
        .chart-container {{
            position: relative;
            height: 400px;
            margin-bottom: 20px;
        }}
        
        .stats {{
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}
        
        .stats h2 {{
            color: #333;
            margin-bottom: 20px;
            font-size: 1.5em;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }}
        
        .stat-item {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }}
        
        .stat-item .label {{
            font-size: 0.9em;
            opacity: 0.9;
            margin-bottom: 10px;
        }}
        
        .stat-item .value {{
            font-size: 2em;
            font-weight: bold;
        }}
        
        .category-list {{
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }}
        
        .category-list h2 {{
            color: #333;
            margin-bottom: 20px;
            font-size: 1.5em;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }}
        
        .category-item {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px;
            border-bottom: 1px solid #eee;
            transition: background 0.3s;
        }}
        
        .category-item:hover {{
            background: #f5f5f5;
        }}
        
        .category-item:last-child {{
            border-bottom: none;
        }}
        
        .category-name {{
            font-weight: bold;
            color: #333;
        }}
        
        .category-stats {{
            display: flex;
            gap: 20px;
            color: #666;
            font-size: 0.9em;
        }}
        
        .back-btn {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
            margin-bottom: 20px;
            transition: transform 0.3s, box-shadow 0.3s;
            text-decoration: none;
            display: inline-block;
        }}
        
        .back-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        }}
        
        .timestamp {{
            text-align: center;
            color: #999;
            font-size: 0.9em;
            margin-top: 20px;
        }}
        
        @media (max-width: 768px) {{
            h1 {{
                font-size: 1.8em;
            }}
            
            .charts-grid {{
                grid-template-columns: 1fr;
            }}
            
            .chart-container {{
                height: 300px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="index.html" class="back-btn">← Volver al Inicio</a>
        <h1>📊 Análisis de Inventario</h1>
        
        <!-- ESTADÍSTICAS -->
        <div class="stats">
            <h2>📈 Estadísticas Generales</h2>
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="label">Total de Productos</div>
                    <div class="value">{len(self.inventory_data)}</div>
                </div>
                <div class="stat-item">
                    <div class="label">Unidades en Stock</div>
                    <div class="value">{sum(p.get('quantity', 0) for p in self.inventory_data)}</div>
                </div>
                <div class="stat-item">
                    <div class="label">Valor Total</div>
                    <div class="value">${total_value:,.2f}</div>
                </div>
                <div class="stat-item">
                    <div class="label">Categorías</div>
                    <div class="value">{len(categories)}</div>
                </div>
            </div>
        </div>
        
        <!-- GRÁFICOS -->
        <div class="charts-grid">
            <div class="chart-card">
                <h2>🥧 Distribución por Categoría (Valor)</h2>
                <div class="chart-container">
                    <canvas id="pieChart"></canvas>
                </div>
            </div>
            
            <div class="chart-card">
                <h2>📦 Distribución por Categoría (Cantidad)</h2>
                <div class="chart-container">
                    <canvas id="barChart"></canvas>
                </div>
            </div>
        </div>
        
        <!-- LISTA DETALLADA -->
        <div class="category-list">
            <h2>📋 Detalle por Categoría</h2>
            {"".join([f'''
            <div class="category-item">
                <span class="category-name">🏷️ {cat}</span>
                <div class="category-stats">
                    <span>Unidades: <strong>{categories[cat]['quantity']}</strong></span>
                    <span>Valor: <strong>${categories[cat]['value']:,.2f}</strong></span>
                </div>
            </div>
            ''' for cat in sorted(categories.keys())])}
        </div>
        
        <div class="timestamp">
            Generado: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
        </div>
    </div>
    
    <script>
        // Datos para los gráficos
        const labels = {json.dumps(labels)};
        const valueData = {json.dumps(values)};
        const quantityData = {json.dumps(quantities)};
        const colors = {json.dumps(colors)};
        
        // Gráfico de Pastel (Valor)
        const pieCtx = document.getElementById('pieChart').getContext('2d');
        new Chart(pieCtx, {{
            type: 'doughnut',
            data: {{
                labels: labels,
                datasets: [{{
                    data: valueData,
                    backgroundColor: colors,
                    borderColor: '#fff',
                    borderWidth: 2
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        position: 'bottom',
                        labels: {{
                            font: {{ size: 14 }},
                            padding: 15
                        }}
                    }},
                    tooltip: {{
                        callbacks: {{
                            label: function(context) {{
                                const value = context.parsed;
                                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                const percentage = ((value / total) * 100).toFixed(1);
                                return `${{value.toLocaleString('es-ES', {{maximumFractionDigits: 2}})}} ({{percentage}}%)`;
                            }}
                        }}
                    }}
                }}
            }}
        }});
        
        // Gráfico de Barras (Cantidad)
        const barCtx = document.getElementById('barChart').getContext('2d');
        new Chart(barCtx, {{
            type: 'bar',
            data: {{
                labels: labels,
                datasets: [{{
                    label: 'Unidades en Stock',
                    data: quantityData,
                    backgroundColor: colors,
                    borderColor: '#fff',
                    borderWidth: 1
                }}]
            }},
            options: {{
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        display: false
                    }},
                    tooltip: {{
                        callbacks: {{
                            label: function(context) {{
                                return `Unidades: ${{context.parsed.x}}`;
                            }}
                        }}
                    }}
                }},
                scales: {{
                    x: {{
                        beginAtZero: true,
                        ticks: {{
                            stepSize: 1
                        }}
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>"""
        
        # Guardar el archivo HTML
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✓ Gráfico de inventario generado: {output_file}")
        return output_file
    
    def generate_json_summary(self, output_file='inventory_summary.json'):
        """
        Genera un resumen en JSON del inventario
        """
        categories = {}
        total_value = 0
        total_quantity = 0
        
        for product in self.inventory_data:
            category = product.get('category', 'Sin categoría')
            quantity = product.get('quantity', 0)
            price = product.get('price', 0)
            value = quantity * price
            
            if category not in categories:
                categories[category] = {
                    'quantity': 0,
                    'value': 0,
                    'products': 0
                }
            
            categories[category]['quantity'] += quantity
            categories[category]['value'] += value
            categories[category]['products'] += 1
            total_value += value
            total_quantity += quantity
        
        summary = {
            'timestamp': datetime.now().isoformat(),
            'total_products': len(self.inventory_data),
            'total_quantity': total_quantity,
            'total_value': round(total_value, 2),
            'categories': categories,
            'low_stock': [
                {
                    'id': p['id'],
                    'name': p['name'],
                    'quantity': p['quantity'],
                    'category': p['category']
                }
                for p in self.inventory_data if p.get('quantity', 0) < 10
            ]
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
        
        print(f"✓ Resumen de inventario generado: {output_file}")
        return output_file


def main():
    """Función principal"""
    print("=" * 50)
    print("📊 Generador de Gráficos de Inventario")
    print("=" * 50)
    
    # Crear generador de gráficos
    charts = InventoryCharts()
    
    if not charts.inventory_data:
        print("\n⚠️ No se encontraron datos de inventario.")
        print("📝 Creando datos de ejemplo para demostración...\n")
        
        # Crear ejemplo si no hay archivo
        sample_inventory = [
            {"id": 1, "name": "Laptop Dell", "quantity": 5, "price": 800, "category": "Electrónicos"},
            {"id": 2, "name": "Mouse Logitech", "quantity": 50, "price": 25, "category": "Accesorios"},
            {"id": 3, "name": "Teclado Mecánico", "quantity": 30, "price": 120, "category": "Accesorios"},
            {"id": 4, "name": "Monitor LG 27\"", "quantity": 8, "price": 300, "category": "Electrónicos"},
            {"id": 5, "name": "Camiseta Negra", "quantity": 100, "price": 20, "category": "Ropa"},
            {"id": 6, "name": "Pantalón Azul", "quantity": 75, "price": 40, "category": "Ropa"},
            {"id": 7, "name": "Arroz Premium", "quantity": 200, "price": 2, "category": "Alimentos"},
            {"id": 8, "name": "Aceite de Oliva", "quantity": 50, "price": 8, "category": "Alimentos"},
        ]
        with open('inventory.json', 'w', encoding='utf-8') as f:
            json.dump(sample_inventory, f, ensure_ascii=False, indent=2)
        charts.inventory_data = sample_inventory
        print("✓ Datos de ejemplo creados en inventory.json\n")
    else:
        print(f"\n✓ Se encontraron {len(charts.inventory_data)} productos\n")
    
    # Generar gráficos
    html_file = charts.generate_pie_chart_html()
    json_file = charts.generate_json_summary()
    
    print("\n✓ Proceso completado exitosamente")
    print(f"  - Gráfico HTML: {html_file}")
    print(f"  - Resumen JSON: {json_file}")
    print("\nAbra 'inventory_chart.html' en su navegador para ver los gráficos.")


if __name__ == '__main__':
    main()
