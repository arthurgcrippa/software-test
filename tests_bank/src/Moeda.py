from enum import Enum


class Moeda(Enum):

    BRL = ("R$", 100)
    USD = ("$",  100)
    CHF = ("Fr", 100)

    def simbolo(self):
        return self.value[0]

    def base_fracionaria(self):
        return self.value[1]