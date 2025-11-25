preco_desconto=float(input("Digite o preço do produto para saber quanto será o valor final: "))
desconto=0.95
if preco_desconto>=100:
    print('O valor final é R$',preco_desconto*desconto,)
else:
    print("O valor final será R$",preco_desconto,"infelismente não conseguimos desconto nesse valor")