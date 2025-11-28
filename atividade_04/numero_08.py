numero=float(input("Digite um numero real para saber se é positivo ou negativo par ou impar: "))

if numero%2==0 and numero>=0:
    print('O número',numero,'é positivo e par')
elif numero%2==0 and numero<0:
    print('O npumero',numero,'é negativo e par')
elif numero%2==1 and numero>0:
    print('O número',numero,'e positivo e impar')
else:
    print('O numero',numero,'e negativo e impar')