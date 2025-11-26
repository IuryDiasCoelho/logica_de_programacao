soma_idade=0
contador=0
while True:

    idade = int(input("digite a proxima idade, ou digite 0 para sair: "))
    if idade == 0:
        break
    soma_idade+=idade
    contador+=1
    print("idade do grupo",soma_idade)
    print("quantidade de pessoas",contador)
    print("media das idades do grupo",soma_idade/contador)


