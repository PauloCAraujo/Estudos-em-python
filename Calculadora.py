
print('''
        Digite a operação desejada...
        (+) -> Adição
        (-) -> Subtração
        (*) -> Multiplicação
        (/) -> Divisão
        <--- Digite 0 para sair o resultado ou finalizar a operação-->
''')



sinais = input('')
sinal = ''

while True:
   numero = float(input('Digite um numero... '))
   numero_2 = float(input('Digite o segundo... '))


   if input('Deseja continuar [S/N]? ').upper() == 'N':
       break

operacao = 0
if sinais == '+':
   sinal = '+'
   operacao = numero + numero_2

elif sinais == '-':
   sinal = '-'
   operacao = numero - numero_2

elif sinais == '*':
   sinal = '*'
   operacao = numero * numero_2

elif sinais == '/':
    sinal = '/'
    operacao = numero / numero_2

else:
   print('Sinal inválido')

print(f'{numero:1.0f} {sinal:} {numero_2:1.0f} = {operacao:1.2f}')



