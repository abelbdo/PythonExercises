#ex1
#String1 = input("Digite uma palavra: \n")
#String2 = input("Digite uma segunda palavra: \n")
#tamanho1 = len(String1)
#tamanho2 = len(String2)

#print(f"Tamanho de {String1} é de {tamanho1} caracteres")
#print(f"Tamanho de {String2} é de {tamanho2} caracteres")

#if tamanho1 == tamanho2:
#    print("As string são de tamanhos iguais")
#    elif String1 == String2:
#    print("As Strings são iguais")

#ex2
#nome = input("Informe o seu nome: \n")
#Anagrama = nome[: : -1]

#print(f"O inverso de seu nome é {Anagrama}")

#ex3
#nome = input("Digite o seu nome: \n")

#for i in nome:
 #   print(str(i))

#ex4
#nome = input("Digite o seu nome: \n")

#for i in range(0, len(nome)+1):
#    print(nome[:i])

#ex5
#nome = input("Digite o seu nome: \n")

#for i in range(0, len(nome)+1):
#    print(nome[:-i])

#ex6
#data = input("Digite a data de nascimento (dd/mm/aaaa): ")
#listaData = data.split("/")

#meses = ["janeiro", "fevereiro", "março", "abril", "maio",
# "junho", "julho", "agosto", "setembro", "outubro",
# "novembro", "dezembro"]
#mesExtenso = meses[int(listaData[1])-1]
#print("Data de nascimento: " +data)
#print("Você nasceu em " +listaData[0] + " de " + mesExtenso + " de " + listaData[2])

#ex7
#frase = input("Digite uma frase:")
#vogais =0
#espacos =0
#for letra in frase:
#    if letra == " ":
 #       espacos += 1
  #  elif letra in "aeiou":
   #     vogais += 1
#print("A frase tem %d vogais e %d espaços" %(vogais,espacos))

#ex8
#palavra = input("Escreva uma palavra: ").replace(" ", "")
#palavraInvertida = palavra[::-1]
#if palavra == palavraInvertida:
 #   print("É um palíndromo")
#else:
 #   print("Não é um palíndromo")

#ex9
#cpf = input("Informe o CPF xxx.xxx.xxx-xx // com pontos e traço: \n")
#if (cpf[3] != ".") or (cpf[7] != ".") or (cpf[11] != "-"):
#    print = input("O 'CPF' pricisa estar no formato xxx.xxx.xxx-xx ")
#else:
#    print("O CPF está no formato correto")

#ex10
#numeral = int(input("Informe um numero de 1 a 99: \n"))
#def converter_em_texto(numeral):
 #   dicionario_numerico = {
  #      0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
   #     6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
    #    11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze',
     #   16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte',
      #  30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta',
       # 80: 'oitenta', 90: 'noventa',
    #}

#    if numeral > 99 or numeral < 0:
#        print('O número deve estar entre 0 e 99 (inclusive)')

 #   if numeral < 20 or numeral % 10 == 0:
  #      return dicionario_numerico.get(numeral)

   # decimal = numeral // 10 * 10
    #unidade = numeral % 10
    #extenso = f'{dicionario_numerico.get(decimal)} e {dicionario_numerico.get(unidade)}'
    #return extenso

#numero_por_extenso = converter_em_texto(numeral)
#print(numero_por_extenso)

#ex11
#def print_forca(forca):
 #   print(' '.join(forca).upper())
  #  print('')


#palavras = input("Informe uma palavra: \n")

#forca = ['_' for i in range(len(palavras))]
#erros = 0
#ganhou = False

#while erros < 6 and not ganhou:
 #   print_forca(forca)
  #  print('Digite uma letra:')
   # chute = str(input()).lower()

#    if chute not in palavras:
 #       erros += 1
  #      print(f'Você errou pela {erros}a vez. Tente de novo!')
   #     continue

    #for index, letra in enumerate(palavras):
     #   if letra == chute:
      #      forca[index] = chute

    #if '_' not in forca:
     #   ganhou = True

#if ganhou:
 #   print('You win!')
#else:
 #   print('Game over!')
#print_forca(forca)

#ex12
#numero = int(input('Telefone: '))
#novoNumero = ''
#if len(str(numero)) < 8:
 #   diferenca = 8 - len(str(numero))
  #  novoNumero = '3' * diferenca

#numeroFormatado = novoNumero + str(numero)
#numeroFormatado = numeroFormatado[0:4] + '-' + numeroFormatado[4:]

#print('Telefone possui %d dígitos. Vou acrescentar o digito três na frente.' % len(str(numero)))
#print('Telefone corrigido sem formatação: %d' % numero)
#print('Telefone corrigido com formatação: %s' % numeroFormatado)

#ex13
#ex14