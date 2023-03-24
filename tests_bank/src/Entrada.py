from Transacao import Transacao
from Dinheiro import Dinheiro
from ValorMonetario import ValorMonetario

class Entrada(Transacao):

    def __init__(self, quantia : Dinheiro):
        self.__quantia = quantia
    #TODO
    # No construtor da Entrada a conta deveria ser passada como parâmetro
    # e a transação ficar com a referencia da conta

    def obter_valor_monetario(self):
        return self.__quantia.positivo()

    def contabilizar(self, saldo : ValorMonetario):
        return saldo.somar(self.__quantia)
