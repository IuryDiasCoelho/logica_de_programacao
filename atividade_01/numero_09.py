valor_compra=float(input('Digite o valor da compra: '))
if valor_compra>=200:
    if valor_compra>=500:
        print('frete gratis e brinde')
    else:
        print('frete gratis')
else:
    if valor_compra<=50:
        print('O valor do frete e de R$20')
    else:
        print('O valor do frete e de R$10')