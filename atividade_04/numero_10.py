produtos=0
compra=0
total=0

while True:
    produtos+=1
    compra=float(input('Digite o valor dos produtos,ou digite 0 para sair: '))
    total+=compra
    if compra==0:
        print('voçe comprou',produtos-1,'itens')
        print('Voçe comprou um total de ',total)
        if total>=200:
            print('Compras acima de 200 podem ser parceladas em até 3 vezes')
        elif total>=100:
            print('Compras acima de 100 podem ser parceladas em até 2 vezes')
        elif total>=50:
            print('Compras entre 50 e 100 podem ser pagas via cartão de credito em 1 vez')
        else:
            print('Compras de valor inferior a 50 só poderão ser pagas via débito ou pix')
        break
