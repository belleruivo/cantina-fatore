const popup = document.getElementById('popup');
const overlay = document.getElementById('overlay');
const openPopupButton = document.querySelector('button.bg-orange-600');  // Garantir que está pegando o botão correto
const closePopupButton = document.getElementById('closePopup');

openPopupButton.addEventListener('click', () => {
    popup.classList.remove('hidden');
    overlay.classList.remove('hidden');
});

closePopupButton.addEventListener('click', () => {
    popup.classList.add('hidden');
    overlay.classList.add('hidden');
});

// Fechar o Popup ao clicar fora dele
overlay.addEventListener('click', () => {
    popup.classList.add('hidden');
    overlay.classList.add('hidden');
});

// Abertura do popup de edição
function abrirPopupEditar(id, nome, categoria, quantidade, preco, foto) {
    const popupEditar = document.getElementById('popup-editar');
    const overlay = document.getElementById('overlay');
    const form = document.getElementById('editar-form');

    // Preenche os campos do formulário com os valores recebidos
    document.getElementById('produto-id').value = id;
    document.getElementById('editar-nome').value = nome;
    document.getElementById('editar-categoria').value = categoria;
    document.getElementById('editar-quantidade').value = quantidade;
    document.getElementById('editar-preco').value = preco;

    // Atualiza a URL de envio do formulário
    form.action = `/produtos/editar/${id}`;

    // Exibe o popup e o overlay
    popupEditar.classList.remove('hidden');
    overlay.classList.remove('hidden');
}

// Fechamento do popup
document.getElementById('closePopupEditar').addEventListener('click', () => {
    document.getElementById('popup-editar').classList.add('hidden');
    document.getElementById('overlay').classList.add('hidden');
});

// Fechar o popup ao clicar fora dele
document.getElementById('overlay').addEventListener('click', () => {
    document.getElementById('popup-editar').classList.add('hidden');
    document.getElementById('overlay').classList.add('hidden');
});
