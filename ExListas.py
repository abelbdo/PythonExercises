# ex1
# numeros = []
# for i in range(0,5):
#    numeros.append(int(input("Informe um número: ")))

# print(numeros)

# ex2
# numeros = []
# for i in range(0,10):
#    numeros.append(int(input("Informe um número: ")))

# numeros.reverse()
# print(numeros)

# ex3
# notas = []
# for i in range(0, 4):
#    notas.append(float(input('Informe uma nota: ')))

# soma = 0.0
# print('\n Notas informadas:')
# for i in range(0, 4):
#    print('Nota %d: %.2f' % (i, notas[i]))
#    soma += notas[i]

# print('Media das notas: %.2f' % (soma / 4.0))

# ex4
# letras = []
# vogais = ['A', 'E', 'I', 'O', 'U']

# for i in range(0, 10):
#    letras.append(input('Digite uma palavra: ').upper())

# qntConsoantes = 0
# consoantes = []
# for i in range(0, 10):
#    if letras[i] not in vogais:
#        consoantes.append(letras[i])
#       qntConsoantes += 1

# print('Voce digitou %d consoantes' % qntConsoantes)
# print(consoantes)

# ex05
# numeros = []
# par = []
# impar = []

# for i in range(0, 20):
#   numero = int(input('Informe um numero: '))
#  numeros.append(numero)
# if (numero % 2 == 0):
#    par.append(numero)
# else:
#   impar.append(numero)

# print(numeros)
# print(par)
# print(impar)

# ex06
# notas = []
# for i in range(0, 10):
#   notasAluno = []
#  for j in range(0, 4):
#     notasAluno.append(float(input('Informe a nota %.d: ' % (i + 1))))
# notas.append(notasAluno)

# alunosMedia = 0
# for notasAluno in notas:
#   somaNotas = 0
#  for nota in notasAluno:
#     somaNotas += nota
# if ((somaNotas / 4.0) >= 7.0):
#   alunosMedia += 1

# print('%d alunos ficaram acima da media' % alunosMedia)

# ex07
# numeros = []
# for i in range(0, 4):
#   numeros.append(int(input('Informe um numero inteiro: ')))

# soma = 0
# multiplicacao = 1
# for i in numeros:
#   soma += i
#  multiplicacao *= i

# print(numeros)
# print('Soma dos numeros: %d' % soma)
# print('Multiplicacao dos numeros: %d' % multiplicacao)

# ex08
# pessoas = []
# for i in range(0, 5):
#    pessoa = []
#    pessoa.append(input('Informe a idade da pessoa: '))
#   pessoa.append(input('Informe a altura da pessoa: '))
#  pessoas.append(pessoa)

# pessoas.reverse()
# for pessoa in pessoas:
#   print('Idade: %s - Altura: %s' % (pessoa[0], pessoa[1]))


# ex09
# vetorA = []
# for i in range(0, 10):
#   vetorA.append(int(input('Informe um numero: ')))

# somaQuadrados = 0
# for numero in vetorA:
#   somaQuadrados += (numero * numero)

# print('A soma dos quadrados dos numeros lidos eh %d' % somaQuadrados)

# ex10
# vetor1 = []
# vetor2 = []
# vetor3 = []

# print('Informe os valores do primeiro vetor')
# for i in range(0, 10):
#   vetor1.append(int(input('Informe um numero: ')))

# print('Informe os valores do segundo vetor')
# for i in range(0, 10):
#   vetor2.append(int(input('Informe um numero: ')))

# for i in range(0, 10):
#   vetor3.append(vetor1[i])
#  vetor3.append(vetor2[i])

# print(vetor3)

# ex11
# vetor1 = []
# vetor2 = []
# vetor3 = []
# vetor4 = []

# print('Informe os valores do primeiro vetor')
# for i in range(0, 10):
#   vetor1.append(int(input('Informe um numero: ')))

# print('Informe os valores do segundo vetor')
# for i in range(0, 10):
#   vetor2.append(int(input('Informe um numero: ')))

# print('Informe os valores do terceiro vetor')
# for i in range(0, 10):
#   vetor3.append(int(input('Informe um numero: ')))

# for i in range(0, 10):
#   vetor4.append(vet1[i])
#  vetor4.append(vet2[i])
# vetor4.append(vetor3[i])

# print(vetor4)

# ex12
#alunos = []
#totalAlunos = 30

#for i in range(0, totalAlunos):
 #   aluno = []
  #  aluno.append(int(input('Informe a idade do aluno: ')))
   # aluno.append(float(input('Informe a altura do aluno: ')))
    #alunos.append(aluno)

#somaAltura = 0.0
#for aluno in alunos:
 #   somaAltura += aluno[1]

#mediaAltura = somaAltura / float(totalAlunos)

#totalAlunosAltos = 0
#for aluno in alunos:
 #   if (aluno[0] >= 13) and (aluno[1] >= mediaAltura):
  #      totalAlunosAltos += 1

#print('Existem %d alunos com mais de 13 anos acima da media de altura' % \
 #     totalAlunosAltos)

#ex13
#meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho',
#         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
#temperaturas = {}

#for mes in meses:
#    temperaturas[mes] = float(input('Informe a temperatura media do mes de %s: ' % mes))

#somaTemperaturas = 0.0
#for temperatura in temperaturas.values():
 #   somaTemperaturas += temperatura

#mediaTemperaturaAnual = somaTemperaturas / 12.0

#print('Temperaturas acima da media anual: %.2f' % mediaTemperaturaAnual)
#for mes in meses:
 #   if (temperaturas[mes] >= mediaTemperaturaAnual):
  #      print('%s - %.2f' % (mes, temperaturas[mes]))

#ex14
#print('Responda as perguntas abaixo com S/N')

#perguntas = ('Telefonou para a vitima? ',
 #            'Esteve no local do crime? ',
  #           'Mora perto da vitima? ',
   #          'Devia para a vitima? ',
    #         'Trabalhou para a vitima? ')

#respostas = []

#for pergunta in perguntas:
 #   respostas.append(input(pergunta).upper())

#classificacao = 0
#for resposta in respostas:
 #   if (resposta == 'S'):
  #      classificacao += 1

#if (classificacao < 2):
 #   print('Inocente')
#elif (classificacao == 2):
 #   print('Suspeito')
#elif (classificacao <= 4):
 #   print('Cumplice')
#else:
 #   print('Assassino')

#ex15
#valores = []
#valor = 0

#while (valor != -1):
 #   valor = int(input('Informe um valor: '))
  #  if (valor != -1):
   #     valores.append(valor)
    #elif (valor == -1):
     #   print("O programa foi encerrado!")

#print('Quantidade de valores lidos: %d' % len(valores))
#print(valores)
#valores.reverse()
#print(valores)

#somaValores = 0
#for valor in valores:
 #   somaValores += valor

#media = somaValores / float(len(valores))
#print('Soma dos Valores: %d' % somaValores)
#print('Media dos Valores: %.2f' % media)

#valoresAcimaDaMedia = 0
#valoresAcimaDeSete = 0
#for valor in valores:
 #   if (valor >= media):
  #      valoresAcimaDaMedia += 1
   # if (valor >= 7):
    #    valoresAcimaDeSete += 1

#print('Valores acima da media: %d' % valoresAcimaDaMedia)
#print('Valores acima de sete: %d' % valoresAcimaDeSete)

#ex16
#salarioBase = 200
#vendedores = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#for i in range(0, 10):
 #   valorVendas = float(input('Informe o valor das vendas do vendedor: '))
  #  salario = valorVendas * 0.09 + salarioBase
   # indice = int(salario / 100) - 1
    #if (indice > 9):
     #   indice = 9
    #elif (indice < 1):
     #   indice = 1
    #print(indice)
    #vendedores[indice - 1] += 1

#for i in range(0, 9):
 #   print('%d - %d : %d' % (i * 100 + 200, (i + 1) * 100 + 199, vendedores[i]))

#ex17
#textoSaltos = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto')
#nomeAtleta = ' '
#atletas = {}

#while (nomeAtleta != ''):
 #   nomeAtleta = input('Atleta: ')
  #  if (nomeAtleta != ''):
   #     saltos = []
    #    for i in textoSaltos:
     #       saltos.append(float(input('%s Salto: ' % i)))
      #  atletas[nomeAtleta] = saltos

#print('\n Resultado Final:')
#for (nomeAtleta, saltos) in atletas.items():
 #   print('Atleta: %s' % nomeAtleta)
  #  print('Saltos: ' , saltos)
   # somaSaltos = 0.0
    #for salto in saltos:
     #   somaSaltos += salto
    #print('Media dos Saltos %.2f m' % (somaSaltos / float(len(textoSaltos))))

#ex18
#votosAtletas = [0] * 23
#numeroAtleta = -1
#totalVotos = 0
#print('Quem foi o melhor jogador?')

#while (numeroAtleta != 0):
 #   numeroAtleta = int(input('Numero do jogador (0=fim): '))
  #  if (numeroAtleta < 0) or (numeroAtleta > 23):
   #     print('Informe um valor entre 1 e 23 ou 0 para sair!')
    #    continue
    #if (numeroAtleta != 0):
     #   votosAtletas[numeroAtleta - 1] += 1
      #  totalVotos += 1

#print('Resultado da votacao:')

#print('Foram computados %d votos' % totalVotos)
#print('Jogador\tVotos\t%')
#contador = 1
#melhorJogador = 0
#for votosAtleta in votosAtletas:
 #   if (votosAtleta > 0):
  #      print('%d\t%d\t%.2f%%' %\
   #           (contador, votosAtleta, votosAtleta / float(totalVotos) * 100))
    #    if (votosAtleta > votosAtletas[melhorJogador]):
     #       melhorJogador = contador - 1
    #contador += 1

#print('O melhor jogador foi o numero %d, com %d votos, correspondendo a '\
 #   '%.2f do total de votos' %\
  #  (melhorJogador + 1, votosAtletas[melhorJogador],
   #     votosAtletas[melhorJogador] / float(totalVotos) * 100))

#ex19
#sistemasOperacionais = (
#    'Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro')
#votosSistemas = [0] * 6
#opcao = -1
#totalVotos = 0
#print('Qual o melhor Sistema Operacional para uso em servidores?')
#print('\nAs possiveis respostas sao:\n')

#i = 0
#for sistema in sistemasOperacionais:
 #   print('%d- %s' % (i + 1, sistemasOperacionais[i]))
  #  i += 1

#while (opcao != 0):
 #   opcao = int(input('Sistema escolhido (0=fim): '))
  #  if (opcao < 0) or (opcao > 23):
   #     print('Informe um valor entre 1 e 6 ou 0 para sair!')
    #    continue
    #if (opcao != 0):
     #   votosSistemas[opcao - 1] += 1
      #  totalVotos += 1

#print('Sistema Operacional   Votos   %')
#print('-------------------   -----   ------')
#i = 0
#maiorVoto = 0
#for sistema in sistemasOperacionais:
 #   print('%-21s %5d   %2.2f' %\
  #      (sistemasOperacionais[i], votosSistemas[i],
   #      votosSistemas[i] / float(totalVotos) * 100))
    #if (votosSistemas[i] > votosSistemas[maiorVoto]):
     #   maiorVoto = i
    #i += 1
#print('-------------------   -----')
#print('Total                   %3d' % totalVotos)

#print('O sistema operacional mais votado foi o %s, com %d votos, correspondendo a '\
#    '%.2f%% dos votos.' %\
 #   (sistemasOperacionais[maiorVoto], votosSistemas[maiorVoto],
  #      votosSistemas[maiorVoto] / float(totalVotos) * 100))

#ex20

#salarios = []
#salarioFuncionario = -1
#print('Projecao de Gastos com Abono')
#print('============================\n')

#while (salarioFuncionario != 0):
 #   salarioFuncionario = float(input('Salario: '))
  #  if (salarioFuncionario < 0):
   #     print('Informe um valor maior que 0 ou 0 para sair!')
    #    continue
    #if (salarioFuncionario != 0):
     #   salarios.append(salarioFuncionario)

#print('Salario\tAbono')

#totalAbono = 0.0
#totalPiso = 0

#for salario in salarios:
 #   abono = salario * 0.2
  #  if (abono < 100):
   #     abono = 100.0
    #    totalPiso += 1
    #totalAbono += abono
    #if ('maiorAbono' not in vars()) or (abono > maiorAbono):
     #   maiorAbono = abono
    #print('R$ %.2f\tR$%.2f' % (salario, abono))

#print('Foram processados %d colaboradores' % len(salarios))
#print('Total gasto com abonos: %.2f' % totalAbono)
#print('Valor minimo pago a %d colaboradores' % totalPiso)
#print('Maior valor de abono pago: %.2f' % maiorAbono)

#ex21
#veiculos = []
#consumo = []
#preco = 6.48

#for i in range(1, 6):
 #   veiculos.append(input('Veiculo %d: ' % i))
  #  consumo.append(float(input('Km por litro: ')))

#print('Relatorio Final')

#for i in range(0, 5):
 #   custo = 1000 / consumo[i]
  #  gasto = custo * preco
   # print('%d - %s - %.2f - %.1f litros - R$ %.2f' %\
    #    (i + 1, veiculos[i], consumo[i], custo, gasto))
    #if ('menorConsumo' not in vars()) or (consumo[i] > consumo[menorConsumo]):
     #   menorConsumo = i

#print('O menor consumo eh do %s' % veiculos[menorConsumo])

#ex22

#idMouse = -1
#defeitos = ('1 - Necessita de Esfera',
 #           '2 - Necessita de limpeza',
  #          '3 - Necessita troca de cabo ou conector',
   #         '4 - Quebrado ou inutilizado')
#totalDefeitos = [0] * 4
#totalMouses = 0

#for i in defeitos:
 #   print('%s' % i)

#while (idMouse != 0):
 #   idMouse = int(input('Identificador do Mouse: '))
  #  if (idMouse != 0):
   #     defeito = int(input('Codigo do defeito: '))
    #    totalDefeitos[defeito - 1] += 1
     #   totalMouses += 1

#print('Quantidade de mouses: %d ' % totalMouses)

#print('Situacao\tQuantidade\tPercentual')
#for i in range(0, len(defeitos)):
 #   print('%s\t%d\t%.2f' %\
  #      (defeitos[i], totalDefeitos[i], totalDefeitos[i] /
   #         float(totalMouses) * 100))

#ex23

#ex24
#import random

#dado = [0] * 6

#for i in range(0, 100):
 #   lancamento = random.randint(0, 5)
  #  dado[lancamento] += 1

#for i in range(0, 6):
 #   print('%d - %d' % (i + 1, dado[i]))