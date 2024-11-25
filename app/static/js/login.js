// adc evento no forms de login
document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault(); // evita o envio tradicional do formulário

    // coleta os dados do formulário
    const formData = new FormData(this);

    // envia os dados para o servidor via POST
    fetch("/login", {
        method: "POST",
        body: formData
    })
    .then(response => response.json()) // processa a resposta JSON do servidor
    .then(data => {
        if (data.success) {
            // login bem-sucedido, exibe o SweetAlert
            Swal.fire({
                icon: 'success',
                title: 'Login bem-sucedido!',
                text: 'Redirecionando para os produtos...',
                showConfirmButton: false,
                timer: 1500
            }).then(() => {
                // redireciona para a página de produtos
                window.location.href = data.redirect_url;
            });
        } else {
            // erro no login
            Swal.fire({
                icon: 'error',
                title: 'Erro!',
                text: data.message  // msg de erro vinda do servidor
            });
        }
    })
    .catch(error => {
        // caso algo de errado aconteça
        console.error('Erro:', error);
        Swal.fire({
            icon: 'error',
            title: 'Erro!',
            text: 'Houve um problema ao tentar fazer o login. Tente novamente.'
        });
    });
});