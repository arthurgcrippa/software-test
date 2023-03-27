from src.Moeda import Moeda
from src.Dinheiro import Dinheiro
from src.ValorMonetario import ValorMonetario
from src.Banco import Banco
from src.Conta import Conta
from src.Entrada import Entrada
from src.Saida import Saida
from src.EstadosDeOperacao import EstadosDeOperacao
from src.TransacaoNaoRealizada import TransacaoNaoRealizada
from src.Operacao import Operacao

class SistemaBancario:

	def __init__(self):
		self.__bancos = []

	def criar_banco(self, nome, moeda : Moeda):
		banco = Banco(nome, moeda)
		self.__bancos.append(banco)
		return banco

	def moeda_invalida(self, conta : Conta, quantia : Dinheiro):
		moeda_do_banco = conta.agencia.banco.moeda
		moeda_da_operacao = quantia.moeda
		return moeda_do_banco != moeda_da_operacao

	def depositar(self, conta : Conta, quantia : Dinheiro):
		entrada = Entrada(quantia)
		estado = EstadosDeOperacao.SUCESSO
		if self.moeda_invalida(conta, quantia):
			entrada = TransacaoNaoRealizada(entrada)
			estado = EstadosDeOperacao.MOEDA_INVALIDA
		conta.adicionar_transacao(entrada)
		return Operacao(estado)

	def saldo_ficara_negativo(self, saldo : ValorMonetario, quantia : Dinheiro):
		return saldo.obter_quantia().obter_quantia_em_escala() < quantia.obter_quantia_em_escala()

	def sacar(self, conta : Conta, quantia : Dinheiro):
		saldo = conta.calcular_saldo()
		saida = Saida(quantia)
		estado = EstadosDeOperacao.SUCESSO
		if (saldo.negativo() or self.saldo_ficara_negativo(saldo, quantia)):
			saida = TransacaoNaoRealizada(saida)
			estado = EstadosDeOperacao.SALDO_INSUFICIENTE
		if self.moeda_invalida(conta, quantia):
			saida = TransacaoNaoRealizada(saida)
			estado = EstadosDeOperacao.MOEDA_INVALIDA
		conta.adicionar_transacao(saida)
		return Operacao(estado)

	def transferir(self, origem : Conta, destino : Conta, quantia : Dinheiro):
		saida = Saida(quantia)
		entrada = Entrada(quantia)
		estado = EstadosDeOperacao.SUCESSO
		if (self.moeda_invalida(origem, quantia) or self.moeda_invalida(destino, quantia)):
			saida = TransacaoNaoRealizada(saida)
			entrada = TransacaoNaoRealizada(entrada)
			estado = EstadosDeOperacao.MOEDA_INVALIDA
		origem.adicionar_transacao(saida)
		destino.adicionar_transacao(entrada)
		return Operacao(estado, saida, entrada)

	def obter_bancos(self):
		return self.__bancos
