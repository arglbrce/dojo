"""

Matriz Espiral
Contribuição de: Eduardo Oliveira de Carvalho

Este problema foi utilizado em 223 Dojo(s).

Dado um número de colunas e um número de linhas, retornar uma matriz em espiral de fora para dentro no sentido horário.

Variação do problema: retorne a espiral no sentido anti-horário.

Este problema é mais fácil de ser compreendido através de exemplos:

Entrada: 2 2

Saída:

 1  2
 4  3

Entrada: 3 4

Saída:

 1  2 3
10 11 4
 9 12 5
 8  7 6

Entrada: 5 6

Saída:

 1  2  3  4  5
18 19 20 21  6
17 28 29 22  7
16 27 30 23  8
15 26 25 24  9
14 13 12 11 10


"""

import unittest

def matrix(row, col):
    numbers = []
    for num in range(1,row*col+1):
        numbers.append(num)

    if row == 1:
        return [numbers]
    elif row == 1:
        return [numbers]
    elif row == 2:
        idx = (row * col + 1) // 2
        return [numbers[:idx],sorted(numbers[idx:], reverse=True)]
    elif row == 3:
        l1 = slice(col)
        res = []
        i = row
        j = col
        start, stop  = 0, col
        for i in range(1, 2 * row):
            s = slice(start, stop)
            res.append(numbers[s])
            start += stop
            stop = start + stop - 1

        #for r in range(row):
            #res.append(numbers[(r*col):(col*(r+1))])
        return res

class MatrizEspiralTest(unittest.TestCase):
    def test_matrix_1_1(self):
        self.assertEqual(matrix(1,1),[[1]])

    def test_matrix_1_2(self):
        self.assertEqual(matrix(1,2),[[1,2]])

    def test_matrix_2_2(self):
        self.assertEqual(matrix(2,2),[[1,2],[4,3]])

    def test_matrix_2_3(self):
        self.assertEqual(matrix(2,3),[[1,2,3],[6,5,4]])

    def test_matrix_3_3(self):
        #self.assertEqual(matrix(3,3),[[1,2,3],[8,9,4], [7,6,5]])
        self.assertEqual(matrix(3,3),[[1,2,3], [4,5], [6,7], [8], [9]])


if __name__ == "__main__":
    unittest.main()