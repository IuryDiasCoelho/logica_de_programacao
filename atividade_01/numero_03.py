notas1=float(input("Digite a nota das diciplinas do 1° bimestre para verificar se foi aprovado: "))
notas2=float(input("Digite a nota das diciplinas do 2° bimestre para verificar se foi aprovado: "))
notas3=float(input("Digite a nota das diciplinas do 3° bimestre para verificar se foi aprovado: "))
notas4=float(input("Digite a nota das diciplinas do 4° bimestre para verificar se foi aprovado: "))
media=(notas1+notas2+notas3+notas4)/4
if media>=6:
    print('Aprovado')
elif media>=5:
    print('Recuperação')
else:
    print('Reprovado')