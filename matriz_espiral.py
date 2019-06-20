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
    matriz_espiral = [[0 for x in range(col)] for y in range(row)] 
    valor = 1
    if row == 1:
        matriz_espiral = [list(range(1, col + 1))]
    
    elif row == col:
        start, stop  = 0, col
        
        while valor <= row * col:
            # percorre da esquerda para direita
            for i in range(start, stop):
                matriz_espiral[start][i] = valor
                valor += 1

            # percorre de cima para baixo
            for i in range(start + 1, stop):
                matriz_espiral[i][stop-1] = valor
                valor += 1

            # percorre da direita para esquerda
            for i in range(stop-2, start-1, -1):
                matriz_espiral[stop-1][i] = valor
                valor += 1

            # percorre de baixo para cima
            for i in range(stop-2, start, -1):
                matriz_espiral[i][start] = valor
                valor += 1
            
            start += 1
            stop -= 1
    elif row < col:
        start_row, stop_row  = 0, col
        start_col, stop_col  = 0, row
        
        while True:
            # percorre da esquerda para direita
            for i in range(start_row, stop_row):
                matriz_espiral[start_row][i] = valor
                valor += 1
            #print('esquerda para direita', matriz_espiral)
            if valor > row * col:
                break

            # percorre de cima para baixo
            for i in range(start_col + 1, stop_col):
                matriz_espiral[i][stop_col] = valor
                valor += 1
            #print('cima para baixo', matriz_espiral)
            if valor > row * col:
                break

            # percorre da direita para esquerda
            for i in range(stop_row-2, start_row-1, -1):
                matriz_espiral[stop_row-2][i] = valor
                valor += 1
            #print('direita para esquerda', matriz_espiral)
            if valor > row * col:
                break

            # percorre de baixo para cima
            for i in range(stop_col-2, start_col, -1):
                matriz_espiral[i][start_col] = valor
                valor += 1
            #print('baixo para cima', matriz_espiral)
            if valor > row * col:
                break

            start_col += 1
            stop_col -= 1
            start_row += 1
            stop_row -= 1
        
    return matriz_espiral
        

class MatrizEspiralTest(unittest.TestCase):
    def test_matrix_1_1(self):
        self.assertEqual(matrix(1,1),[[1]])

    def test_matrix_1_2(self):
        self.assertEqual(matrix(1,2),[[1,2]])

    def test_matrix_2_2(self):
        self.assertEqual(matrix(2,2),[[1,2],[4,3]])

    def test_matrix_3_3(self):
        self.assertEqual(matrix(3,3),[[1,2,3],[8,9,4], [7,6,5]])

    def test_matrix_4_4(self):
        self.assertEqual(matrix(4,4),[[1,2,3,4],[12,13,14,5], [11,16,15,6],[10,9,8,7]])

    def test_matrix_2_3(self):
        self.assertEqual(matrix(2,3),[[1,2,3],[6,5,4]])

    def test_matrix_3_4(self):
        self.assertEqual(matrix(3,4),[[1,2,3,4],[10,11,12,5], [9,8,7,6]])
    
if __name__ == "__main__":
    unittest.main()