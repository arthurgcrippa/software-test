import unittest

from src.SistemaBancario import SistemaBancario
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
class MyTestCase(unittest.TestCase):
    def test_sacar(self):
        sistema_bancario = SistemaBancario()
        conta = HelperTest.create_new_account(self)
        dinheiro = Dinheiro(Moeda.BRL, 10, 50)

        test = sistema_bancario.sacar(conta, dinheiro)
        self.assertEqual(test.obter_estado(), EstadosDeOperacao.SALDO_INSUFICIENTE)

    def test_depositar(self):
        sistema_bancario = SistemaBancario()
        conta = HelperTest.create_new_account(self)
        dinheiro = Dinheiro(Moeda.BRL, 10, 50)

        test = sistema_bancario.depositar(conta, dinheiro)
        self.assertEqual(test.obter_estado(), EstadosDeOperacao.SUCESSO)

    def test_depositar_moeda_diferente(self):
        sistema_bancario = SistemaBancario()
        conta = HelperTest.create_new_account(self)
        dinheiro = Dinheiro(Moeda.CHF, 10, 50)

        test = sistema_bancario.depositar(conta, dinheiro)
        self.assertEqual(test.obter_estado(), EstadosDeOperacao.MOEDA_INVALIDA)
class HelperTest():
    def create_new_account(self):
        sistema_bancario = SistemaBancario()
        banco_brasil = sistema_bancario.criar_banco("Banco do Brasil", Moeda.BRL)
        agencia_criciuma = banco_brasil.criar_agencia("Criciuma")
        return agencia_criciuma.criar_conta("Davi Becker")



if __name__ == '__main__':
    unittest.main()
