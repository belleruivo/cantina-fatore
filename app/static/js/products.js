const popup = document.getElementById('popup');
const overlay = document.getElementById('overlay');
const openPopupButton = document.querySelector('.bg-orange-500');
const closePopupButton = document.getElementById('closePopup');

openPopupButton.addEventListener('click', () => {
    popup.classList.remove('hidden');
    overlay.classList.remove('hidden');
});

closePopupButton.addEventListener('click', () => {
    popup.classList.add('hidden');
    overlay.classList.add('hidden');
});

// fechar o Popup ao clicar fora dele
overlay.addEventListener('click', () => {
    popup.classList.add('hidden');
    overlay.classList.add('hidden');
});


function abrirPopupEditar(id, nome, categoria, quantidade, preco, foto) {
const popupEditar = document.getElementById('popup-editar');
const overlay = document.getElementById('overlay');
const form = document.getElementById('editar-form');

document.getElementById('produto-id').value = id;
document.getElementById('editar-nome').value = nome;
document.getElementById('editar-categoria').value = categoria;
document.getElementById('editar-quantidade').value = quantidade;
document.getElementById('editar-preco').value = preco;

form.action = `/produtos/editar/${id}`;

popupEditar.classList.remove('hidden');
overlay.classList.remove('hidden');
}

document.getElementById('closePopupEditar').addEventListener('click', () => {
document.getElementById('popup-editar').classList.add('hidden');
document.getElementById('overlay').classList.add('hidden');
});
