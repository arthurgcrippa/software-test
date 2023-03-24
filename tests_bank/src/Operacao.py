from src.EstadosDeOperacao import EstadosDeOperacao

class Operacao:

    def __init__(self, estado : EstadosDeOperacao):
        self.__estado = estado
    #TODO
    # No construtor da Operacao estava sendo passado uma lista de transacoes.
    # Mas nada era feito com essa lista de transacoes...

    def obter_estado(self):
        return self.__estado
