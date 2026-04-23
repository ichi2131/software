# 🎬 GUÍA RÁPIDA DE DEMOSTRACIÓN

## Primeros Pasos

### Paso 1: Abrir el sistema
1. Abre `login.html` en tu navegador
2. Verás la pantalla de login con credenciales de prueba

### Paso 2: Probar cada rol

---

## 🎯 DEMOSTRACIÓN 1: ADMIN

### Credenciales
- Usuario: `admin`
- Contraseña: `admin123`

### Qué puede hacer:
1. **Agregar Productos**
   - Click en "Agregar Producto"
   - Completa los campos
   - Producto aparece en "Ver Inventario"

2. **Editar Productos**
   - Ve a "Ver Inventario"
   - Click en "Editar" junto a cualquier producto
   - Modifica y actualiza

3. **Eliminar Productos**
   - Ve a "Ver Inventario"
   - Click en "Eliminar"
   - Confirma la eliminación

4. **Ver Reportes**
   - Click en "Reportes"
   - Ve stock bajo, valor total, productos por categoría
   - **Importante**: Solo admin ve los precios y valores

5. **Personalizar Diseño**
   - Click en "⚙️ Configuración"
   - Cambia colores, fuentes, fondos
   - **PRUEBA**: Sube una imagen PNG como fondo
   - Los cambios se aplican en TODAS las páginas

### Especial para Admin:
```
Prueba esto para ver la magia:
1. Ve a Configuración
2. En "Fondos y Gradientes", haz click en "📁 Selecciona una imagen"
3. Sube un archivo PNG o JPG de tu computadora
4. Verás el preview en tiempo real
5. Click en "Guardar Configuración"
6. Navega a otra página - ¡El fondo se aplicó a todas!
```

---

## 👁️ DEMOSTRACIÓN 2: TESTER (Inspector)

### Credenciales
- Usuario: `tester`
- Contraseña: `tester123`

### Qué puede hacer:
1. **Ver Inventario**
   - "Ver Inventario" aparece en el menú
   - Ve la lista de productos
   - **NOTA**: Columna de "Precio" NO aparece (está oculta)

2. **Buscar Productos**
   - Click en "Buscar Producto"
   - Busca por nombre o categoría
   - **NOTA**: Precios no se muestran

3. **Monitorear Stock**
   - Ve cantidad de cada producto
   - Identifica stock bajo (<10 unidades)
   - Productos resaltados en rojo

### Qué NO puede hacer:
- ❌ "Agregar Producto" - NO aparece en el menú
- ❌ Botones de editar/eliminar - NO son visibles
- ❌ "Reportes" - NO aparece en el menú
- ❌ "Configuración" - NO aparece en el menú
- ❌ Ver precios en ninguna parte

### Ejemplo de Restricción:
```
Intenta esto:
1. Abre Dev Tools (F12)
2. Ve a Application → localStorage
3. Cambia "role" de "tester" a "admin"
4. Recarga la página
5. ¡Ahora verás todo lo que antes estaba oculto!
```

---

## 💰 DEMOSTRACIÓN 3: TESORERA

### Credenciales
- Usuario: `tesorera`
- Contraseña: `tesorera123`

### Qué puede hacer:
1. **Ver Inventario**
   - "Ver Inventario" aparece
   - Ve lista de productos
   - **IMPORTANTE**: Puede ver PRECIOS
   - Botones de editar/eliminar NO aparecen

2. **Generar Reportes**
   - Click en "Reportes"
   - Ve stock bajo
   - Ve VALOR TOTAL del inventario
   - Ve productos por categoría con valores

3. **Calcular Inversión**
   - Acceso a todos los precios
   - Puede ver valor total del stock
   - Desglose por categoría

### Qué NO puede hacer:
- ❌ "Agregar Producto" - NO aparece
- ❌ Botones de editar/eliminar - NO visibles
- ❌ "Configuración" - NO accesible
- ❌ Modificar datos - Solo lectura

---

## 🔄 DEMOSTRACIÓN 4: CAMBIAR FONDOS (ADMIN)

### Paso a Paso

#### Opción 1: Subir Archivo Local
1. Login como admin
2. Ve a "⚙️ Configuración"
3. Baja a "🌈 Fondos y Gradientes"
4. Selecciona "Imagen de Fondo (PNG/JPG)"
5. Click en "📁 Selecciona una imagen"
6. Elige un archivo de tu computadora (PNG, JPG, etc.)
7. Verás preview del fondo
8. Click "💾 Guardar Configuración"
9. ¡Listo! El fondo se aplicó a TODAS las páginas

#### Opción 2: Usar URL de Internet
1. Login como admin
2. Ve a "⚙️ Configuración"
3. En "O URL de Imagen de Fondo", pega esta URL:
   ```
   https://images.unsplash.com/photo-1557804506-669714026ba8?w=1200
   ```
4. Click "💾 Guardar Configuración"
5. ¡El fondo se cambió instantáneamente!

#### Opción 3: Cambiar Opacidad
1. Usa el slider "Opacidad del Fondo"
2. 100% = Totalmente visible
3. 50% = Semi transparente
4. 0% = Completamente transparente
5. Los cambios se ven en tiempo real

---

## 🎨 DEMOSTRACIÓN 5: PERSONALIZAR COLORES

### Cambiar Tema de Colores
1. Login como admin
2. Ve a "⚙️ Configuración"
3. En "🎨 Colores Principales":
   - Cambia "Color Primario" → Haz clic en la caja de color
   - Selecciona un color rojo brillante
   - El header y botones cambian automáticamente

4. En "✅ Colores de Estado":
   - Cambia color de éxito (verde)
   - Cambiar color de error (rojo diferente)

5. Click "💾 Guardar Configuración"

### Cambiar Tipografía
1. En "🔤 Tipografía"
2. Selecciona "Comic Sans MS" (o tu favorita)
3. Los cambios se aplican inmediatamente
4. Click guardar

---

## 🔐 DEMOSTRACIÓN 6: SEGURIDAD Y PERMISOS

### Prueba 1: Acceso Negado
1. Login como `tester`
2. Intenta acceder directamente a: `add_product.html`
3. Se te redirigirá a la página de inicio
4. Mensaje: "No tienes permiso para agregar productos"

### Prueba 2: Restringe Información
1. Login como `tester`
2. Ve a "Ver Inventario"
3. Nota que NO ves precios (columna oculta)
4. Logout

5. Login como `admin`
6. Ve a "Ver Inventario"
7. ¡Ahora sí ves los precios!

### Prueba 3: Logout de Seguridad
1. En cualquier página, arriba a la derecha verás tu rol
2. Click en "Salir"
3. Se cierra tu sesión
4. Se redirige a login.html
5. Tu sesión fue eliminada

---

## 📊 DEMOSTRACIÓN 7: FLUJO COMPLETO DE TRABAJO

### Escenario: Gerente de Inventario

**Usuario: Admin**
1. Login
2. Ve a "Agregar Producto"
   - Nombre: "Laptop Dell XPS"
   - Descripción: "Computadora portátil de 15 pulgadas"
   - Cantidad: 5
   - Precio: $1200.00
   - Categoría: Electrónicos
   - Proveedor: TechStore
3. Click "Agregar Producto"
4. Ve a "Ver Inventario"
   - Ves el nuevo producto en la lista
5. Click "Configuración"
   - Cambia color primario a azul marino
   - Sube un fondo profesional
   - Guarda

**Usuario: Tesorera (después)**
1. Login como `tesorera`
2. Ve a "Reportes"
3. Ve que hay 5 laptops a $1200 = $6000 en stock
4. Ve gráfico por categoría (Electrónicos: $6000)

**Usuario: Inspector (después)**
1. Login como `tester`
2. Ve a "Ver Inventario"
3. Ve que hay 5 laptops (stock OK, >10)
4. NO ve el precio (está oculto)

---

## 💡 TIPS Y TRUCOS

### Tip 1: Cambios en Tiempo Real
- Cambio un color en Configuración
- El preview se actualiza INMEDIATAMENTE
- No necesitas guardar para ver cambios en el preview

### Tip 2: Fondos Más Rápidos
- Sube una imagen local es más rápido que URLs
- PNG: Mejor calidad, más tamaño
- JPG: Menos tamaño, buena calidad
- WebP: Mejor compresión (si tu navegador lo soporta)

### Tip 3: Busca Inteligente
- En "Buscar Producto", búsqueda en TIEMPO REAL
- Mientras escribes, se filtran resultados
- Puedes filtrar por categoría

### Tip 4: Stock Bajo
- En "Ver Inventario", productos con <10 unidades se destacan en rojo
- En "Reportes", hay una sección especial de stock bajo

### Tip 5: Datos Locales
- Todo se guarda en localStorage del navegador
- Si limpias datos del navegador (Ctrl+Shift+Delete), pierdes todo
- Es 100% local - no necesita servidor

---

## 🐛 SI ALGO NO FUNCIONA

### Problema: No puedo hacer login
**Solución**: Verifica las credenciales exactas:
```
Admin: admin / admin123
Tester: tester / tester123
Tesorera: tesorera / tesorera123
```

### Problema: No veo cambios después de guardar
**Solución**: 
1. Recarga la página (F5 o Ctrl+R)
2. Prueba Ctrl+F5 (recarga forzada sin caché)
3. Revisa que hagas clic en "Guardar"

### Problema: Desaparecieron mis cambios
**Solución**: Revisa que no hayas:
- Limpiado datos del navegador
- Borrado cookies/localStorage
- Abierto en navegador de incógnito (los datos no persisten)

---

## 🎉 ¡LISTO!

Ya puedes explorar el sistema completamente. ¡Diviértete probando todas las funcionalidades!

Recuerda:
- 🔐 Cada rol tiene acceso diferente
- 🎨 Personaliza el diseño como quieras
- 📸 Sube tus propias imágenes
- 👥 Cambia entre usuarios para ver diferencias
