"""
for i in range (10,0,-2):
    print(i)"""

incio,fim,intervalo=(int(input("digite um numero inteiro para inicio da contagem: ")),
                     int(input("digite um numero inteiro para fim da contagem: ")),
                     int(input("digite um numero inteiro para intervalo da contagem: ")))
#stop sempra para um antes , adicionar variavel +1

for contador in range(incio,fim,intervalo):
    print(contador,end='.')

