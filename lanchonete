

pedidos = []

while True:
    print('\nCARDÁPIO')
    print('CÓDIGO       PRODUTO              VALOR')
    print('[ 100 ]      Cachorro-Quente      R$ 5,00')
    print('[ 101 ]      Cheeseburguer        R$ 8,30')
    print('[ 102 ]      Refrigerante         R$ 3,50')

    codigo = input('Qual a opção? ')
    quantidade = int(input('Quantas unidades? '))

    pedidos.append({'codigo': codigo, 'quantidade': quantidade})

    continua = input('Deseja adicionar outro produto?[S/N] ')

    if continua.upper() == 'N':
        break

valor_total_pedido = 0

print('\nCÓDIGO   PRODUTO            QUANTIDADE     VALOR UN.      VALOR TOTAL')

for pedido in pedidos:
    codigo = pedido["codigo"]
    quantidade = pedido["quantidade"]

    if codigo == '100':
        valor_un = 5
        valor_total = valor_un * quantidade
        valor_total_pedido += valor_total
        print(
            f'100      Cachorro-Quente    {quantidade}              R$ {valor_un:1.2f}        R$ {valor_total:1.2f}')

    if codigo == '101':
        valor_un = 8.3
        valor_total = valor_un * quantidade
        valor_total_pedido += valor_total
        print(
            f'101      Cheeseburguer      {quantidade}              R$ {valor_un:1.2f}        R$ {valor_total:1.2f}')

    if codigo == '102':
        valor_un = 3.5
        valor_total = valor_un * quantidade
        valor_total_pedido += valor_total
        print(
            f'101      Refrigerante       {quantidade}              R$ {valor_un:1.2f}        R$ {valor_total:1.2f}')

print(
    f'\nVALOR TOTAL DO PEDIDO                                     R$ {valor_total_pedido:1.2f}')




