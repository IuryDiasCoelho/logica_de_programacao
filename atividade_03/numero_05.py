inicio,fim,intervalo=(int(input("inicio:")),
                     int(input("fim:")),
                     int(input("intervalo:")))
soma=0
print("a sequencia é:")
for sequencia in range(inicio,fim,intervalo):
    print(sequencia,end=' ')

    soma+=sequencia
print("\n")

print("soma dos numeros é :",soma,end=' ')