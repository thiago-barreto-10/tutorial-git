print('TABELA DE PREÇOS\n GASOLINA: 2,50 L\n ÁLCOOL:   1,90 L')
print('#' * 20) 
print('SUPER PROMOÇÃO!!!!!!!')
print('ÁLCOOL:\nATÉ 20L DESCONTO DE %3\nACIMA DE 20L DESCONTO DE %5\n')
print('GASOLINA:\nATÉ 20L DESCONTO DE %4\nACIMA DE 20L DESCONTO DE %6\n')

combustivel = input('Digite "g" para Gasolina ou "a" para álcool: ')
litros= int (input('Quantos litros deseja? '))

if combustivel == 'g' and litros <= 20:
   total = litros * (2.50 - ((4/100) * 2.50 ))
   print(f'Valor a pagar R$ {total}')

elif combustivel == 'g' and litros >20:
    total = litros * (2.50 - ((6/100) * 2.50))
    print(f'valor a pagar R$ {total}')

elif combustivel == 'a' and litros <= 20:
    total = litros * (1.90 - ((3/100) * 1.90))
    print(f'Valor a pagar R$ {total}')

elif combustivel == 'a' and litros >20:
    total = litros * (1.90 - ((5/100) * 1.90))
    print(f'valor a pagar R$ {total}')