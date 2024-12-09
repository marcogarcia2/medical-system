document.getElementById('Consultas').addEventListener('click', function () {
    // Simulação de estado de login; no backend, você usaria cookies ou APIs
    const usuarioLogado = false; // Substitua isso pela verificação real do backend

    if (!usuarioLogado) {
        // Redireciona para a página de login
        window.location.href = '/login/';
    } else {
        // Redireciona para a página de consultas
        window.location.href = '/consultas/';
    }
});
