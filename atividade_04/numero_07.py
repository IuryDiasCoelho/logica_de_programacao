num_a,num_b=int(input("Digite um numero inteiro par: ")),int(input("Digite outro numero inteiro par: "))
media=(num_a+num_b)/2

while True:
    if num_a%2!=0:
        print(int(input("Digite um numero inteiro par: ")))
    elif num_a%2==0:
        break

while True:
    if num_b%2!=0:
        print(int(input("Digite um numero inteiro par: ")))
    elif num_a % 2 == 0:
        break


if num_a%2==0 and num_b%2==0:
    print('A soma dos numeros é',num_a+num_b,'a média dos numeros é',media)


