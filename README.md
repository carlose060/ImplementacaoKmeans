# ImplementacaoKmeans
Trabalho proposto na disciplina de TÓPICOS ESPECIAIS EM CIÊNCIA DA COMPUTAÇÃO - UFSJ 2022/2

Kmeans é um algoritmo de aprendizado não supervisionado (ou seja, que não precisa de inputs de confirmação externos) que avalia e clusteriza os dados de acordo com suas características, como por exemplo:
  lojas/centro logistico
  clientes/produtos ou serviços semelhantes
  clientes/características semelhantes
  séries/gênero da série ou faixa etaria
  usuarios de uma rede social/usuario influenciador
  paciente/sintoma ou característica semelhante
  
  Como funciona?
1.Primeiro, preciso definir um ‘K’, ou seja, um número de clusters (ou agrupamentos).\n
2.Depois, preciso definir, aleatoriamente, um centroide para cada cluster.
3.O próximo passo é calcular, para cada ponto, o centroide de menor distância. Cada ponto pertencerá ao centroide mais próximo (lembrar do exemplo do CD logístico e das lojas: cada loja (ponto) deve ser atendida pelo CD (centróide) mais próximo)
4.Agora, devo reposicionar o centróide. A nova posição do centroide deve ser a média da posição de todos os pontos do cluster.
5.Os dois ultimos passos são repetidos, iterativamente, até obtermos a posição ideal dos centróides.

O Algoritmo roda especificamente em cima da base de dados iris, e com parametro ja definido pela professora na proposta. Mas é facilmente generalizado.
