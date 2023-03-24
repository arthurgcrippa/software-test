import unittest

from src.Dinheiro import Dinheiro
from src.Moeda import Moeda


class MyTestCase(unittest.TestCase):

    # ================================ TEST DINHEIRO ================================ #

    def test_negativo_de_dez_reais_cinquenta_centavos(self):
        # INLINE FIXTURE SETUP
        dez_reais_cinquenta_centavos = Dinheiro(Moeda.BRL, 10, 50)
        # EXERCISE SUT
        negativo = dez_reais_cinquenta_centavos.negativo()  # retorna um valor monetario
        # RESULT VERIFICATION
        self.assertTrue(negativo.negativo())
        self.assertEqual(1050, int(negativo.obter_quantia().obter_quantia_em_escala()))
        # TEARDOWN

    def test_positivo_de_dez_reais_cinquenta_centavos(self):
        # INLINE FIXTURE SETUP
        dez_reais_cinquenta_centavos = Dinheiro(Moeda.BRL, 10, 50)
        # EXERCISE SUT
        positivo = dez_reais_cinquenta_centavos.positivo()  # retorna um valor monetario
        # RESULT VERIFICATION
        self.assertEqual(1050, int(positivo.obter_quantia().obter_quantia_em_escala()))
        # TEARDOWN

    def test_zero_reais(self):
        # INLINE FIXTURE SETUP
        zero_reais = Dinheiro(Moeda.BRL, 0, 0)
        # EXERCISE SUT
        # RESULT VERIFICATION
        self.assertEqual(0, zero_reais.obter_quantia_em_escala())
        # TEARDOWN

    def test_tipo_da_moeda_brl(self):
        # INLINE FIXTURE SETUP
        dez_reais_cinquenta_centavos = Dinheiro(Moeda.BRL, 10, 50)
        # EXERCISE SUT
        # RESULT VERIFICATION
        self.assertEqual(Moeda.BRL, dez_reais_cinquenta_centavos.moeda)
        # TEARDOWN

    def test_tipo_da_moeda_usd(self):
        # INLINE FIXTURE SETUP
        dez_reais_cinquenta_centavos = Dinheiro(Moeda.USD, 10, 50)
        # EXERCISE SUT
        # RESULT VERIFICATION
        self.assertEqual(Moeda.USD, dez_reais_cinquenta_centavos.moeda)
        # TEARDOWN

    def test_tipo_da_moeda_chf(self):
        # INLINE FIXTURE SETUP
        dez_reais_cinquenta_centavos = Dinheiro(Moeda.CHF, 10, 50)
        # EXERCISE SUT
        # RESULT VERIFICATION
        self.assertEqual(Moeda.CHF, dez_reais_cinquenta_centavos.moeda)
        # TEARDOWN

    def test_verificar_inteiro(self):
        # INLINE FIXTURE SETUP
        dez_reais_cinquenta_centavos = Dinheiro(Moeda.CHF, 10, 50)
        # EXERCISE SUT
        # RESULT VERIFICATION
        self.assertEqual(10, dez_reais_cinquenta_centavos.inteiro)
        # TEARDOWN

    def test_verificar_fracionado(self):
        # INLINE FIXTURE SETUP
        dez_reais_cinquenta_centavos = Dinheiro(Moeda.CHF, 10, 50)
        # EXERCISE SUT
        # RESULT VERIFICATION
        self.assertEqual(50, dez_reais_cinquenta_centavos.fracionado)
        # TEARDOWN


if __name__ == '__main__':
    unittest.main()
