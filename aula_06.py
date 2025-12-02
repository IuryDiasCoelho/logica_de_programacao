#estrutura de listas
frutas=["maçã","banana","uva"]
numeros=[10,20,30,40,50]
vazia=[]

print(frutas,numeros,vazia)
print(frutas[0])
print(len(frutas))

#adicionando itens usando a posição
frutas[0]="acabate"
print(frutas)

#sort modificando ordem da lista apenas visualização
frutas1=["acabate","banana","maça","pera","uva","morango","laranja"]
frutas1.sort()
print(frutas1)

#sorted cria uma nova lista definitiva
legumes=["cenoura","vagem","ervilha","cebola"]
legumes_ordenados= sorted(legumes)
print(legumes_ordenados)
# reverse=True e pra colocar em ordem decrecente


#adicionar elemento lista append
frutas1=["acabate","banana","maça","pera","uva","morango","laranja"]
frutas1.append("melao")
print(frutas1)

# adicionar com .insert
frutas1=["acabate","banana","maça","pera","uva","morango","laranja"]
frutas1.insert(0,"amora")
print(frutas1)

# remover itens da lista .remove
frutas1=["acabate","banana","maça","pera","uva","morango","laranja"]
frutas1.remove("uva")
print(frutas1)

#removendo usando posição especifica
frutas1=["acabate","banana","maça","pera","uva","morango","laranja"]
del frutas1[0]
print(frutas1)

#usando maximo e minimo lista
frutas1=["acabate","banana","maça","pera","uva","morango","laranja"]
maior_frutas1=max(frutas1)
print(maior_frutas1)

numeros=[10,20,30,40,50]
numero_maximo=max(numeros)
print(numero_maximo)
#ou
print(min(numeros))