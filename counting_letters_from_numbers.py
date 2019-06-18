"""
Contando as letras dos números

Este problema foi utilizado em 181 Dojo(s).

Se os números de 1 a 5 fossem escritos em palavras:
um, dois, três, quatro, cinco, então teríamos utilizado
2 + 4 + 4 + 6 + 5 = 21 letras no total.

Se todos os números de 1 até 1000 fossem escritos em palavras,
quantas letras nós teríamos utilizado?

"""

import unittest


def cardinal_str(num):
    cardinal = {}
    cardinal[1] = 'um'
    cardinal[2] = 'dois'
    cardinal[3] = 'três'
    cardinal[4] = 'quatro'
    cardinal[5] = 'cinco'
    cardinal[6] = 'seis'
    cardinal[7] = 'sete'
    cardinal[8] = 'oito'
    cardinal[9] = 'nove'
    cardinal[10] = 'dez'
    cardinal[11] = 'onze'
    cardinal[12] = 'doze'
    cardinal[13] = 'treze'
    cardinal[14] = 'catorze'
    cardinal[15] = 'quinze'
    cardinal[16] = 'dezesseis'
    cardinal[17] = 'dezessete'
    cardinal[18] = 'dezoito'
    cardinal[19] = 'dezenove'
    cardinal[20] = 'vinte'
    cardinal[30] = 'trinta'
    cardinal[40] = 'quarenta'
    cardinal[50] = 'cinquenta'
    cardinal[60] = 'sessenta'
    cardinal[70] = 'setenta'
    cardinal[80] = 'oitenta'
    cardinal[90] = 'noventa'
    cardinal[100] = 'cem'
    cardinal[200] = 'duzentos'
    cardinal[300] = 'trezentos'
    cardinal[400] = 'quatrocentos'
    cardinal[500] = 'quinhentos'
    cardinal[600] = 'seiscentos'
    cardinal[700] = 'setecentos'
    cardinal[800] = 'oitocentos'
    cardinal[900] = 'novecentos'
    cardinal[1000] = 'mil'

    numbers = split_number(num)
    card = ''
    for n in numbers:
        card += cardinal[n]

    return card


def split_number(num):
    # print(num)
    str_num = str(num)
    # print(str_num)
    numbers = []
    for i in range(len(str_num)):
        potencia = (len(str_num) - i - 1)
        digito = int(str_num[i])
        number = digito * (10 ** potencia)
        if number >= 20:
            numbers.append(number)
        elif number > 0:
            numbers.append(int(str_num[i:]))
            break

        # print(digito, potencia, i, digito * 10 ** potencia)

    return numbers


def count(num):
    soma = 0
    for i in range(1, num + 1):
        soma += len(cardinal_str(i))
    return soma


class CountLettersTest(unittest.TestCase):
    def test_count_1(self):
        self.assertEqual(count(1), 2)

    def test_count_2(self):
        self.assertEqual(count(2), 6)

    def test_count_3(self):
        self.assertEqual(count(3), 10)

    def test_count_5(self):
        self.assertEqual(count(5), 21)

    def test_count_20(self):
        self.assertEqual(count(20), 104)

    def test_count_21(self):
        self.assertEqual(count(21), 111)

    def test_count_22(self):
        self.assertEqual(count(22), 120)

    def test_split_21(self):
        self.assertEqual(split_number(21), [20, 1])

    def test_split_22(self):
        self.assertEqual(split_number(22), [20, 2])

    def test_split_37(self):
        self.assertEqual(split_number(37), [30, 7])

    def test_split_89(self):
        self.assertEqual(split_number(89), [80, 9])

    def test_split_103(self):
        self.assertEqual(split_number(103), [100, 3])

    def test_split_133(self):
        self.assertEqual(split_number(133), [100, 30, 3])

    def test_split_513(self):
        self.assertEqual(split_number(513), [500, 13])

    def test_split_1513(self):
        self.assertEqual(split_number(1513), [1000, 500, 13])


if __name__ == '__main__':
    # print(split_number(513))
    # print(cardinal_str(21))
    # print(cardinal_str(133))
    # print(cardinal_str(513))
    # print(cardinal_str(1513))
    # print(count(513))
    unittest.main()

