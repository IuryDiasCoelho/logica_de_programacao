lista_compras = []
while True:
    entrada=input("Digite os itens da sua compra ou digite 0 para parar: ")
    if entrada != "0":
        lista_compras.append(entrada)
    else:
        print("sua lista de compras e :",lista_compras)
        break


