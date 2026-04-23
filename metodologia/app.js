// app.js - Funciones comunes para el sistema de inventario

// ============ AUTENTICACIÓN Y AUTORIZACIÓN ============
function initializeUsers() {
    const users = JSON.parse(localStorage.getItem('users')) || null;
    if (!users) {
        const defaultUsers = [
            { id: 1, username: 'owner', password: 'owner123', role: 'owner', fullName: 'Owner' },
            { id: 2, username: 'admin', password: 'admin123', role: 'admin', fullName: 'Administrador' },
            { id: 3, username: 'tester', password: 'tester123', role: 'tester', fullName: 'Inspector' },
            { id: 4, username: 'tesorera', password: 'tesorera123', role: 'tesorera', fullName: 'Tesorera' },
            { id: 5, username: 'buyer', password: 'buyer123', role: 'buyer', fullName: 'Comprador' }
        ];
        localStorage.setItem('users', JSON.stringify(defaultUsers));
    }
}

function initializeProducts() {
    const products = JSON.parse(localStorage.getItem('products')) || null;
    if (!products || products.length === 0) {
        const defaultProducts = [
            { id: 1, name: 'Laptop Dell XPS', description: 'Laptop de alto rendimiento', quantity: 5, price: 800, category: 'Electrónicos' },
            { id: 2, name: 'Mouse Logitech MX', description: 'Mouse inalámbrico de precisión', quantity: 50, price: 25, category: 'Accesorios' },
            { id: 3, name: 'Teclado Mecánico', description: 'Teclado gaming RGB', quantity: 30, price: 120, category: 'Accesorios' },
            { id: 4, name: 'Monitor LG 27" 4K', description: 'Monitor ultra HD', quantity: 8, price: 300, category: 'Electrónicos' },
            { id: 5, name: 'Camiseta Algodón', description: 'Camiseta 100% algodón', quantity: 100, price: 20, category: 'Ropa' },
            { id: 6, name: 'Pantalón Denim', description: 'Pantalón blue jean', quantity: 75, price: 40, category: 'Ropa' },
            { id: 7, name: 'Arroz Premium', description: 'Arroz basmati 5kg', quantity: 200, price: 2, category: 'Alimentos' },
            { id: 8, name: 'Aceite de Oliva', description: 'Aceite premium 1L', quantity: 50, price: 8, category: 'Alimentos' }
        ];
        localStorage.setItem('products', JSON.stringify(defaultProducts));
    }
}

function getCurrentUser() {
    return JSON.parse(localStorage.getItem('currentUser')) || null;
}

function setCurrentUser(user) {
    localStorage.setItem('currentUser', JSON.stringify(user));
}

function loginGuest() {
    const guestUser = { id: 999, username: 'guest', role: 'guest', fullName: 'Invitado' };
    setCurrentUser(guestUser);
}

function login(username, password) {
    const users = JSON.parse(localStorage.getItem('users')) || [];
    const user = users.find(u => u.username === username && u.password === password);
    if (user) {
        const userData = { ...user };
        delete userData.password;
        setCurrentUser(userData);
        return true;
    }
    return false;
}

function logout() {
    localStorage.removeItem('currentUser');
}

function hasRole(role) {
    const user = getCurrentUser();
    return user && user.role === role;
}

function hasPermission(permission) {
    const user = getCurrentUser();
    if (!user) return false;
    
    const permissions = {
        'owner': ['view_inventory', 'edit_product', 'delete_product', 'add_product', 'view_reports', 'view_users', 'view_config', 'manage_users'],
        'admin': ['view_inventory', 'edit_product', 'delete_product', 'add_product', 'view_reports', 'view_users', 'view_config', 'manage_users'],
        'tester': ['view_inventory', 'view_stock'],
        'tesorera': ['view_inventory', 'view_prices', 'view_reports'],
        'buyer': ['view_inventory', 'view_prices', 'add_to_cart', 'view_cart'],
        'guest': ['view_inventory', 'view_prices', 'add_to_cart', 'view_cart']
    };
    
    return permissions[user.role] && permissions[user.role].includes(permission);
}

function checkAuth() {
    if (!getCurrentUser()) {
        window.location.href = 'login.html';
    }
}

// ============ GESTIÓN DE USUARIOS ============
function getAllUsers() {
    return JSON.parse(localStorage.getItem('users')) || [];
}

function usernameExists(username) {
    const users = getAllUsers();
    return users.some(u => u.username.toLowerCase() === username.toLowerCase());
}

function registerUser(username, password, fullName, role) {
    // Validaciones
    if (!username || !password || !fullName) {
        return { success: false, message: 'Todos los campos son requeridos' };
    }
    
    if (username.length < 3) {
        return { success: false, message: 'El usuario debe tener al menos 3 caracteres' };
    }
    
    if (password.length < 6) {
        return { success: false, message: 'La contraseña debe tener al menos 6 caracteres' };
    }
    
    if (usernameExists(username)) {
        return { success: false, message: 'El usuario ya existe' };
    }
    
    const users = getAllUsers();
    const newUser = {
        id: Math.max(...users.map(u => u.id), 0) + 1,
        username: username.toLowerCase(),
        password: password,
        role: role || 'buyer',
        fullName: fullName
    };
    
    users.push(newUser);
    localStorage.setItem('users', JSON.stringify(users));
    
    return { success: true, message: 'Usuario creado exitosamente', user: newUser };
}

function updateUser(userId, updates) {
    const users = getAllUsers();
    const userIndex = users.findIndex(u => u.id === userId);
    
    if (userIndex === -1) {
        return { success: false, message: 'Usuario no encontrado' };
    }
    
    // Validar si el username ya existe (para otros usuarios)
    if (updates.username && updates.username !== users[userIndex].username) {
        if (usernameExists(updates.username)) {
            return { success: false, message: 'El usuario ya existe' };
        }
    }
    
    users[userIndex] = { ...users[userIndex], ...updates };
    localStorage.setItem('users', JSON.stringify(users));
    
    return { success: true, message: 'Usuario actualizado', user: users[userIndex] };
}

function deleteUser(userId) {
    const users = getAllUsers();
    const admin = users.find(u => u.role === 'admin');
    
    // Proteger contra eliminación del último admin
    if (users[users.findIndex(u => u.id === userId)].role === 'admin' && 
        users.filter(u => u.role === 'admin').length === 1) {
        return { success: false, message: 'No puedes eliminar el último administrador' };
    }
    
    const filtered = users.filter(u => u.id !== userId);
    localStorage.setItem('users', JSON.stringify(filtered));
    
    return { success: true, message: 'Usuario eliminado' };
}

// ============ CARRITO DE COMPRAS ============
function getCart() {
    return JSON.parse(localStorage.getItem('cart')) || [];
}

function saveCart(cart) {
    localStorage.setItem('cart', JSON.stringify(cart));
}

function addToCart(product) {
    let cart = getCart();
    const existingItem = cart.find(item => item.id === product.id);
    
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({
            id: product.id,
            name: product.name,
            price: product.price,
            quantity: 1
        });
    }
    
    saveCart(cart);
    return true;
}

function removeFromCart(productId) {
    let cart = getCart();
    cart = cart.filter(item => item.id !== productId);
    saveCart(cart);
}

function updateCartQuantity(productId, quantity) {
    let cart = getCart();
    const item = cart.find(item => item.id === productId);
    if (item) {
        item.quantity = Math.max(1, quantity);
        saveCart(cart);
    }
}

function clearCart() {
    localStorage.removeItem('cart');
}

function getCartTotal() {
    const cart = getCart();
    return cart.reduce((total, item) => total + (item.price * item.quantity), 0);
}

function getCartItemCount() {
    const cart = getCart();
    return cart.reduce((count, item) => count + item.quantity, 0);
}

// Inicializar usuarios y productos al cargar
initializeUsers();
initializeProducts();

// ============ CONFIGURACIÓN DE DISEÑO ============
function getDesignConfig() {
    return JSON.parse(localStorage.getItem('designConfig')) || null;
}

function saveDesignConfig(config) {
    localStorage.setItem('designConfig', JSON.stringify(config));
    applyDesignConfig(config);
}

function applyDesignConfig(config) {
    if (!config) return;
    
    document.documentElement.style.setProperty('--primary-color', config.primaryColor || '#2196f3');
    document.documentElement.style.setProperty('--primary-light', config.primaryLightColor || '#21cbf3');
    document.documentElement.style.setProperty('--text-color', config.textColor || '#333333');
    document.documentElement.style.setProperty('--border-color', config.borderColor || '#dddddd');
    document.documentElement.style.setProperty('--bg-gradient-1', config.bgGradient1 || '#e3f2fd');
    document.documentElement.style.setProperty('--bg-gradient-2', config.bgGradient2 || '#bbdefb');
    document.documentElement.style.setProperty('--success-bg', config.successBg || '#d4edda');
    document.documentElement.style.setProperty('--success-text', config.successText || '#155724');
    document.documentElement.style.setProperty('--error-bg', config.errorBg || '#f8d7da');
    document.documentElement.style.setProperty('--error-text', config.errorText || '#721c24');
    document.documentElement.style.setProperty('--font-family', config.fontFamily || "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif");
    document.documentElement.style.setProperty('--border-radius', (config.borderRadius || '5') + 'px');
    document.documentElement.style.setProperty('--form-spacing', (config.formSpacing || '20') + 'px');
    
    const useImage = config.useBackgroundImage && config.backgroundImageUrl;
    if (useImage) {
        const opacity = (config.backgroundOpacity || 100) / 100;
        document.documentElement.style.setProperty('--bg-image', `url('${config.backgroundImageUrl}')`);
        document.documentElement.style.setProperty('--bg-opacity', opacity);
    } else {
        document.documentElement.style.setProperty('--bg-image', 'none');
        document.documentElement.style.setProperty('--bg-opacity', '1');
    }
    
    // Aplicar colores de botones
    const style = document.getElementById('dynamic-styles') || document.createElement('style');
    style.id = 'dynamic-styles';
    style.textContent = `
        .edit { background-color: ${config.editColor || '#ffc107'} !important; }
        .edit:hover { background-color: ${config.editHover || '#e0a800'} !important; }
        .delete { background-color: ${config.deleteColor || '#dc3545'} !important; }
        .delete:hover { background-color: ${config.deleteHover || '#c82333'} !important; }
    `;
    if (!document.getElementById('dynamic-styles')) {
        document.head.appendChild(style);
    }
}

// Aplicar configuración al cargar cualquier página
window.addEventListener('DOMContentLoaded', () => {
    const config = getDesignConfig();
    if (config) {
        applyDesignConfig(config);
    }
});

// ============ GESTIÓN DE INVENTARIO ============
function getInventory() {
    return JSON.parse(localStorage.getItem('inventory')) || [];
}

function addProduct(product) {
    const inventory = getInventory();
    product.id = Date.now();
    product.dateAdded = new Date().toISOString();
    inventory.push(product);
    localStorage.setItem('inventory', JSON.stringify(inventory));
}

function updateProduct(id, updatedProduct) {
    let inventory = getInventory();
    const index = inventory.findIndex(p => p.id === id);
    if (index !== -1) {
        inventory[index] = { ...inventory[index], ...updatedProduct };
        localStorage.setItem('inventory', JSON.stringify(inventory));
    }
}

function deleteProduct(id) {
    let inventory = getInventory();
    inventory = inventory.filter(p => p.id !== id);
    localStorage.setItem('inventory', JSON.stringify(inventory));
}

function searchProducts(query) {
    const inventory = getInventory();
    return inventory.filter(product =>
        product.name.toLowerCase().includes(query.toLowerCase()) ||
        product.category.toLowerCase().includes(query.toLowerCase()) ||
        product.supplier.toLowerCase().includes(query.toLowerCase())
    );
}

// Funciones adicionales para estadísticas
function getTotalValue() {
    const inventory = getInventory();
    return inventory.reduce((total, product) => total + (product.price * product.quantity), 0);
}

function getLowStockProducts(threshold = 10) {
    const inventory = getInventory();
    return inventory.filter(product => product.quantity < threshold);
}

function getProductsByCategory() {
     const inventory = getInventory();
    const categories = {};
    inventory.forEach(product => {
        if (!categories[product.category]) {
            categories[product.category] = [];
        }
        categories[product.category].push(product);
    });
    return categories;
}

// ============ HEADER Y FOOTER ============
function getHeaderConfig() {
    return JSON.parse(localStorage.getItem('headerConfig')) || {
        title: 'Sistema de Administración de Inventario',
        subtitle: 'Gestiona tu inventario de forma eficiente',
        logoText: '📦'
    };
}

function saveHeaderConfig(config) {
    localStorage.setItem('headerConfig', JSON.stringify(config));
}

function getFooterConfig() {
    return JSON.parse(localStorage.getItem('footerConfig')) || {
        companyName: 'Mi Empresa',
        address: 'Dirección de la empresa',
        phone: '(+1) 555-0000',
        email: 'info@empresa.com',
        copyright: '© 2026 Todos los derechos reservados'
    };
}

function saveFooterConfig(config) {
    localStorage.setItem('footerConfig', JSON.stringify(config));
}

function renderHeader() {
    const config = getHeaderConfig();
    const user = getCurrentUser();
    const cartCount = hasPermission('add_to_cart') ? getCartItemCount() : 0;
    
    const header = document.createElement('header');
    header.id = 'main-header';
    header.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 20px;">
            <div>
                <h1 style="margin: 0; font-size: 2em;">${config.logoText} ${config.title}</h1>
                <p style="margin: 5px 0 0 0; font-size: 0.9em; color: rgba(255,255,255,0.8);">${config.subtitle}</p>
            </div>
            <div style="display: flex; gap: 20px; align-items: center;">
                ${cartCount > 0 ? `<a href="cart.html" style="color: white; font-size: 1.5em;">🛒 (${cartCount})</a>` : ''}
                <div style="background: rgba(255,255,255,0.2); padding: 10px 15px; border-radius: var(--border-radius);">
                    <span style="color: white;">${user.fullName || user.username}</span>
                </div>
            </div>
        </div>
    `;
    
    const body = document.body;
    if (document.querySelector('header')) {
        document.querySelector('header').replaceWith(header);
    } else {
        body.insertBefore(header, body.firstChild);
    }
}

function renderFooter() {
    const config = getFooterConfig();
    
    const footer = document.createElement('footer');
    footer.id = 'main-footer';
    footer.style.cssText = `
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-light) 100%);
        color: white;
        padding: 30px 20px;
        margin-top: 50px;
        text-align: center;
    `;
    footer.innerHTML = `
        <div style="max-width: 1200px; margin: 0 auto;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 20px;">
                <div>
                    <h3 style="margin-top: 0;">${config.companyName}</h3>
                    <p>${config.address}</p>
                </div>
                <div>
                    <h3 style="margin-top: 0;">Contacto</h3>
                    <p>📞 ${config.phone}</p>
                    <p>📧 ${config.email}</p>
                </div>
                <div>
                    <h3 style="margin-top: 0;">Links</h3>
                    <p><a href="index.html" style="color: white; text-decoration: none;">Inicio</a></p>
                    <p><a href="view_inventory.html" style="color: white; text-decoration: none;">Inventario</a></p>
                </div>
            </div>
            <hr style="opacity: 0.3;">
            <p style="margin: 15px 0 0 0;">${config.copyright}</p>
        </div>
    `;
    
    const body = document.body;
    if (document.querySelector('footer')) {
        document.querySelector('footer').replaceWith(footer);
    } else {
        body.appendChild(footer);
    }
}

// ============ EXPORTAR DATOS PARA GRÁFICOS ============
function exportInventoryData() {
    const products = JSON.parse(localStorage.getItem('products')) || [];
    const timestamp = new Date().toISOString();
    
    const data = {
        timestamp,
        products,
        summary: {
            totalProducts: products.length,
            totalQuantity: products.reduce((sum, p) => sum + (p.quantity || 0), 0),
            totalValue: products.reduce((sum, p) => sum + (p.quantity * p.price || 0), 0)
        }
    };
    
    // Guardar en archivo (si está en Node/Electron)
    if (typeof require !== 'undefined') {
        const fs = require('fs');
        fs.writeFileSync('inventory.json', JSON.stringify(data, null, 2));
    }
    
    return data;
}

function getInventorySummary() {
    const products = JSON.parse(localStorage.getItem('products')) || [];
    const categories = {};
    
    products.forEach(product => {
        const cat = product.category || 'Sin categoría';
        if (!categories[cat]) {
            categories[cat] = { quantity: 0, value: 0, products: 0 };
        }
        categories[cat].quantity += product.quantity || 0;
        categories[cat].value += (product.quantity || 0) * (product.price || 0);
        categories[cat].products += 1;
    });
    
    return {
        totalProducts: products.length,
        totalQuantity: products.reduce((sum, p) => sum + (p.quantity || 0), 0),
        totalValue: products.reduce((sum, p) => sum + (p.quantity * p.price || 0), 0),
        categories
    };
}

// ============ FUNCIONES DE INVENTARIO (compatibilidad) ============
function getInventory() {
    return JSON.parse(localStorage.getItem('products')) || [];
}

function getTotalValue() {
    const products = getInventory();
    return products.reduce((total, p) => total + (p.quantity * p.price || 0), 0);
}

function getLowStockProducts() {
    const products = getInventory();
    return products.filter(p => p.quantity < 10);
}