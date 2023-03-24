from src.Moeda import Moeda
from src.Agencia import Agencia

class Banco:

    def __init__(self, nome, moeda : Moeda):
        self.__nome = nome
        self.__moeda = moeda
        self.__agencias = []

    @property
    def nome(self):
        return self.__nome

    @property
    def moeda(self):
        return self.__moeda

    def criar_agencia(self, nome):
        agencia = Agencia(nome, len(self.__agencias)+1, self)
        self.__agencias.append(agencia)
        return agencia
