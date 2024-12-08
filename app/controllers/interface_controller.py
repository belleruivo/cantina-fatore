from abc import ABC, abstractmethod

class CadastroInterface(ABC): #Segregação de interface**
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

''' Principio da substituição de Liskov: assegura que qualquer 
implementação dessas interfaces possa ser substituída sem alterar o comportamento esperado'''