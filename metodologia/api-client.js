// api-client.js - Cliente para comunicarse con la API de inventario

const API_BASE_URL = 'http://localhost:5000/api';

// ============ AUTENTICACIÓN ============
async function login(username, password) {
    try {
        const response = await fetch(`${API_BASE_URL}/login`, {
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
    } catch (error) {
        console.error('Error en login:', error);
        return false;
    }
}

async function logout() {
    try {
        await fetch(`${API_BASE_URL}/logout`, {
            method: 'POST',
            credentials: 'include'
        });
        
        localStorage.removeItem('currentUser');
        return true;
    } catch (error) {
        console.error('Error en logout:', error);
        return false;
    }
}

async function signup(username, password, fullName) {
    try {
        const response = await fetch(`${API_BASE_URL}/signup`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
            body: JSON.stringify({ username, password, fullName })
        });
        
        const data = await response.json();
        if (response.ok) {
            localStorage.setItem('currentUser', JSON.stringify(data.user));
            return { success: true, user: data.user };
        }
        
        return { success: false, error: data.error };
    } catch (error) {
        console.error('Error en signup:', error);
        return { success: false, error: 'Error de conexión' };
    }
}

async function getCurrentUser() {
    // Primero intenta obtener del localStorage
    const cached = localStorage.getItem('currentUser');
    if (cached) {
        return JSON.parse(cached);
    }
    
    // Si no, intenta obtener del servidor
    try {
        const response = await fetch(`${API_BASE_URL}/current-user`, {
            credentials: 'include'
        });
        const data = await response.json();
        
        if (data.user) {
            localStorage.setItem('currentUser', JSON.stringify(data.user));
            return data.user;
        }
    } catch (error) {
        console.error('Error obteniendo usuario actual:', error);
    }
    
    return null;
}

function setCurrentUser(user) {
    if (user) {
        localStorage.setItem('currentUser', JSON.stringify(user));
    } else {
        localStorage.removeItem('currentUser');
    }
}

async function loginGuest() {
    const guestUser = { id: 999, username: 'guest', role: 'guest', fullName: 'Invitado' };
    setCurrentUser(guestUser);
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
async function getAllUsers() {
    try {
        const response = await fetch(`${API_BASE_URL}/users`, {
            credentials: 'include'
        });
        
        if (response.ok) {
            const data = await response.json();
            return data.users || [];
        }
        return [];
    } catch (error) {
        console.error('Error obteniendo usuarios:', error);
        return [];
    }
}

async function updateUser(userId, updates) {
    try {
        const response = await fetch(`${API_BASE_URL}/users/${userId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
            body: JSON.stringify(updates)
        });
        
        return response.ok;
    } catch (error) {
        console.error('Error actualizando usuario:', error);
        return false;
    }
}

async function deleteUser(userId) {
    try {
        const response = await fetch(`${API_BASE_URL}/users/${userId}`, {
            method: 'DELETE',
            credentials: 'include'
        });
        
        return response.ok;
    } catch (error) {
        console.error('Error eliminando usuario:', error);
        return false;
    }
}

async function resetUsers() {
    try {
        const response = await fetch(`${API_BASE_URL}/reset-users`, {
            method: 'POST',
            credentials: 'include'
        });
        
        return response.ok;
    } catch (error) {
        console.error('Error reseteando usuarios:', error);
        return false;
    }
}

// ============ GESTIÓN DE PRODUCTOS ============
async function getAllProducts() {
    try {
        const response = await fetch(`${API_BASE_URL}/products`, {
            credentials: 'include'
        });
        
        if (response.ok) {
            const data = await response.json();
            return data.products || [];
        }
        return [];
    } catch (error) {
        console.error('Error obteniendo productos:', error);
        return [];
    }
}

async function getProduct(productId) {
    try {
        const response = await fetch(`${API_BASE_URL}/products/${productId}`, {
            credentials: 'include'
        });
        
        if (response.ok) {
            const data = await response.json();
            return data.product;
        }
        return null;
    } catch (error) {
        console.error('Error obteniendo producto:', error);
        return null;
    }
}

async function addProduct(name, description, quantity, price, category) {
    try {
        const response = await fetch(`${API_BASE_URL}/products`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
            body: JSON.stringify({ name, description, quantity, price, category })
        });
        
        if (response.ok) {
            const data = await response.json();
            return data.product;
        }
        return null;
    } catch (error) {
        console.error('Error agregando producto:', error);
        return null;
    }
}

async function updateProduct(productId, updates) {
    try {
        const response = await fetch(`${API_BASE_URL}/products/${productId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
            body: JSON.stringify(updates)
        });
        
        return response.ok;
    } catch (error) {
        console.error('Error actualizando producto:', error);
        return false;
    }
}

async function deleteProduct(productId) {
    try {
        const response = await fetch(`${API_BASE_URL}/products/${productId}`, {
            method: 'DELETE',
            credentials: 'include'
        });
        
        return response.ok;
    } catch (error) {
        console.error('Error eliminando producto:', error);
        return false;
    }
}

async function resetProducts() {
    try {
        const response = await fetch(`${API_BASE_URL}/reset-products`, {
            method: 'POST',
            credentials: 'include'
        });
        
        return response.ok;
    } catch (error) {
        console.error('Error reseteando productos:', error);
        return false;
    }
}

// ============ GESTIÓN DE CARRITO ============
async function getCart() {
    try {
        const response = await fetch(`${API_BASE_URL}/cart`, {
            credentials: 'include'
        });
        
        if (response.ok) {
            const data = await response.json();
            return data.cart || [];
        }
        return [];
    } catch (error) {
        console.error('Error obteniendo carrito:', error);
        return [];
    }
}

async function addToCart(productId, quantity) {
    try {
        const response = await fetch(`${API_BASE_URL}/cart`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
            body: JSON.stringify({ product_id: productId, quantity })
        });
        
        return response.ok;
    } catch (error) {
        console.error('Error agregando al carrito:', error);
        return false;
    }
}

async function removeFromCart(cartItemId) {
    try {
        const response = await fetch(`${API_BASE_URL}/cart/${cartItemId}`, {
            method: 'DELETE',
            credentials: 'include'
        });
        
        return response.ok;
    } catch (error) {
        console.error('Error eliminando del carrito:', error);
        return false;
    }
}

async function clearCart() {
    try {
        const response = await fetch(`${API_BASE_URL}/cart/clear`, {
            method: 'POST',
            credentials: 'include'
        });
        
        return response.ok;
    } catch (error) {
        console.error('Error limpiando carrito:', error);
        return false;
    }
}

// ============ AUDITORÍA ============
async function getActivityLog(limit = 100) {
    try {
        const response = await fetch(`${API_BASE_URL}/activity-log?limit=${limit}`, {
            credentials: 'include'
        });
        
        if (response.ok) {
            const data = await response.json();
            return data.logs || [];
        }
        return [];
    } catch (error) {
        console.error('Error obteniendo log:', error);
        return [];
    }
}

// ============ FUNCIONES HEREDADAS (para compatibilidad) ============
function initializeUsers() {
    // Ya no es necesario con la API
}

function initializeProducts() {
    // Ya no es necesario con la API
}

function usernameExists(username) {
    // Esta validación se hace en el servidor
    return false;
}
