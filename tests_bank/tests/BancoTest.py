import unittest

from src.Banco import Banco
from src.Moeda import Moeda


class MyTestCase(unittest.TestCase):

    # ================================ TEST BANCO ================================ #

    def test_create_banco(self):
        # INLINE FIXTURE SETUP
        banco_brasil = Banco("Banco do Brasil", Moeda.BRL)
        # EXERCISE SUT
        # RESULT VERIFICATION
        self.assertEqual("Banco do Brasil", banco_brasil.nome)
        self.assertEqual(Moeda.BRL, banco_brasil.moeda)
        # TEARDOWN

    def test_cria_dois_bancos_iguais_porem_diferentes(self):
        # INLINE FIXTURE SETUP
        banco_brasil1 = Banco("Banco do Brasil", Moeda.BRL)
        banco_brasil2 = Banco("Banco do Brasil", Moeda.BRL)
        # EXERCISE SUT
        # RESULT VERIFICATION
        self.assertNotEqual(banco_brasil1, banco_brasil2)
        # TEARDOWN

    # ================================ TEST AGENCIA ================================ #

    def test_cria_agencia(self):
        # INLINE FIXTURE SETUP
        banco_brasil = Banco("Banco do Brasil", Moeda.BRL)
        # EXERCISE SUT
        agencia_criciuma = banco_brasil.criar_agencia("Criciuma")
        # RESULT VERIFICATION
        self.assertEqual(agencia_criciuma.nome, "Criciuma")
        self.assertEqual(agencia_criciuma.banco, banco_brasil)
        # TEARDOWN

    def test_obter_identificador(self):
        # INLINE FIXTURE SETUP
        banco_brasil = Banco("Banco do Brasil", Moeda.BRL)
        # EXERCISE SUT
        agencia_criciuma = banco_brasil.criar_agencia("Criciuma")
        # RESULT VERIFICATION
        self.assertEqual(agencia_criciuma.nome, "Criciuma")
        self.assertEqual(agencia_criciuma.banco, banco_brasil)
        # TEARDOWN

    def test_cria_duas_agencias_iguais_porem_diferentes(self):
        # INLINE FIXTURE SETUP
        banco_brasil = Banco("Banco do Brasil", Moeda.BRL)
        # EXERCISE SUT
        agencia_criciuma1 = banco_brasil.criar_agencia("Criciuma")
        agencia_criciuma2 = banco_brasil.criar_agencia("Criciuma")
        # RESULT VERIFICATION
        self.assertNotEqual(agencia_criciuma1, agencia_criciuma2)
        # TEARDOWN

    # ================================ TEST CONTA ================================ #

    def test_cria_conta(self):
        # INLINE FIXTURE SETUP
        banco_brasil = Banco("Banco do Brasil", Moeda.BRL)
        agencia_criciuma = banco_brasil.criar_agencia("Criciuma")
        # EXERCISE SUT
        conta = agencia_criciuma.criar_conta("Davi Becker")
        # RESULT VERIFICATION
        self.assertEqual(conta.agencia, agencia_criciuma)
        self.assertEqual(conta.titular, "Davi Becker")
        # TEARDOWN

    def test_cria_duas_contas_iguais_porem_diferentes(self):
        # INLINE FIXTURE SETUP
        banco_brasil = Banco("Banco do Brasil", Moeda.BRL)
        agencia_criciuma = banco_brasil.criar_agencia("Criciuma")
        # EXERCISE SUT
        conta1 = agencia_criciuma.criar_conta("Davi Becker")
        conta2 = agencia_criciuma.criar_conta("Davi Becker")
        # RESULT VERIFICATION
        self.assertNotEqual(conta1, conta2)
        # TEARDOWN

    def test_adiciona_transação(self):
        banco_brasil = Banco("Banco do Brasil", Moeda.BRL)
        print("test")
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        # RESULT VERIFICATION
        # TEARDOWN

    def test_calcula_saldo_positivo(self):
        banco_brasil = Banco("Banco do Brasil", Moeda.BRL)
        print("test")
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        # RESULT VERIFICATION
        # TEARDOWN

    def test_calcula_saldo_negativo(self):
        banco_brasil = Banco("Banco do Brasil", Moeda.BRL)
        print("test")
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        # RESULT VERIFICATION
        # TEARDOWN



if __name__ == '__main__':
    unittest.main()
