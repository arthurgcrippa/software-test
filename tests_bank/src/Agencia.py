from src.Conta import Conta

class Agencia:

	def __init__(self, nome, codigo, banco):
		self.__nome = nome
		self.__codigo = codigo
		self.__banco = banco
		self.__contas = []

	@property
	def	nome(self):
		return self.__nome

	@property
	def banco(self):
		return self.__banco

	def obter_identificador(self):
		return '{0:03d}'.format(self.__codigo)

	def criar_conta(self, titular):
		conta = Conta(titular, len(self.__contas) + 1, self)
		self.__contas.append(conta)
		return conta
