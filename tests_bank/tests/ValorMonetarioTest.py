import unittest

from src.ValorMonetario import ValorMonetario
from src.Moeda import Moeda
from src.Dinheiro import Dinheiro

class MyTestCase(unittest.TestCase):

    # Create
    valor_monetario = ValorMonetario(Moeda.BRL, 10)
    def setUp(self):
        # Sei que não faz sentido criar um setup com apenas 1 linha, mas foi mais para entender como funcionava
        # Acho que valeu
        self.valor_monetario =  ValorMonetario(Moeda.BRL, 1000)

    def test_criar_valor_monetario(self):
        # INLINE FIXTURE SETUP
        self.setUp()
        # EXERCISE SUT
        # RESULT VERIFICATION
        self.assertEqual(self.valor_monetario.obter_quantia(), Dinheiro(Moeda.BRL, 0, 1000))
        # TEARDOWN

    def test_somar_moedas_iguais(self):
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        valor_atualizado = self.valor_monetario.somar(Dinheiro(Moeda.BRL, 0, 1000))
        # RESULT VERIFICATION
        self.assertEqual(valor_atualizado, Dinheiro(Moeda.BRL, 0, 2000))
        # TEARDOWN

    def test_somar_moedas_diferentes(self):
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        # RESULT VERIFICATION
        with self.assertRaises(Exception):
            self.valor_monetario.somar(Dinheiro(Moeda.CHF, 0, 1000))
        # TEARDOWN


if __name__ == '__main__':
    unittest.main()
