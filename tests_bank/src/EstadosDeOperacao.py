from enum import Enum


class EstadosDeOperacao(Enum):
    SUCESSO = 1
    SALDO_INSUFICIENTE = 2
    MOEDA_INVALIDA = 3
