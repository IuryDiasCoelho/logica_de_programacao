nomes=["joao","maria","jose","junio","weslei","wanessa"]
print(nomes)
excluir=int(input("digite um numero de posição (indice) para excluir um nome: "))

del nomes[excluir]
print(nomes)