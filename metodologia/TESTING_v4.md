# 🚀 PRUEBAS RÁPIDAS - v4.0

## 1. REGISTRARSE COMO NUEVO USUARIO

1. Abre `login.html`
2. Haz clic en "📝 Crear Cuenta"
3. Rellena el formulario:
   - Nombre: Tu Nombre
   - Usuario: tunombre123
   - Contraseña: micontraseña123
   - Confirmar: micontraseña123
   - Tipo: Comprador (o el que prefieras)
4. Haz clic en "✓ Crear Cuenta"
5. Serás redirigido a login - inicia sesión con tus credenciales

## 2. GESTIÓN DE USUARIOS (ADMIN SOLO)

### Como Admin (admin / admin123):
1. Inicia sesión
2. En el menú, haz clic en "👥 Usuarios"
3. Puedes:
   - **Crear usuario**: Rellena el formulario y haz clic en "✓ Crear Usuario"
   - **Editar usuario**: Haz clic en "✏️ Editar" en una fila
   - **Eliminar usuario**: Haz clic en "🗑️ Eliminar" (con confirmación)

### Cambios que puedes hacer:
- Admin, Inspector, Tesorera, Comprador
- Nombre completo
- (Contraseña se define al crear)

## 3. CONFIGURACIÓN DEL SISTEMA

### Como Admin:
1. Haz clic en "⚙️ Configuración"
2. **Te pedirá contraseña**: Ingresa `admin123`
3. Acceso a dos secciones:

#### 🎨 Diseño
- Cambiar colores primarios
- Ajustar gradientes de fondo
- Subir imagen PNG/JPG de fondo
- Cambiar fuente y tamaño
- Ajustar opacidad de imagen

#### 📄 Encabezado/Pie
- **Encabezado**: Título, subtítulo, logo URL
- **Pie de Página**: Empresa, dirección, teléfono, email, copyright

Los cambios se aplican **instantáneamente a todas las páginas**

## 4. HEADER Y FOOTER EN TODAS LAS PÁGINAS

✓ Las siguientes páginas ahora tienen header y footer:
- index.html (Inicio)
- add_product.html (Agregar Producto)
- edit_product.html (Editar Producto)
- view_inventory.html (Ver Inventario)
- search_product.html (Buscar Producto)
- reports.html (Reportes)
- browse.html (Catálogo)
- cart.html (Carrito)
- user_management.html (Gestión de Usuarios)

Todas las páginas muestran el encabezado y pie personalizado desde config.html

## 5. NAVEGACIÓN MEJORADA

Todas las páginas ahora tienen:
- ✓ Botón "🏠 Inicio" (arriba a la derecha)
- ✓ Información de usuario (nombre + rol)
- ✓ Botón "Salir" (logout)
- ✓ Navegación coherente
- ✓ Header y footer personalizables

## 6. PERMISOS POR ROL

| Acción | Admin | Inspector | Tesorera | Comprador | Invitado |
|--------|-------|-----------|----------|-----------|----------|
| Ver inventario | ✓ | ✓ | ✓ | ✗ | ✗ |
| Agregar producto | ✓ | ✗ | ✗ | ✗ | ✗ |
| Editar producto | ✓ | ✗ | ✗ | ✗ | ✗ |
| Ver precios | ✓ | ✗ | ✓ | ✓ | ✓ |
| Ver reportes | ✓ | ✗ | ✓ | ✗ | ✗ |
| Comprar | ✗ | ✗ | ✗ | ✓ | ✓ |
| Carrito | ✗ | ✗ | ✗ | ✓ | ✓ |
| Config (protegida) | ✓ | ✗ | ✗ | ✗ | ✗ |
| Gestión usuarios | ✓ | ✗ | ✗ | ✗ | ✗ |

## 7. CONTRASEÑAS DE PRUEBA

```
Usuario: admin        Contraseña: admin123
Usuario: tester       Contraseña: tester123
Usuario: tesorera     Contraseña: tesorera123
Usuario: buyer        Contraseña: buyer123
```

## 8. PANTALLAS IMPORTANTES

### Login
- Usuarios de prueba predeterminados
- Link "📝 Crear Cuenta" para registro
- Botón "Continuar como Invitado" para comprar sin login

### Signup
- Validación de campos
- Selección de rol limitada (sin admin)
- Redirect a login tras éxito

### Configuración
- 🔒 Pantalla de bloqueo con contraseña
- Contraseña: `admin123`
- Dos pestañas: Diseño y Encabezado/Pie

### Gestión de Usuarios
- Tabla de usuarios con editar/eliminar
- Crear nuevos usuarios
- Solo accesible por admin

## 9. FUNCIONALIDADES CLAVE

✅ Registro completo de usuarios
✅ Gestión de usuarios con CRUD
✅ Configuración protegida con contraseña
✅ Header/Footer personalizables
✅ Header y footer en todas las páginas
✅ Botón de inicio en todas partes
✅ Control de acceso basado en roles
✅ Persistencia en localStorage
✅ Interfaz responsiva y moderna

## 10. ARCHIVOS CREADOS/MODIFICADOS

### Nuevos archivos:
- `signup.html` - Página de registro
- `user_management.html` - Panel de gestión de usuarios
- `UPDATE_v4.md` - Documentación de cambios

### Archivos modificados:
- `config.html` - Reescrito con protección y header/footer
- `login.html` - Agregado link a signup
- `index.html` - Actualizado menú y permisos
- `add_product.html` - Agregado header/footer
- `edit_product.html` - Agregado header/footer
- `view_inventory.html` - Agregado header/footer
- `search_product.html` - Agregado header/footer
- `reports.html` - Agregado header/footer
- `user_management.html` - Agregado header/footer
- `header_footer_admin.html` - Agregado header/footer (obsoleto - usar config.html)

## 🎯 PRÓXIMOS PASOS SUGERIDOS

1. Eliminar archivos obsoletos:
   - `header_footer_admin.html` (funcionalidad en config.html)
   - `config_new.html` (archivo temporal)

2. Funcionalidades adicionales:
   - Cambio de contraseña de usuario
   - Historial de cambios
   - Exportar/importar datos
   - Backup de configuración

3. Mejoras de seguridad:
   - Considerar hashing de contraseñas
   - Timeout de sesión
   - Validación de email
   - Logs de actividad
