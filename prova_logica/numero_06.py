if media>=450 and redacao!=0:
    print("Parabens você foi aprovado no ProUni")
elif media<450 and redacao==0:
    print("Você não esta apto pra se inscrever sua média e sua redação não atingiram os índices minimos")
elif media<450:
    print("Você não esta apto pra se inscrever sua média foi abaixo do minimo exigido de 450 pontos")
elif redacao==0:
    print("Você não esta apto pra se inscrever sua redação teve nota 0")