lista = []
while True:
    fruta = input("digite sua fruta : ")
    posicao = int(input("digite a posição onde sua fruta quer fica na lista: "))
    lista.insert(posicao, fruta)
    finalizar=input("digite 'sim' para finalizar e ver a lista completa,ou digite 'continuar': ")

    if finalizar.lower() == "sim":
        break

print(lista)