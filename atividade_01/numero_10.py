vel=int(input('Informe a velocidade do carro (em km/hr):'))
vel_max=80
execo=vel-vel_max
print(f"você estava a {vel}")
print(f"A velocidade máxima permitida {vel_max}")

if execo>=20:
    print("infração grave 7 pontos")
elif execo>=11:
    print("infração media 4 pontos")
elif execo :
    print("infração leve 3 pontos")
else:
    print("sem multa 0 pontos")
