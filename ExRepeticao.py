#ex01

#nota = -1
#while (nota < 0) or (nota > 10):
 #   nota = int(input('Informe uma nota: '))
  #  if (nota < 0) or (nota > 10):
   #     print('Nota Invalida')

#ex02

#usuario = senha = ''
#while (usuario == senha):
 #   usuario = input('Informe um nome de usuario: ')
  #  senha = input('Informe a senha: ')
   # if (usuario == senha):
    #    print('A senha não pode ser igual ao nome do usuario')

#ex03

#nome = ''
#while (len(nome) <= 3):
 #   nome = input('Informe um nome: ')
  #  if (len(nome) <= 3):
   #     print('O nome deve ter mais de tres letras!')

#idade = -1
#while (idade < 0) or (idade > 150):
 #   idade = int(input('Informe a idade: '))
  #  if (idade < 0) or (idade > 150):
   #     print('Idade deve estar entre 0 e 150')

#salario = 0
#while (salario <= 0):
 #   salario = int(input('Informe o salario: '))
  #  if (salario <= 0):
   #     print('O salario deve ser maior que zero')

#sexo = ''
#while (sexo != 'F') and (sexo != 'M'):
 #   sexo = input('Informe o sexo: ').upper()
  #  if (sexo != 'F') and (sexo != 'M'):
   #     print('O sexo deve ser infomado como M (masculino) ou F (feminino)')

#estado_civil = 'A'
#while ('SCVD'.find(estado_civil) < 0):
 #   estado_civil = input('Informe o estado civil: ').upper()
  #  if ('SCVD'.find(estado_civil) < 0):
   #     print('Estado civil deve ser informado como S (solteiro), C (casado),'\
    #        ' V (viuvo) ou D (divorciado)')

#ex04

#populacaoA = 80000
#crescimentoA = 1.03
#populacaoB = 200000
#crescimentoB = 1.015

#ano = 1
#while (populacaoA <= populacaoB):
 #   populacaoA *= crescimentoA
  #  populacaoB *= crescimentoB
   # ano += 1


#print('Serão necessários', ano, 'anos para que a população do país A'\
 #   ' ultrapasse a população do pais B')

#ex05
#populacaoA = 0
#crescimentoA = 0

#while (populacaoA <= 0):
 #   populacaoA = int(input('Informe a populacao do pais A: '))
  #  if (populacaoA <= 0):
   #     print('Populacao deve ser um valor maior que 0')
#while (crescimentoA <= 0):
 #   crescimentoA = float(input('Informe o percentual de crescimento do pais A: '))
  #  if (crescimentoA <= 0):
   #     print('Percentual de crescimento deve ser maior que 0')
#populacaoB = populacaoA
#while (populacaoB <= populacaoA):
 #   populacaoB = int(input('Informe a populacao do pais B: '))
  #  if (populacaoB <= populacaoA):
   #     print('Populacao do pais B deve ser maior que a populacao do pais A')
#crescimentoB = crescimentoA
#while (crescimentoB >= crescimentoA):
 #   crescimentoB = float(input('Informe o percentual de crescimento do pais B: '))
  #  if (crescimentoB >= crescimentoA):
   #     print('Percentual de crescimento do pais B deve ser menor que o do '
    #        'pais A')

#crescimentoA = 1 + (crescimentoA / 100.0)
#crescimentoB = 1 + (crescimentoB / 100.0)

#ano = 1
#while (populacaoA <= populacaoB):
 #   populacaoA *= crescimentoA
  #  populacaoB *= crescimentoB
   # ano += 1

#print('Serao necessarios', ano, 'anos para que a populacao do pais A '
 #   'ultrapasse a populacao do pais B')

#ex06
#for i in range(1, 21):
 #   print(i)

#for i in range(1, 21):
 #   print(i, end=" ")

#ex07
#for i in range(0, 5):
 #   numero = int(input('Informe um numero: '))
  #  if ('maior' in vars()):
   #     if (numero > maior):
    #        maior = numero
    #else:
     #   maior = numero

#print('O maior numero que voce digitou e', maior)

#ex08
#soma = 0
#for i in range(0, 5):
 #   numero = int(input('Informe um numero: '))
  #  soma += numero

#print('A soma dos numeros digitados eh', soma)
#print('A media dos numeros digitados eh', (soma / 5.0))

#ex09
#for i in range(0, 50):
 #   if (i % 2 != 0):
  #      print(i)

#ex10
#inicial = int(input('Informe o valor inicial: '))
#final = inicial
#while (final <= inicial):
 #   final = int(input('Informe o valor final: '))
  #  if (final <= inicial):
   #     print('O valor final deve ser maior que o valor inicial')

#for i in range(inicial, final + 1):
 #   print(i)

#ex11
#inicial = int(input('Informe o valor inicial: '))
#final = inicial
#while (final <= inicial):
 #   final = int(input('Informe o valor final: '))
  #  if (final <= inicial):
   #     print('O valor final deve ser maior que o valor inicial')

#soma = 0
#for i in range(inicial, final + 1):
 #   soma += i
  #  print(i)

#print('A soma dos números é ', soma)

#ex12
#numero = int(input('Informe o numero que voce quer ver a tabuada: '))

#print('Tabuada de', numero, ':')
#for i in range(1, 11):
 #   print(numero, 'X', i, '=', (numero * i))

#ex13
#base = int(input('Informe o valor da base: '))
#expoente = int(input('Informe o valor do expoente: '))

#potencia = 1
#for i in range(1, expoente + 1):
 #   potencia *= base

#print(base, 'elevada a', expoente, '=', potencia)

#ex14
#print('Informe 10 numeros')
#pares = 0
#impares = 0
#for i in range(1, 11):
 #   numero = int(input('Informe um numero: '))
  #  if (numero % 2 == 0):
   #     pares += 1
    #else:
     #   impares += 1

#print('Numeros pares:', pares)
#print('Numeros impares:', impares)

#ex15
#termo = 0
#while (termo <= 0):
 #   termo = int(input('Voce quer a serie de Fibonacci ate qual termo: '))
  #  if (termo <= 0):
   #     print('O termo deve ser positivo!')

#primeiro = 0
#print(primeiro)
#segundo = 1
#for i in range(1, termo):
 #   print(segundo)
  #  terceiro = primeiro + segundo
   # primeiro = segundo
    #segundo = terceiro

#ex16
#primeiro = 0
#print(primeiro)
#segundo = 1
#while (segundo < 500):
 #   print(segundo)
  #  terceiro = primeiro + segundo
   # primeiro = segundo
    #segundo = terceiro

#ex17
#numero = 0
#while (numero <= 0):
 #   numero = int(input('Informe o número que deseja calcular o fatorial: '))
  #  if (numero <= 0):
   #     print('O termo deve ser positivo!')

#fatorial = 1
#for i in range(1, numero + 1):
 #   fatorial *= i

#print(fatorial)

#ex18
#quantidade = 0
#while (quantidade <= 0):
 #   quantidade = int(input('Informe a quantidade de números: '))
  #  if (quantidade <= 0):
   #     print('Quantidade deve ser positiva')

#soma = 0
#for i in range(0, quantidade):
 #   numero = int(input('Informe um numero: '))
  #  if ('maior' not in vars()) or (numero > maior):
   #     maior = numero

    #if ('menor' not in vars()) or (numero < menor):
     #   menor = numero

    #soma += numero

#print('Menor numero:', menor)
#print('Maior numero:', maior)
#print('Soma dos numeros:', soma)

#ex19
#quantidade = 0
#while (quantidade <= 0):
 #   quantidade = int(input('Informe a quantidade de números: '))
  #  if (quantidade <= 0):
   #     print('Quantidade deve ser positiva!')

#soma = 0
#for i in range(0, quantidade):
 #   numero = 1001
  #  while (numero > 1000):
   #     numero = int(input('Informe um numero: '))
    #    if (numero > 1000):
     #       print('O numero deve ser menor ou igual a 1000!')
    #if ('maior' not in vars()) or (numero > maior):
     #   maior = numero

    #if ('menor' not in vars()) or (numero < menor):
     #   menor = numero

    #soma += numero

#print('Menor numero:', menor)
#print('Maior numero:', maior)
#print('Soma dos numeros:', soma)

#ex20
#quantidade = 0
#while (quantidade <= 0):
 #   quantidade = int(input('Voce quer calcular quantos fatoriais: '))
  #  if (quantidade <= 0):
   #     print('Quantidade deve ser positiva!')

#for i in range(0, quantidade):
 #   termo = 0
  #  while (termo <= 0) or (termo > 16):
   #     termo = int(input('Voce quer o fatorial de qual número: '))
    #    if (termo <= 0):
     #       print('O número deve ser positivo!')
      #  if (termo > 16):
       #     print('O número deve ser menor que 16')

    #fatorial = 1
    #for i in range(1, termo + 1):
     #   fatorial *= i

    #print(fatorial)

#ex21
#numero = 0
#while (numero <= 0):
 #   numero = int(input('Informe um número: '))
  #  if (numero <= 0):
   #     print('O numero deve ser positivo!')

#test = int(numero / 2) + 1
#primo = True
#for i in range(2, test):
 #   if (numero % i == 0):
  #      primo = False

#if (primo):
 #   print('O numero é primo')
#else:
 #   print('O numero não é primo')

#ex22
#numero = 0
#while (numero <= 0):
 #   numero = int(input('Informe um número: '))
  #  if (numero <= 0):
   #     print('O numero deve ser positivo!')

#test = int(numero / 2 + 1)
#primo = True
#for i in range(2, test):
 #   if (numero % i == 0):
  #      primo = False
   #     break

#if (primo):
 #   print('O numero é primo')
#else:
 #   print('O numero não é primo')
  #  print('Ele é divisivel por',)
   # for i in range(1, numero + 1):
    #    if (numero % i == 0):
     #       print(i,)

#ex23
#quantidade = 0
#while (quantidade <= 0):
 #   quantidade = int(input('Informe o range: '))
  #  if (quantidade <= 0):
   #     print('A quandidade deve ser positiva!')

#quantidadeDivisoes = 0
#for numero in range(1, quantidade + 1):
 #   test = int(numero / 2 + 1)
  #  primo = True
   # for i in range(2, test):
    #    quantidadeDivisoes += 1
     #   if (numero % i == 0):
      #      primo = False
       #     break

    #if (primo):
     #   print(numero,)

#print('\nQuantidade de divisoes:', quantidadeDivisoes)

#ex24
#quantidade = 0
#while (quantidade <= 0):
 #   quantidade = int(input('Informe a quantidade de notas: '))
  #  if (quantidade <= 0):
   #     print('A quandidade deve ser positiva!')

#soma = 0.0
#for i in range(0, quantidade):
 #   nota = -1
  #  while (nota < 0) or (nota > 10):
   #     nota = float(input('Informe a nota: '))
    #    if (nota < 0) or (nota > 10):
     #       print('A nota deve estar entre 0 e 10')
    #soma += nota

#print('A media das notas eh', (soma / float(quantidade)))

#ex25
#quantidade = 0
#while (quantidade <= 0):
 #   quantidade = int(input('Informe a quantidade de pessoas: '))
  #  if (quantidade <= 0):
   #     print('A quandidade deve ser positiva!')

#soma = 0
#for i in range(0, quantidade):
 #   idade = -1
  #  while (idade < 0):
   #     idade = int(input('Informe a idade da pessoa: '))
    #    if (idade < 0):
     #       print('A idade não pode ser negativa')
    #soma += idade

#media = soma / float(quantidade)

#if (media <= 25):
 #   print('A turma é jovem')
#elif (media <= 60):
 #   print('A turma é adulta')
#else:
 #   print('A turma é idosa')

#ex26
#quantidade = 0
#while (quantidade <= 0):
 #   quantidade = int(input('Informe a quantidade de eleitores: '))
  #  if (quantidade <= 0):
   #     print('A quandidade deve ser positiva!')

#votosCandidato1 = 0
#votosCandidato2 = 0
#votosCandidato3 = 0
#for i in range(0, quantidade):
 #   voto = 0
  #  while (voto < 1) or (voto > 3):
   #     voto = int(input('Voce quer votar no candidato 1, 2 ou 3: '))
    #    if (voto < 1) or (voto > 3):
     #       print('Candidato invalido! Vote novamente')
    #if (voto == 1):
     #   votosCandidato1 += 1
    #elif (voto == 2):
     #   votosCandidato2 += 1
    #else:
     #   votosCandidato3 += 1

#print('Resultado:')
#print('Candidato 1:', votosCandidato1)
#print('Candidato 2:', votosCandidato2)
#print('Candidato 3:', votosCandidato3)

#ex27
#quantidade = 0
#while (quantidade <= 0):
 #   quantidade = int(input('Informe a quantidade de turmas: '))
  #  if (quantidade <= 0):
   #     print('A quandidade deve ser positiva!')

#soma = 0
#for i in range(0, quantidade):
 #   alunos = -1
  #  while (alunos < 0) or (alunos > 40):
   #     alunos = int(input('Informe a quantidade de alunos da turma: '))
    #    if (alunos < 0) or (alunos > 40):
     #       print('A turma deve ter até 40 alunos')
    #soma += alunos

#media = soma / float(quantidade)

#print('Media de alunos por turma', media)

#ex28
#quantidade = 0
#while (quantidade <= 0):
 #   quantidade = int(input('Informe a quantidade de CDs: '))
  #  if (quantidade <= 0):
   #     print('A quandidade deve ser positiva!')

#soma = 0
#for i in range(0, quantidade):
 #   valor = -1
  #  while (valor < 0):
   #     valor = float(input('Informe o valor pago pelo CD: '))
    #    if (valor < 0):
     #       print('O valor deve ser maior ou igual a 0')
    #soma += valor

#media = soma / float(quantidade)

#print ('Quantidade de CDs:', quantidade)
#print ('Media do valor dos CDs:', media)

#ex29
#print ('Loja Quase Dois - Tabela de precos')
#for i in range(1, 51):
 #   print ('%d - R$ %.2f' % (i, i * 1.99))

#ex30
#precoPao = float(input('Preco do pão: '))

#print ('Panificadora Pao de Ontem - Tabela de precos')
#for i in range(1, 51):
#    print ('%d - R$ %.2f' % (i, i * precoPao))

#ex31
#soma = 0.0
#quantidade = 1
#precoMercadoria = 1
#while (precoMercadoria != 0):
 #   precoMercadoria = float(input('Produto %d: R$ ' % (quantidade)))
  #  soma += precoMercadoria

#print ('Total: R$ %.2f' % soma)
#pagamento = float(input('Dinheiro: R$ '))

#print ('Troco: R$ %.2f' % ((pagamento - soma)*(-1)))

#ex32
#termo = 0
#while (termo <= 0):
 #   termo = int(input('Voce quer o fatorial de qual termo: '))
  #  if (termo <= 0):
   #     print ('O termo deve ser positivo!')

#fatorial = 1
#print ('Fatorial de %d' % termo)
#print ('!%d = ' % termo,end='')
#for i in reversed(range(2, termo + 1)):
 #   print ('%d . ' % i,end="")
  #  fatorial *= i

#print ('1 = %d' % fatorial)

#ex33
#quantidade = 0
#while (quantidade <= 0):
 #   quantidade = int(input('Informe a quantidade de temperaturas: '))
  #  if (quantidade <= 0):
   #     print ('A quandidade deve ser positiva!')

#soma = 0.0
#for i in range(0, quantidade):
 #   temperatura = float(input('Informe a temperatura: '))
  #  if ('maior' not in vars()) or (temperatura > maior):
   #     maior = temperatura
    #if ('menor' not in vars()) or (temperatura < menor):
     #   menor = temperatura
    #soma += temperatura

#media = soma / float(quantidade)

#print ('Media da temperatura: ', media)
#print ('Maior temperatura: ', maior)
#print ('Menor temperatura: ', menor)

#ex36
#tabuada = int(input('Montar a tabuada de: '))

#comecar = -1
#while (comecar < 0):
 #   comecar = int(input('Comecar por: '))
  #  if (comecar < 0):
   #     print ('O numero deve ser maior que 0')

#terminar = comecar
#while (comecar >= terminar):
 #   terminar = int(input('Terminar em: '))
  #  if (comecar >= terminar):
   #     print ('Deve terminar com um numero maior que o de comecar')

#print ('Vou montar a tabuada de', tabuada, 'comecando em', comecar,\
 #   'e terminando em', terminar)
#for i in range(comecar, terminar + 1):
 #   print ('%i X %i = %i' % (tabuada, i, tabuada * i))

#ex38
#salario = float(input("Informe o salário inicial: "))
#percentual = 1.5
#ano = 1996

#while (ano <= 2014):
 #   print ('Ano (%i) Percentual (%.2f) Salario (%.2f)' %\
  #      (ano, percentual, salario))
  #  salario += (salario * (percentual / 100.0))
   # percentual *= 2
    #ano += 1

#print ('Salario atual do funcionario: %.2f' % (salario))

#ex39

#for i in range(0, 10):
 #   codigo = int(input('Informe o numero do aluno: '))
  #  altura = float(input('Informe a altura do aluno: '))
   # if ('maisAlto' not in vars()) or (altura > maisAlto):
    #    maisAlto = altura
     #   codigoMaisAlto = codigo
    #if ('maisBaixo' not in vars()) or (altura < maisBaixo):
     #   maisBaixo = altura
      #  codigoMaisBaixo = codigo

#print ('O aluno mais alto eh o de codigo %i com %f' %\
 #   (codigoMaisAlto, maisAlto))
#print ('O aluno mais baixo eh o de codigo %i com %f' %\
 #   (codigoMaisBaixo, maisBaixo))

#ex40
#somaVeiculos = 0
#somaAcidentes = 0
#somaAcidentesMenos2Mil = 0
#totalCidadesMenos2Mil = 0

#for i in range(0, 5):
 #   codigo = int(input('Informe o codigo da cidade: '))
  #  veiculos = int(input('Informe o numero de veiculos de passeio: '))
   # acidentes = int(input('Informe a quantidade de acidentes em 1999: '))

    #indiceAcidentes = acidentes / float(veiculos)
    #somaVeiculos += veiculos

    #if ('maisAcidentes' not in vars()) or (indiceAcidentes > maisAcidentes):
     #   maisAcidentes = indiceAcidentes
      #  codigoMaisAcidentes = codigo
    #if ('menosAcidentes' not in vars()) or (indiceAcidentes < menosAcidentes):
     #   menosAcidentes = indiceAcidentes
      #  codigoMenosAcidentes = codigo

    #if (veiculos < 2000):
     #   somaAcidentesMenos2Mil += acidentes
      #  totalCidadesMenos2Mil += 1

#print ('O cidade com maior indice de acidentes eh %i com %.2f' %\
 #   (codigoMaisAcidentes, maisAcidentes))
#print ('O cidade com menor indice de acidentes eh %i com %.2f' %\
 #   (codigoMenosAcidentes, menosAcidentes))
#print ('A media de veiculos nas cidades eh %.2f' % (somaVeiculos / 5.0))
#print ('A media de acidentes de transito nas cidades com menos '\
 #   'de 2k veiculos eh %.2f' %\
  #  (somaAcidentesMenos2Mil / float(totalCidadesMenos2Mil)))

#ex41
#divida = float(input('Informe o valor da divida: '))

#print(\
 #   'Valor da divida\tValor dos Juros\t'\
  #  'Quantidade de Parcelas\tValor da Parcela')
#juros = 0
#for i in [1, 3, 6, 9, 12]:
 #   valorJuros = (divida * (juros / 100.0))
  #  valorDivida = divida + valorJuros
   # valorParcela = valorDivida / float(i)
    #print ('R$ %.2f\tR$ %.2f\t%i\tR$ %.2f' %\
     #   (valorDivida, valorJuros, i, valorParcela))
    #if (i == 1):
     #   juros = 10
    #else:
     #   juros += 5

#ex42
#numero = 0

#intervalo025 = 0
#intervalo2650 = 0
#intervalo5175 = 0
#intervalo76100 = 0

#while (numero >= 0):
 #   numero = int(input('Informe um numero: '))

  #  if (numero >= 0):
   #     if (numero <= 25):
    #        intervalo025 += 1
     #   elif (numero <= 51):
      #      intervalo2650 += 1
       # elif (numero <= 75):
        #    intervalo5175 += 1
        #elif (numero <= 100):
         #   intervalo76100 += 1

#print ('%d numeros no intervalo [0-25]' % (intervalo025))
#print ('%d numeros no intervalo [26-50]' % (intervalo2650))
#print ('%d numeros no intervalo [51-75]' % (intervalo5175))
#print ('%d numeros no intervalo [75-100]' % (intervalo76100))

#ex43
#print ('Especificacao   Codigo  Preco')
#print ('Cachorro Quente 100     R$ 1,20')
#print ('Bauru Simples   101     R$ 1,30')
#print ('Bauru com Ovo   102     R$ 1,50')
#print ('Hamburger       103     R$ 1,20')
#print ('Cheeseburger    104     R$ 1,30')
#print ('Refrigerante    105     R$ 1,00')

#codigo = 100
#valorTotal = 0
#while (codigo >= 100 and codigo <= 105):
#    codigo = int(input('Informe o codigo do produto ou um codigo invalido para encerrar: '))
 #   if (codigo >= 100 and codigo <= 105):
  #      quantidade = int(input('Informe a quantidade: '))
   #     if (codigo == 100):
    #        valorItem = 1.20 * quantidade
     #   elif (codigo == 101):
      #      valorItem = 1.30 * quantidade
       # elif (codigo == 102):
        #    valorItem = 1.50 * quantidade
        #elif (codigo == 103):
         #   valorItem = 1.20 * quantidade
        #elif (codigo == 104):
         #   valorItem = 1.30 * quantidade
        #elif (codigo == 105):
         #   valorItem = 1.0 * quantidade
        #print ('Valor do item: %.2f' % valorItem)
        #valorTotal += valorItem

#print ('Valor Total: %.2f' % (valorTotal))

#ex44
'''
print ('URNA ELETRONICA')
print ('1 - Joao')
print ('2 - Jose')
print ('3 - Jaco')
print ('4 - Jobe')
print ('5 - Voto Nulo')
print ('6 - Voto em Branco')

opcao1 = opcao2 = opcao3 = opcao4 = opcao5 = opcao6 = 0
totalVotos = 0
codigo = 1
while (codigo >= 1 and codigo <= 6):
    codigo = int(input('Informe a opcao ou zero para encerrar: '))
    if (codigo >= 1 and codigo <= 6):
        if (codigo == 1):
            opcao1 += 1
        elif (codigo == 2):
            opcao2 += 1
        elif (codigo == 3):
            opcao3 += 1
        elif (codigo == 4):
            opcao4 += 1
        elif (codigo == 5):
            opcao5 += 1
        elif (codigo == 6):
            opcao6 += 1
        totalVotos += 1

print ('RESULTADO:')
print ('1 - Joao - %d votos' % (opcao1))
print ('2 - Jose - %d votos' % (opcao2))
print ('3 - Jaco - %d votos' % (opcao3))
print ('4 - Jobe - %d votos' % (opcao4))
print ('5 - %d votos nulos' % (opcao5))
print ('6 - %d votos em branco' % (opcao6))
print ('Percentual de votos nulos: %.2f%%' % (opcao5 / float(totalVotos) * 100))
print ('Percentual de votos em branco: %.2f%%' %\
    (opcao6 / float(totalVotos) * 100))
'''

#ex45
'''
continua = 'S'
totalAlunos = 0
somaAcertos = 0

while (continua.upper() == 'S'):
    acertos = 0
    print ('Informe a resposta de cada questao:')
    resposta = input('Questao 1: ').upper()
    if (resposta == 'A'):
        acertos += 1
    resposta = input('Questao 2: ').upper()
    if (resposta == 'B'):
        acertos += 1
    resposta = input('Questao 3: ').upper()
    if (resposta == 'C'):
        acertos += 1
    resposta = input('Questao 4: ').upper()
    if (resposta == 'D'):
        acertos += 1
    resposta = input('Questao 5: ').upper()
    if (resposta == 'E'):
        acertos += 1
    resposta = input('Questao 6: ').upper()
    if (resposta == 'E'):
        acertos += 1
    resposta = input('Questao 7: ').upper()
    if (resposta == 'D'):
        acertos += 1
    resposta = input('Questao 8: ').upper()
    if (resposta == 'C'):
        acertos += 1
    resposta = input('Questao 9: ').upper()
    if (resposta == 'B'):
        acertos += 1
    resposta = input('Questao 10: ').upper()
    if (resposta == 'A'):
        acertos += 1

    somaAcertos += acertos
    print ('Total de Acertos: %d' % acertos)

    if ('maiorAcerto' not in vars()) or (acertos > maiorAcerto):
        maiorAcerto = acertos
    if ('menorAcerto' not in vars()) or (acertos < menorAcerto):
        menorAcerto = acertos

    totalAlunos += 1

    continua = input('Deseja continuar (S/N): ').upper()

print ('Maior acerto: %d' % maiorAcerto)
print ('Menor acerto: %d' % menorAcerto)
print ('Total de alunos que utilizaram o sistema: %d' % totalAlunos)
print ('Media de acertos: %.2f' % (somaAcertos / float(totalAlunos)))
'''

#EX46
'''
nomeAtleta = ' '

while (nomeAtleta != ''):
    nomeAtleta = input('Atleta: ')

    if (nomeAtleta != ''):
        primeiroSalto = float(input('Primeiro Salto: '))
        segundoSalto = float(input('Segundo Salto: '))
        terceiroSalto = float(input('Terceiro Salto: '))
        quartoSalto = float(input('Quarto Salto: '))
        quintoSalto = float(input('Quinto Salto: '))

        somaSaltos = primeiroSalto + segundoSalto + \
            terceiroSalto + quartoSalto + quintoSalto
        if (primeiroSalto >= segundoSalto) and \
           (primeiroSalto >= terceiroSalto) and \
           (primeiroSalto >= quartoSalto) and \
           (primeiroSalto >= quintoSalto):
            melhorSalto = primeiroSalto
        elif (segundoSalto >= terceiroSalto) and \
             (terceiroSalto >= quartoSalto) and \
             (quartoSalto >= quintoSalto):
            melhorSalto = segundoSalto
        elif (terceiroSalto >= quartoSalto) and \
             (terceiroSalto >= quintoSalto):
            melhorSalto = terceiroSalto
        elif (quartoSalto >= quintoSalto):
            melhorSalto = quartoSalto
        else:
            melhorSalto = quintoSalto
        somaSaltos -= melhorSalto

        if (primeiroSalto <= segundoSalto) and \
           (primeiroSalto <= terceiroSalto) and \
           (primeiroSalto <= quartoSalto) and \
           (primeiroSalto <= quintoSalto):
            piorSalto = primeiroSalto
        elif (segundoSalto <= terceiroSalto) and \
             (terceiroSalto <= quartoSalto) and \
             (quartoSalto <= quintoSalto):
            piorSalto = segundoSalto
        elif (terceiroSalto <= quartoSalto) and (terceiroSalto <= quintoSalto):
            piorSalto = terceiroSalto
        elif (quartoSalto <= quintoSalto):
            piorSalto = quartoSalto
        else:
            piorSalto = quintoSalto
        somaSaltos -= piorSalto

        print ('Melhor Salto: %.2f m' % (melhorSalto))
        print ('Pior Salto: %.2f m' % (piorSalto))
        print ('Media dos demais saltos: %.2f m' % (somaSaltos / 3.0))

        print ('Resultado Final: ')
        print ('%s: %.2f m' % (nomeAtleta, (somaSaltos / 3.0)))'''


#ex47
'''nomeAtleta = ' '
somaNotas = 0

atleta = input('Atleta: ')

for i in range(0, 7):

    nota = float(input('Nota: '))
    somaNotas += nota

    if ('maiorNota' not in vars()) or (nota > maiorNota):
        maiorNota = nota

    if ('menorNota' not in vars()) or (nota < menorNota):
        menorNota = nota

somaNotas -= maiorNota
somaNotas -= menorNota

print ('\nResultado final:')
print ('Atleta: %s' % nomeAtleta)
print ('Melhor nota: %.2f' % maiorNota)
print ('Pior nota: %.2f' % menorNota)
print ('Media: %.2f' % (somaNotas / 5.0))'''

#ex48
'''numero = input('Informe um numero: ')

print (numero[::-1])'''

#ex49
'''termos = int(input('Informe a quantidade de termos que deseja: '))

s = 0.0
denominador = 1
for i in range(1, termos + 1):
    s += i / denominador
    denominador += 2

print ('Resultado: %.2f' % s)'''

#ex50
'''termos = int(input('Informe a quantidade de termos que deseja: '))

s = 0.0
for i in range(1, termos + 1):
    s += 1 / i

print ('Resultado: %.2f' % s)'''