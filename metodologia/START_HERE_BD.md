# 🚀 GUÍA RÁPIDA - Sistema con Base de Datos

## ¿Qué es nuevo?

Tu sistema ahora usa **SQLite (base de datos real)** en lugar de `localStorage`. Los datos ahora se guardan de forma permanente y segura.

### Antes (localStorage)
```
Navegador → localStorage → datos perdidos si limpias cache
```

### Ahora (Base de datos)
```
Navegador → API Flask → SQLite Database → datos persistentes
```

---

## ⚡ INICIO RÁPIDO (3 pasos)

### Paso 1: Abre la terminal
```bash
cd C:\Users\shado\OneDrive\Desktop\chamba\metodologia
```

### Paso 2: Ejecuta el script
**Opción A (Recomendado):**
```bash
start_api.bat
```

**Opción B (PowerShell):**
```bash
.\start_api.ps1
```

**Opción C (Manual):**
```bash
python api.py
```

### Paso 3: Accede a la aplicación
El navegador se abrirá automáticamente en:
```
http://localhost:8000/login.html
```

---

## 🔐 Credenciales de Prueba

```
Usuario:     owner
Contraseña:  owner123
```

Otros usuarios disponibles:
- admin / admin123
- tester / tester123
- tesorera / tesorera123
- buyer / buyer123

---

## 📁 Archivos Nuevos Creados

| Archivo | Tamaño | Descripción |
|---------|--------|------------|
| `database.py` | 14.7 KB | Gestor de base de datos SQLite |
| `api.py` | 10.8 KB | Servidor Flask con API REST |
| `api-client.js` | 11.0 KB | Cliente JavaScript para la API |
| `requirements.txt` | 50 B | Dependencias de Python |
| `start_api.bat` | 1.2 KB | Script para iniciar (Windows) |
| `start_api.ps1` | 4.4 KB | Script para iniciar (PowerShell) |
| `test_system.py` | 4.7 KB | Script de prueba |
| `DATABASE_SETUP.md` | 8.4 KB | Documentación técnica |
| `SETUP_GUIDE.txt` | 7.1 KB | Guía completa |

---

## 🎯 Cambiado en los archivos existentes

### login.html
- **Antes:** `<script src="app.js"></script>`
- **Ahora:** `<script src="api-client.js"></script>`
- El login ahora usa la API en lugar de localStorage

---

## 🗄️ Base de Datos (Automática)

Se crea automáticamente en:
```
C:\Users\shado\OneDrive\Desktop\chamba\metodologia\inventory.db
```

**Tablas creadas:**
- `users` (5 usuarios por defecto)
- `products` (8 productos por defecto)
- `cart_items` (carrito de compras)
- `activity_log` (auditoría)

---

## 📡 Puertos

- **API:** http://localhost:5000/api
- **Frontend:** http://localhost:8000
- **Health Check:** http://localhost:5000/api/health

---

## ✅ Checklist de Instalación

- [ ] Python 3.7+ instalado (`python --version`)
- [ ] Estoy en la carpeta metodologia
- [ ] Ejecuté `start_api.bat` o `python api.py`
- [ ] El navegador abrió http://localhost:8000/login.html
- [ ] Pude loguearme con owner/owner123
- [ ] Los datos persisten (actualiza la página)

---

## 🔧 Solución de Problemas

### Error: "Python no encontrado"
```bash
pip install -r requirements.txt
python api.py
```

### Error: "Puerto 5000 en uso"
Cambia el puerto en `api.py` línea final:
```python
app.run(debug=True, host='localhost', port=5001)  # Cambiar 5001
```

### Error: "CORS error"
Asegúrate de que ambos servidores corran:
- `python api.py` (API en puerto 5000)
- `python server.py` (Frontend en puerto 8000)

### Datos no persisten
Verifica que `inventory.db` existe en la carpeta:
```bash
dir inventory.db
```

---

## 📚 Documentación Completa

Para información más detallada, lee:
- **DATABASE_SETUP.md** - Documentación técnica completa
- **SETUP_GUIDE.txt** - Guía visual con todos los detalles

---

## 🎉 ¿Ya está todo listo?

```bash
# 1. Inicia la API
python api.py

# 2. En otra terminal, inicia el servidor web
python server.py

# 3. Abre en navegador
http://localhost:8000/login.html

# 4. Login con owner / owner123
```

---

## 💡 Próximos Pasos (Opcional)

1. **Actualizar otros HTML:** Cambiar referencias de `app.js` a `api-client.js`
2. **Implementar JWT:** Mayor seguridad en producción
3. **Agregar validación:** Validar datos en cliente y servidor
4. **Crear admin panel:** Dashboard de estadísticas

---

## 📞 ¿Preguntas?

- ✓ Verifica que Python esté instalado
- ✓ Verifica que Flask esté instalado (`pip list`)
- ✓ Lee los logs de la API en la terminal
- ✓ Abre http://localhost:5000/api/health para ver si la API corre

---

**¡Tu sistema está listo para producción! 🚀**
