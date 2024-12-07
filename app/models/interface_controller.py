from abc import ABC, abstractmethod

class CRUDInterface(ABC):
    
    @abstractmethod
    def salvar(self):
        pass
    
    @abstractmethod
    def excluir(self):
        pass
    
    @abstractmethod
    def atualizar(self):
        pass 
