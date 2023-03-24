from Transacao import Transacao
from src.Dinheiro import Dinheiro
from ValorMonetario import ValorMonetario

class Saida(Transacao):

    def __init__(self, quantia : Dinheiro):
        self.__quantia = quantia
    #TODO
    # No construtor da Entrada a conta deveria ser passada como parâmetro
    # e a transação ficar com a referencia da conta

    def obter_valor_monetario(self):
        return self.__quantia.negativo()

    def contabilizar(self, saldo: ValorMonetario):
        return saldo.subtrair(self.__quantia)

