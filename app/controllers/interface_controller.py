from abc import ABC, abstractmethod

''' PRINCÍPIO DA SEGREGAÇÃO DE INTERFACE: cada método da interface é implementado em uma classe diferente.'''

''' PRINCÍPIO DA SUBSTITUIÇÃO DE LISKOV: nesse caso, ele é cumprido, pois a classe CadastroInterface pode ser substituída por qualquer outra classe que implemente o mesmo método.'''
class CadastroInterface(ABC): 
    @abstractmethod
    def cadastrar(self):
        pass

class AtualizacaoInterface(ABC):
    @abstractmethod
    def atualizar(self, id):
        pass

class RemocaoInterface(ABC):
    @abstractmethod
    def remover(self, id):
        pass

class ListagemInterface(ABC):
    @abstractmethod
    def listar(self):
        pass