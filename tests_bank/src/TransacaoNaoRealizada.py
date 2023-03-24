from Transacao import Transacao
from ValorMonetario import ValorMonetario

class TransacaoNaoRealizada(Transacao):

    def __init__(self, transacao : Transacao):
        self.__transacao = transacao

    def obter_valor_monetario(self):
        return self.__transacao.obter_valor_monetario()

    def contabilizar(self, saldo: ValorMonetario):
        return saldo

