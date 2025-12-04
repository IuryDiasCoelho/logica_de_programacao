numeros=[]
repeticao=1
while repeticao<=5:
    repeticao+=1
    entrada=float(input("digite um numero: "))
    numeros.append(entrada)

print("sua list de numeros é:",numeros)
print("seu numero maior é:  ",max(numeros))
print("seu numero menor é:  ",min(numeros))
print("seu soma dos números é:",sum(numeros))
print("a media dos numeros e ",sum(numeros)/len(numeros))




