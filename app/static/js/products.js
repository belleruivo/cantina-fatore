const popup = document.getElementById('popup');
const overlay = document.getElementById('overlay');
const openPopupButton = document.querySelector('button.bg-orange-600');  
const closePopupButton = document.getElementById('closePopup');

openPopupButton.addEventListener('click', () => {
    popup.classList.remove('hidden');
    overlay.classList.remove('hidden');
});

closePopupButton.addEventListener('click', () => {
    popup.classList.add('hidden');
    overlay.classList.add('hidden');
});

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

document.getElementById('overlay').addEventListener('click', () => {
    document.getElementById('popup-editar').classList.add('hidden');
    document.getElementById('overlay').classList.add('hidden');
});

document.addEventListener('DOMContentLoaded', () => {
   
    const modal = document.getElementById('modal-registrar-venda');
    const totalCarrinho = parseFloat(modal.dataset.totalCarrinho) || 0;
    const totalVenda = document.getElementById('total-venda');
    const dataVenda = document.getElementById('data-venda');

    // Atualiza os dados no modal
    function preencherModal() {
        totalVenda.textContent = `R$ ${totalCarrinho.toFixed(2)}`;
        dataVenda.value = new Date().toISOString().slice(0, 16);
    }

    // Abrir o modal ao clicar em "Prosseguir"
    const prosseguirCarrinho = document.getElementById('prosseguir-carrinho');
    prosseguirCarrinho.addEventListener('click', () => {
        preencherModal();
        modal.classList.remove('hidden');
    });

    // Salvar a venda
    const salvarVenda = document.getElementById('salvar-venda');
    salvarVenda.addEventListener('click', () => {
        // Captura os dados do formulário
        const compradorTipo = document.getElementById('comprador_tipo').value;
        const funcionarioId = compradorTipo === 'funcionario' ? document.getElementById('funcionario_id').value : null;

        const pagamentos = {
            dinheiro: parseFloat(document.getElementById('valor-dinheiro').value || 0),
            cartao: parseFloat(document.getElementById('valor-cartao').value || 0),
            pix: parseFloat(document.getElementById('valor-pix').value || 0),
        };

        const somaPagamentos = Object.values(pagamentos).reduce((acc, val) => acc + val, 0);

        if (somaPagamentos !== totalCarrinho) {
            alert('O valor total dos métodos de pagamento deve ser igual ao total do carrinho!');
            return;
        }

        // Prepara os dados para salvar no banco
        const venda = {
            comprador_tipo: compradorTipo,
            comprador_id: funcionarioId,
            metodo_pagamento: Object.entries(pagamentos)
                .filter(([_, valor]) => valor > 0)
                .map(([metodo, _]) => metodo)
                .join(','),
            total: totalCarrinho,
            data_venda: new Date().toISOString(),
            itens: carrinho, // Detalhes dos produtos no carrinho
        };

        console.log('Venda registrada:', venda); // Substitua com a chamada à API para salvar no banco.

        // Limpa o modal e o carrinho após salvar
        modal.classList.add('hidden'); // Fecha o modal
        alert('Venda registrada com sucesso!');
        // Aqui você pode limpar o carrinho no front e back-end
    });
});

document.getElementById('comprador_tipo').addEventListener('change', function() {
    var funcionarioSection = document.getElementById('funcionario-section');
    if (this.value === 'funcionario') {
        funcionarioSection.classList.remove('hidden');
    } else {
        funcionarioSection.classList.add('hidden');
    }
});

// Habilitar os campos de valor de pagamento quando a opção for selecionada
document.querySelectorAll('input[name="pagamento_metodo"]').forEach(function(input) {
    input.addEventListener('change', function() {
        var valorInput = document.getElementById('valor-' + this.value);
        if (this.checked) {
            valorInput.removeAttribute('disabled');
        } else {
            valorInput.setAttribute('disabled', 'disabled');
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.fixed.top-4.right-4');
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 300);
        }, 3000);
    });
});

function calcularTotalPagamentos() {
    const valorDinheiro = parseFloat(document.getElementById('valor-dinheiro').value) || 0;
    const valorCartao = parseFloat(document.getElementById('valor-cartao').value) || 0;
    const valorPix = parseFloat(document.getElementById('valor-pix').value) || 0;
    return valorDinheiro + valorCartao + valorPix;
}

function validarPagamentos() {
    const totalCarrinho = parseFloat(document.getElementById('modal-registrar-venda').dataset.totalCarrinho);
    const totalPagamentos = calcularTotalPagamentos();
    const btnSalvar = document.getElementById('salvar-venda');
    
    if (totalPagamentos > totalCarrinho) {
        mostrarMensagem(`O valor total dos pagamentos (R$ ${totalPagamentos.toFixed(2)}) não pode exceder o valor da compra (R$ ${totalCarrinho.toFixed(2)})`, 'error');
        btnSalvar.disabled = true;
        btnSalvar.classList.add('opacity-50');
        return false;
    } else if (totalPagamentos < totalCarrinho) {
        mostrarMensagem(`Ainda falta R$ ${(totalCarrinho - totalPagamentos).toFixed(2)} para completar o pagamento`, 'error');
        btnSalvar.disabled = true;
        btnSalvar.classList.add('opacity-50');
        return false;
    } else {
        btnSalvar.disabled = false;
        btnSalvar.classList.remove('opacity-50');
        return true;
    }
}

function mostrarMensagem(mensagem, tipo) {
    const mensagemDiv = document.createElement('div');
    mensagemDiv.className = `fixed top-4 right-4 z-50 p-4 rounded-md ${tipo === 'error' ? 'bg-red-500' : 'bg-green-500'} text-white`;
    mensagemDiv.textContent = mensagem;
    document.body.appendChild(mensagemDiv);
    
    setTimeout(() => {
        mensagemDiv.style.opacity = '0';
        setTimeout(() => mensagemDiv.remove(), 300);
    }, 3000);
}

// Adicione os event listeners para os campos de pagamento
document.querySelectorAll('#metodos-pagamento input[type="number"]').forEach(input => {
    input.addEventListener('input', validarPagamentos);
});

// Adicione o código para fechar o modal
document.getElementById('cancelar-venda').addEventListener('click', () => {
    document.getElementById('modal-registrar-venda').classList.add('hidden');
});

// Atualizar o event listener do botão salvar
document.getElementById('salvar-venda').addEventListener('click', (e) => {
    e.preventDefault();
    if (!validarPagamentos()) {
        return;
    }
    
    // ... resto do código de salvar venda ...
    
    // Após salvar, fechar o modal
    document.getElementById('modal-registrar-venda').classList.add('hidden');
});

// Atualizar o event listener do botão prosseguir
document.getElementById('prosseguir-carrinho').addEventListener('click', () => {
    const modal = document.getElementById('modal-registrar-venda');
    const totalCarrinho = parseFloat(modal.dataset.totalCarrinho);
    
    // Resetar os campos de pagamento
    document.querySelectorAll('#metodos-pagamento input[type="number"]').forEach(input => {
        input.value = '';
        input.disabled = true;
    });
    
    document.querySelectorAll('#metodos-pagamento input[type="checkbox"]').forEach(checkbox => {
        checkbox.checked = false;
    });
    
    // Atualizar o total no modal
    document.getElementById('total-venda').textContent = `R$ ${totalCarrinho.toFixed(2)}`;
    
    // Definir a data atual
    document.getElementById('data-venda').value = new Date().toISOString().slice(0, 16);
    
    // Mostrar o modal
    modal.classList.remove('hidden');
});

document.getElementById('salvar-venda').addEventListener('click', async (e) => {
    e.preventDefault();
    if (!validarPagamentos()) {
        return;
    }
    
    const compradorTipo = document.getElementById('comprador_tipo').value;
    const funcionarioId = compradorTipo === 'funcionario' ? 
        document.getElementById('funcionario_id').value : null;
    
    const dados = {
        comprador_tipo: compradorTipo,
        comprador_id: funcionarioId,
        valor_dinheiro: document.getElementById('valor-dinheiro').value || 0,
        valor_cartao: document.getElementById('valor-cartao').value || 0,
        valor_pix: document.getElementById('valor-pix').value || 0
    };
    
    try {
        const response = await fetch('/registrar-venda', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados)
        });
        
        const result = await response.json();
        
        if (result.success) {
            mostrarMensagem(result.message, 'success');
            document.getElementById('modal-registrar-venda').classList.add('hidden');
            // Recarregar a página para atualizar o carrinho
            setTimeout(() => window.location.reload(), 1500);
        } else {
            mostrarMensagem(result.message, 'error');
        }
    } catch (error) {
        mostrarMensagem('Erro ao processar a venda', 'error');
    }
});