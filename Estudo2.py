

#fazer estrutura de repetição pedindo numeros positivos
# se for igual a 0 e numero negativo o programa irá parar e nos dar os dados
# cada contagem ira acrescentar dentro de cada grupo coom os numeros positivos
#ira nos retornar quantos numeros inteiros o usuario digitou e separar por grupos
# imprimir a contagem de acordo com cada grupo de contagem
#caso o usuario digite numero maior que 100 retornara ''invalido'' e repetira a pergunta

primeiro = 0
segundo = 0
terceiro = 0
quarto = 0

while True:
    numeros = int(input('Digite um numero positivo (entre 1 e 100)...'))

    if numeros <= 0:
        break


    if numeros >= 1 and numeros <= 25:
        primeiro += 1

    elif numeros >= 26 and numeros <= 50:
        segundo += 1

    elif numeros >= 51 and numeros <= 75:
        terceiro += 1

    elif numeros >= 76 and numeros <= 100:
        quarto += 1
    else:
        print('Inválido')


print(f'Numeros de 1 a 25: {primeiro}')
print(f'Numeros de 26 a 50: {segundo}')
print(f'Numeros de 51 a 75: {terceiro}')
print(f'Numeros de 76 a 100: {quarto}')
