document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.querySelector('.login-form');
    
    // Función para validar el formulario de registro antes del envío
    function validarFormularioRegistro() {
        const email = document.querySelector('input[name="email"]').value;
        const password = document.querySelector('input[name="password"]').value;
        const confirmPassword = document.querySelector('input[name="confirm_password"]').value;
        
        // Validar que los campos no estén vacíos
        if (!email || !password || !confirmPassword) {
            alert('Por favor, completa todos los campos');
            return false;
        }
        
        // Validar formato de email
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Por favor, ingresa un email válido');
            return false;
        }
        
        // Validar que la contraseña tenga al menos 6 caracteres
        if (password.length < 6) {
            alert('La contraseña debe tener al menos 6 caracteres');
            return false;
        }
        
        // Validar que las contraseñas coincidan
        if (password !== confirmPassword) {
            alert('Las contraseñas no coinciden');
            return false;
        }
        
        return true;
    }
    
    registerForm.addEventListener('submit', (e) => {
        // Solo validar, no prevenir el envío del formulario
        if (!validarFormularioRegistro()) {
            e.preventDefault();
        }
    });
    
    // Validación en tiempo real para confirmar contraseña
    const passwordInput = document.querySelector('input[name="password"]');
    const confirmPasswordInput = document.querySelector('input[name="confirm_password"]');
    
    function validarCoincidenciaContraseñas() {
        const password = passwordInput.value;
        const confirmPassword = confirmPasswordInput.value;
        
        if (confirmPassword && password !== confirmPassword) {
            confirmPasswordInput.style.borderColor = '#ff4444';
        } else if (confirmPassword) {
            confirmPasswordInput.style.borderColor = '#4CAF50';
        } else {
            confirmPasswordInput.style.borderColor = '';
        }
    }
    
    passwordInput.addEventListener('input', validarCoincidenciaContraseñas);
    confirmPasswordInput.addEventListener('input', validarCoincidenciaContraseñas);
}); 