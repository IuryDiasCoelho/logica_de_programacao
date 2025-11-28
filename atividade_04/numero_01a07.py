"""Atividade prática e teórica de lógica de programação

1)	O IF, ELIF E ELSE tem uma ordem de prioridade a ser executada que e definida pela linguagem sendo ela a primeira a
ser executada a IF a próxima podendo ser a ELIF se tiver essa condição e na sequência e ELSE sendo sempre a última a ser
executada.

2)	O loop WHILE vai ser executado ate que uma das condições estabelecidas seja verdadeira, já o FOR vai ser executando
dentro de um parâmetro passado podendo ser uma sequência de números ou listas.

3)	No loop WHILE ele só vai ser parado de atender uma condição como verdadeira, a condição de parada obriga o loop a
parar mesmo que uma condição não tenha sido atendida.

4)	Em um loop de FOR pode se usar uma condição de parada por escolha do usuário desde que o código seja programado para
isso, um exemplo e usando uma condição IF no código contendo a instrução BREAK

5)	A função do RANGE e dar um início, fim e uma intervalo para que seja percorrido, o START e obrigatório sendo o
primeiro a ser digitado representando de onde o loop começa, o STOP e obrigatório também e representa onde o loop
terminará, o STEP seria o intervalo e o único que e optativo

6)	O contador serve para ver quantas vezes o loop foi realizado, já o acumulador pode ser utilizado para juntar strings
ou para realizar cálculos."""

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


