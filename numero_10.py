vel=input('Informe a velocidade do carro (em km/hr):')
vel_max=80
print(f"você estava a {vel}")
print(f"A velocidade máxima permitida {vel_max}")

if vel>="90":
    print("infração leve 3 pontos")
elif vel>="111":
    print("infração media 4 pontos")
elif vel>="120" :
    print("infração grave 7 pontos")
else:
    print("sem multa 0 pontos")
