

'''
Tabela de Juros da divida
parcela   ///    juros
1 ==> 0%   6==> 15%
3 ==> 10%  9==> 20%
12==> 25%
'''
valor_inicial = float(input('Digite o valor da sua divida...'))

juros_1 = valor_inicial * 0
parcela_1 = '1'
valor_total_1 = valor_inicial
valor_parcela_1 = valor_inicial

juros_2 = valor_inicial * 0.1
parcela_2 = '3'
valor_total_2 = valor_inicial + juros_2
valor_parcela_2 = valor_total_2/3

juros_3 = valor_inicial * 0.15
parcela_3 = '6'
valor_total_3 = valor_inicial + juros_3
valor_parcela_3 = valor_total_3/6

juros_4 = valor_inicial * 0.2
parcela_4 = '9'
valor_total_4 = valor_inicial + juros_4
valor_parcela_4 = valor_total_4/9

juros_5 = valor_inicial * 0.25
parcela_5 = '12'
valor_total_5 = valor_inicial + juros_5
valor_parcela_5 = valor_total_5/12


print('VALOR INICIAL DA DIVIDA: R${v:1.2f}'.format(v=valor_inicial))
print('JUROS     VALOR TOTAL   PARCELAS   PARCELA')
print('R${j:1.2f}    R${v:1.2f}     {p}          R${vp:1.2f}'.format(j=juros_1, v=valor_total_1, p=parcela_1, vp=valor_parcela_1))
print('R${a:1.2f}  R${b:1.2f}     {c}          R${d:1.2f}'.format(a=juros_2, b=valor_total_2, c=parcela_2, d=valor_parcela_2))
print('R${a:1.2f}  R${b:1.2f}     {c}          R${d:1.2f}'.format(a=juros_3, b=valor_total_3, c=parcela_3, d=valor_parcela_3))
print('R${a:1.2f}  R${b:1.2f}     {c}          R${d:1.2f}'.format(a=juros_4, b=valor_total_4, c=parcela_4, d=valor_parcela_4))
print('R${a:1.2f}  R${b:1.2f}     {c}         R${d:1.2f}'.format(a=juros_5, b=valor_total_5, c=parcela_5, d=valor_parcela_5))

