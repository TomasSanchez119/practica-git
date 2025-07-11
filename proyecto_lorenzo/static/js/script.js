document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.querySelector('.login-form');
    
    // Función para validar el formulario antes del envío
    function validarFormulario() {
        const email = document.querySelector('input[name="email"]').value;
        const password = document.querySelector('input[name="password"]').value;
        
        // Validar que los campos no estén vacíos
        if (!email || !password) {
            alert('Por favor, completa todos los campos');
            return false;
        }
        
        // Validar formato de email
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Por favor, ingresa un email válido');
            return false;
        }
        
        return true;
    }
    
    loginForm.addEventListener('submit', (e) => {
        // Solo validar, no prevenir el envío del formulario
        if (!validarFormulario()) {
            e.preventDefault();
        }
    });
    
    // Función para verificar si el usuario ya está logueado
    function verificarSesion() {
        const usuarioLogueado = localStorage.getItem('usuarioLogueado');
        if (usuarioLogueado) {
            // Si ya está logueado, redirigir directamente
            window.location.href = 'casomusica_modificado.html';
        }
    }
    
    // Verificar sesión al cargar la página
    verificarSesion();
}); 