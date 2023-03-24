from abc import ABC
from src.ValorMonetario import ValorMonetario

class Transacao(ABC):

    def obter_valor_monetario(self):
        pass

    def contabilizar(self, saldo : ValorMonetario):
        pass


