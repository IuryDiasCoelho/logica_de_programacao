'''idade=int(input("digite sua idade: "))

if idade>=18 and idade <150:
    print('Você e maior de idade')

elif idade < 18:
    print('Você e menor de idade')

else:
    print('Voçê provavelmente está morto')

nota=float(input("digite sua nota: "))

if nota==10:
    print("Nota máxima! Parabéns")
elif nota>=7:
    print("Aprovado")
elif nota>=5:
    print("recuperação")
else:
    print("Reprovado")

while True:
    numero = int(input("digite um numero para descobrir se e par ou impar: "))

    if numero%2==1:
        print('Seu número é impar')

    elif numero:
        print('seu número e par')

    else:
        print('Para você o zero e par ou impar')'''


passou_de_ano =input("você passou de ano? (sim/não): ").strip().lower()
passou_no_vestibular=input("você passou no vestibular? (sim/não): ").strip().lower()


if passou_de_ano =="sim":

    if passou_no_vestibular=="sim":
        print("começarei a faculdade no próximo ano")

    else:
        print("vou precisar tentar o vestibular novamente")
else:
    print("preciso estudar mais para passar de ano")