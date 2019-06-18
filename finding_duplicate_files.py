"""

Encontrando arquivos duplicados

Este problema foi utilizado em 91 Dojo(s).

Quando fazemos o backup de arquivos, como imagens, músicas ou vídeos, um problema comum é saber se um determinado arquivo já foi armazenado ou não. A solução mais simples é fazer o backup de tudo. Isto é válido se você tem um espaço infinito para armazenar o seu backup. Não é uma solução tão boa se você possui um espaço limitado, dado que você pode acabar com a mesma foto da última viagem de férias em 5 locais diferentes dentro do seu backup.

Uma solução para essa duplicação excessiva de arquivos, é encontrar as duplicatas, e apagá-las. É claro que eu preciso confiar no software que faça esse procedimento, pois qualquer falha nele pode provocar a perda definitiva de algum dos meus arquivos.

Escreva um algoritmo para encontrar arquivos duplicados utilizando TDD.

Para fazer isso, pense:

    O que significa que um arquivo é idêntico ao outro? Nome, tamanho, conteúdo, data de criação?
    Como você vai fornecer a entrada para o algoritmo? Você deveria usar algum mock para o sistema de arquivos?
    Qual a saída do algoritmo? Uma lista de arquivos? Alguma outra coisa?

Você pode começar aos poucos, tratando somente arquivos tipo texto por exemplo

Adaptado de http://sites.google.com/site/tddproblems/all-problems-1/finding-duplicate-files

"""