document.addEventListener('DOMContentLoaded', function () {
    const consultasButton = document.getElementById('botaoConsultas');
    if (consultasButton) {
        consultasButton.addEventListener('click', function () {
            window.location.href = '/consultas/';
        });
    } else {
        console.error("Botão 'Consultas' não encontrado!");
    }
});
