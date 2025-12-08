#questão 1

print("CADASTRO ENEM 2025")
nome,cpf,email,senha=(input("Digite o nome completo: "),input("Digite seu cpf: "),input("Digite seu email: ")
                          ,input("Digite sua senha: "))

#questão 2
email_loguin,senha_loguin=input("Digite sua email de loguin: "),input("Digite sua senha de loguin: ")
while True:
    if email_loguin==email and senha_loguin==senha :
        print("Acesso liberado")
        break
    else:
        print("Dados incorretos.Tente novamente")
        email_loguin, senha_loguin = input("Digite sua email de loguin: "), input("Digite sua senha de loguin: ")

#questão 3

lista_cursos=["Robotica","Desenvolvimento Web e Mobilie","inteligência artificial"]
lista_ordenadas=sorted(lista_cursos)

#questão 4

lista_cursos.append("Engenharia de Software")
lista_ordenadas=sorted(lista_cursos)
print(lista_ordenadas)

#questão 5

linguagens_codigos=int(input("Digite a sua nota de linguagens ,códigos e suas tecnologias: "))
matematica=int(input("Digite a sua nota de matemática e suas tecnologias: "))
ciencias_da_natureza=int(input("Digite a sua nota de ciências da natureza e suas tecnologias: "))
ciencias_humanas=int(input("Digite a sua nota de ciências humanas e suas tecnologias: "))
redacao=int(input("Digite a sua nota de redação: "))
media=(linguagens_codigos+matematica+ciencias_da_natureza+ciencias_humanas+redacao)/5
print("Sua nota de linguagens códigos e suas tecnologias é:",linguagens_codigos,
      "\nSua nota de matemática e suas tecnologias é:",matematica,
      "\nSua nota de ciências da natureza e suas tecnologias é: ",ciencias_da_natureza,
      "\nSua nota de ciências humanas e suas tencnologias é: ",ciencias_humanas,
      "\nSua nota de redação é: ",redacao,
      "\nSua pontuação final é: ",media)

#questão 6

if media>=450 and redacao!=0:
    print("Parabens você foi aprovado no ProUni")
elif media<450 and redacao==0:
    print("Você não esta apto pra se inscrever sua média e sua redação não atingiram os índices minimos")
elif media<450:
    print("Você não esta apto pra se inscrever sua média foi abaixo do minimo exigido de 450 pontos")
elif redacao==0:
    print("Você não esta apto pra se inscrever sua redação teve nota 0")

#questão 7
print("A faculdade UNIASSELVI te oferece bolsa no curso de Engenharia de Software, veja abaixo as condições que você "
      "consegiu de acordo com sua nota")
if media>701:
    print("Parabens sua bolsa te deu um desconto de 100% ,a mensalidade original e de R$1000 reais,"
          " sua mensalidade sera de R$0 reais, sua economia anual foi de R$12 mil reais")
elif media>651:
    print("Parabens sua bolsa te deu um desconto de 50% ,a mensalidade original e de R$1000 reais,"
          " sua mensalidade sera de R$500 reais, sua economia anual foi de R$6 mil reais")
elif media>601:
    print("Parabens sua bolsa te deu um desconto de 40% ,a mensalidade original e de R$1000 reais,"
          " sua mensalidade sera de R$600 reais, sua economia anual foi de R$4800 reais")
elif media>551:
    print("Parabens sua bolsa te deu um desconto de 35% ,a mensalidade original e de R$1000 reais,"
          " sua mensalidade sera de R$650 reais, sua economia anual foi de R$4200 reais")
elif media>451:
    print("Parabens sua bolsa te deu um desconto de 100% ,a mensalidade original e de R$1000 reais,"
          " sua mensalidade sera de R$700 reais, sua economia anual foi de R$3600 reais")
else:
    print(("Parabens sua bolsa te deu um desconto de 100% ,a mensalidade original e de R$1000 reais,"
          " sua mensalidade sera de R$800 reais, sua economia anual foi de R$2400 reais"))