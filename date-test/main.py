import datetime
from datetime import date
import unittest

class TestDateTime(unittest.TestCase):

    ##################################### Teste de Datas ####################################
    def test_cria_data_natal_2017(self):
        # Fixture Setup
        # Exercise SUT
        natal_2017 = datetime.date(2017, 12, 25)
        # Result Verification
        self.assertEqual(2017, natal_2017.year)
        self.assertEqual(12, natal_2017.month)
        self.assertEqual(25, natal_2017.day)
        # Fixture Teardown

    def test_cria_data_dia_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            data_invalida = datetime.date(2017, 1, -1)
        # Result Verification
        # Fixture Teardown
    
    def test_cria_data_dia_valido(self):
        # Fixture Setup
        # Exercise SUT
        datetime.date(2017, 1, 11)
        # Result Verification
        # Fixture Teardown

    def test_cria_data_de_ano_bissexto_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            dia_29_fevereiro = datetime.date(2018, 2, 29)
        # Result Verification
        # Fixture Teardown
    
    def test_cria_data_de_ano_bissexto_valido(self):
        # Fixture Setup
        # Exercise SUT
        dia_29_fevereiro = datetime.date(2020, 2, 29)
        # Result Verification
        self.assertEqual(0, (dia_29_fevereiro.year%4))
        self.assertEqual(2, (dia_29_fevereiro.month))
        self.assertEqual(29, (dia_29_fevereiro.day))
        # Fixture Teardown
    
    def test_datas_diferentes(self):
        # Fixture Setup
        # Exercise SUT
        data_1 = datetime.date(2017, 3, 21)
        data_2 = datetime.date(2017, 10, 3)
        # Result Verification
        self.assertNotEqual(data_1, data_2)
        # Fixture Teardown

    def test_datas_iguais(self):
        # Fixture Setup
        # Exercise SUT
        data_1 = datetime.date(2017, 3, 21)
        data_2 = datetime.date(2017, 3, 21)
        # Result Verification
        self.assertEqual(data_1, data_2)
        # Fixture Teardown

    def test_dia_primeiro_janeiro(self):
        # Fixture Setup
        # Exercise SUT
        primeiro_janeiro = datetime.date(2000, 1, 1)
        self.assertEqual(1, primeiro_janeiro.month)
        self.assertEqual(1, primeiro_janeiro.day)
        # Result Verification
        # Fixture Teardown

    def test_data_menor_que_maior_data(self):
        # Fixture Setup
        # Exercise SUT
        data_alearotia = datetime.date(2000,2,28)
        # Result Verification
        self.assertGreater(datetime.MAXYEAR, data_alearotia.year)
        # Fixture Teardown

    def test_data_maior_que_menor_data(self):
        # Fixture Setup
        # Exercise SUT
        data_alearotia = datetime.date(2000,2,28)
        # Result Verification
        self.assertGreater(data_alearotia.year, datetime.MINYEAR)
        # Fixture Teardown

    def test_dia_do_stars_wars(self):
        # Fixture Setup
        # Exercise SUT
        data_alearotia = datetime.date(2000,5,4)
        # Result Verification
        self.assertEqual(5, data_alearotia.month)
        self.assertEqual(4, data_alearotia.day)
        # Fixture Teardown
    
    def test_dia_31_mes_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2022, 4, 31)
        # Result Verifications
        # Fixture Teardown

    def test_dia_zero(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2022, 4, 0)
        # Result Verifications
        # Fixture Teardown

    def test_dia_maior_31(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2022, 4, 32)
        # Result Verifications
        # Fixture Teardown

    def test_mes_zero(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2022, 0, 1)
        # Result Verifications
        # Fixture Teardown

    def test_mes_maior_12(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2022, 13, 1)
        # Result Verifications
        # Fixture Teardown

    def test_mes_menor_zero(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2022, -1, 1)
        # Result Verifications
        # Fixture Teardown

    # #################################### Teste de Horas ####################################
    def test_hora_valida(self):
        # Fixture Setup
        # Exercise SUT
        datetime.time(23, 59, 59, 1000)
        # Result Verification
        # Fixture Teardown
    
    def test_hora_invalida(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            meia_noite = datetime.time(25, 59, 59)
        # Result Verification
        # Fixture Teardown

    def test_minuto_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            meia_noite = datetime.time(25, 60, 59)
        # Result Verification
        # Fixture Teardown

    def test_segundo_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            meia_noite = datetime.time(25, 59, 61)
        # Result Verification
        # Fixture Teardown

    def test_microsegundo_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            meia_noite = datetime.time(25, 59, 61, -1000)
        # Result Verification
        # Fixture Teardown

    def test_meio_dia(self):
        # Fixture Setup
        # Exercise SUT
        meio_dia = datetime.time(12, 0, 0, 1000)
        # Result Verification
        self.assertEqual(12, meio_dia.hour)
        # Fixture Teardown

    def test_meia_noite(self):
        # Fixture Setup
        # Exercise SUT
        datetime.time(0, 0, 0)
        # Result Verification
        # Fixture Teardown

    def test_am(self):
        # Fixture Setup
        # Exercise SUT
        meio_dia = datetime.time(12, 0, 0, 1000)
        # Result Verification
        self.assertLessEqual(12, meio_dia.hour)
        self.assertLessEqual(0, meio_dia.minute)
        self.assertLessEqual(0, meio_dia.second)
        # Fixture Teardown

    def test_pm(self):
        # Fixture Setup
        # Exercise SUT
        meio_dia = datetime.time(12, 0, 0, 1000)
        # Result Verification
        self.assertGreaterEqual(12, meio_dia.hour)
        self.assertGreaterEqual(0, meio_dia.minute)
        self.assertGreaterEqual(0, meio_dia.second)
        # Fixture Teardown

    # #################################### Teste de Timedelta ####################################
    def test_cria_deltatime(self):
        # Fixture Setup
        # Exercise SUT
        delta_time = datetime.timedelta(days=50,seconds=27, microseconds=10,milliseconds=29000, minutes=5,hours=8, weeks=2)
        # Result Verification
        # Fixture Teardown

    def test_maximo_deltatime(self):
        # Fixture Setup
        # Exercise SUT
        datetime.timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)
        # Result Verification
        # Fixture Teardown

    def test_minimo_deltatime(self):
        # Fixture Setup
        # Exercise SUT
        datetime.timedelta(-999999999)
        # Result Verification
        # Fixture Teardown

    def test_minus_deltatime(self):
        # Fixture Setup
        max = datetime.timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)
        delta_time = datetime.timedelta(days=50,seconds=27, microseconds=10,milliseconds=29000, minutes=5,hours=8, weeks=2)
        # Exercise SUT
        t1 = max - delta_time
        # Result Verification
        self.assertEqual((max-t1), delta_time)
        # Fixture Teardown

if __name__ == "__main__":
    unittest.main()

