# 🧹 ARCHIVOS A LIMPIAR

## Archivos Temporales / Obsoletos

### 1. **config_new.html** → RENOMBRAR a **config.html**
- Este es el archivo correcto con todas las características nuevas
- El config.html viejo es la versión antigua sin protección de contraseña
- **Acción**: Usar config_new.html como config.html (el viejo puede borrarse)

### 2. **header_footer_admin.html** → PUEDE BORRARSE
- Su funcionalidad ha sido integrada completamente en config.html
- Ya no se usa en ningún link del sistema
- No hay referencias activas a este archivo

## Instalaciones Manuales Recomendadas

Si deseas limpiar el proyecto, ejecuta:

```bash
# Opción 1: Usando comandos de sistema

# Eliminar el config.html viejo (CUIDADO: asegúrate de hacer backup)
del config.html

# Renombrar config_new.html a config.html
ren config_new.html config.html

# Eliminar header_footer_admin.html (ya no necesario)
del header_footer_admin.html
```

O manualmente:
1. Haz backup del proyecto
2. Abre `config_new.html`
3. Copia TODO su contenido
4. Reemplaza el contenido de `config.html` completamente
5. Elimina `config_new.html`
6. Elimina `header_footer_admin.html` (opcional pero recomendado)

## ✅ Archivos que SÍ NECESITAS

### HTML Pages
- ✅ index.html
- ✅ login.html
- ✅ signup.html ← NUEVO
- ✅ config.html (usar config_new.html)
- ✅ user_management.html ← NUEVO
- ✅ browse.html
- ✅ cart.html
- ✅ add_product.html
- ✅ edit_product.html
- ✅ view_inventory.html
- ✅ search_product.html
- ✅ reports.html

### Archivo JavaScript
- ✅ app.js (contiene toda la lógica)

### Estilos
- ✅ styles.css

### Documentación
- ✅ README.md
- ✅ QUICK_START.txt
- ✅ DEMO.md
- ✅ UPDATE_v3.md
- ✅ UPDATE_v4.md ← NUEVO
- ✅ TESTING_v4.md ← NUEVO
- ✅ FINAL_SUMMARY.md ← NUEVO
- ✅ CLEANUP_NOTES.md (este archivo)

## 🗑️ Archivos a Eliminar

- ❌ config_new.html (después de renombrar a config.html)
- ❌ header_footer_admin.html (funcionalidad integrada)

## 📋 Lista de Verificación

- [ ] Backup del proyecto realizado
- [ ] Renombrar config_new.html a config.html
- [ ] Eliminar config_new.html (si es posible)
- [ ] Eliminar header_footer_admin.html (si es necesario)
- [ ] Probar que config.html funciona
- [ ] Probar que login y signup funcionan
- [ ] Probar que user_management funciona
- [ ] Verificar que todas las páginas tienen header y footer

## 🔍 Verificación Post-Limpieza

Después de hacer la limpieza, verifica:

1. **Login**: Inicia sesión con admin/admin123
2. **Configuración**: 
   - Haz clic en ⚙️ Configuración
   - Ingresa contraseña: `admin123`
   - Deberías ver dos pestañas: Diseño y Encabezado/Pie
3. **Usuarios**:
   - Haz clic en 👥 Usuarios
   - Deberías ver tabla de usuarios y formulario de crear usuario
4. **Signup**:
   - Vuelve a login
   - Haz clic en "📝 Crear Cuenta"
   - Crea un nuevo usuario

## ✨ Resultado Final

Después de la limpieza tendrás:
- ✅ Sistema completo funcional
- ✅ Interfaz limpia sin archivos obsoletos
- ✅ Config.html con protección y header/footer
- ✅ Signup funcional
- ✅ User management completo
- ✅ Header y footer en todas las páginas
- ✅ Todo sincronizado y funcionando perfectamente

## 💡 Nota Importante

El archivo `config_new.html` fue creado como respaldo durante la migración. Una vez que confirmes que `config.html` funciona correctamente con todas las nuevas características, puedes eliminar `config_new.html` de forma segura.

Si algo falla, tienes `config_new.html` como copia de seguridad para restaurar.
