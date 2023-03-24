from src import ValorMonetario

class Dinheiro:

    def __init__(self, moeda, inteiro, fracionado):
        self.__moeda = moeda
        self.__inteiro = inteiro
        self.__fracionado = fracionado
        self.__normalizar()

    @property
    def moeda(self):
        return self.__moeda

    @property
    def inteiro(self):
        return self.__inteiro

    @property
    def fracionado(self):
        return self.__fracionado

    def __normalizar(self):
        soma = self.obter_quantia_em_escala()
        base_fracionaria = self.moeda.base_fracionaria()
        self.__inteiro = (soma - soma % base_fracionaria) / base_fracionaria
        self.__fracionado = soma % base_fracionaria

    def obter_quantia_em_escala(self):
        return abs(self.__inteiro) * self.__moeda.base_fracionaria() + abs(self.__fracionado)

    def zero(self):
        return self.inteiro == 0 and self.fracionado == 0

    def formatar_sem_moeda(self):
        return '{0},{1:02d}'.format(int(self.inteiro), int(self.fracionado))

    def formatar_com_moeda(self):
        return '{0},{1:02d} {2}'.format(int(self.inteiro), int(self.fracionado), self.moeda.name)

    def formatado(self):
        if self.zero():
            return self.formatar_sem_moeda()
        else:
            return self.formatar_com_moeda()

    def positivo(self):
        return ValorMonetario.ValorMonetario(self.moeda).somar(self)

    def negativo(self):
        return ValorMonetario.ValorMonetario(self.moeda).subtrair(self)

    def __eq__(self, other):
        if isinstance(other, Dinheiro):
            mesma_moeda = self.moeda == other.moeda
            mesmo_valor = (self.inteiro == other.inteiro) and (self.fracionado == other.fracionado)
            return self.zero() or (mesmo_valor and mesma_moeda)
        return super == other

    def __str__(self):
        return self.formatado()

