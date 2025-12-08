email_loguin,senha_loguin=input("Digite sua email de loguin: "),input("Digite sua senha de loguin: ")
while True:
    if email_loguin==email and senha_loguin==senha :
        print("Acesso liberado")
        break
    else:
        print("Dados incorretos.Tente novamente")
        email_loguin, senha_loguin = input("Digite sua email de loguin: "), input("Digite sua senha de loguin: ")