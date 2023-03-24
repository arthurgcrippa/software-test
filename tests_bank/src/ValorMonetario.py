from src import Dinheiro


class ValorMonetario:

    def __init__(self, moeda, valor = 0):
        self.__moeda = moeda
        self.__sinal = 1 if valor >= 0 else -1
        self.__quantia = Dinheiro.Dinheiro(moeda, 0, valor)

    def validar_moeda(self, quantia_somada):
        if self.__moeda != quantia_somada.moeda:
            raise Exception("moedas incompativeis")

    def somar(self, quantia_somada):
        self.validar_moeda(quantia_somada)
        valor = self.__quantia.obter_quantia_em_escala() * self.__sinal + quantia_somada.obter_quantia_em_escala()
        return ValorMonetario(self.__moeda, valor)

    def subtrair(self, quantia_subtraida):
        self.validar_moeda(quantia_subtraida)
        valor = self.__quantia.obter_quantia_em_escala() * self.__sinal - quantia_subtraida.obter_quantia_em_escala()
        return ValorMonetario(self.__moeda, valor)

    def obter_quantia(self):
        return self.__quantia

    def negativo(self):
        return self.__sinal < 0

    def zero(self):
        return self.__quantia.obter_quantia_em_escala() == 0

    def formatado(self):
        if self.zero():
            return self.formatar_sem_sinal()
        else:
            return self.formatar_com_sinal()

    def formatar_sem_sinal(self):
        return self.__quantia.formatado()

    def formatar_com_sinal(self):
        if (self.negativo()):
            return self.formatar_negativo()
        else:
            return self.formatar_positivo()

    def formatar_positivo(self):
        return "+" + self.__quantia.formatado()

    def formatar_negativo(self):
        return "-" + self.__quantia.formatado()

    def __eq__(self, other):
        if isinstance(other, ValorMonetario):
            iguais_zero = self.zero() and other.zero()
            iguais_com_mesma_moeda = self.__sinal.__eq__(other.__sinal) and \
                                     self.__quantia.__eq__(other.__quantia) and \
                                     self.__moeda.__eq__(other.__moeda)
            return iguais_zero and iguais_com_mesma_moeda
        return super == other

    def __str__(self):
        return self.formatado()


