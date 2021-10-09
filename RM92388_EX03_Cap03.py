"""Uma grande empresa de jogos está querendo tornar seus games mais desafiadores. Por isso ela contratou você para desenvolver um algoritmo que será aplicado futuramente em diversos outros games: o algoritmo da sorte de Fibonnaci.
A ideia dessa empresa, é claro, é fazer com que seja mais difícil os jogadores terem sucesso nas ações que realizam nos games. Por isso o seu algoritmo deverá funcionar da seguinte forma: o usuário deve digitar um valor numérico inteiro e o algoritmo deverá verificar se esse valor encontra-se na sequência de Fibonnaci. Caso o número esteja na sequência, o algoritmo deve exibir a mensagem “Ação bem sucedida!” e, caso não esteja, deve exibir a mensagem “A ação falhou...”."""

print("*"*20)
print("DESAFIO DE FIBONACCI")
print("*"*20)

num = int(input("\nDigite um número... "))

a = 0
b = 1
contador = 0

while a <= num:
    c = a + b
    a = b
    b = c
    contador += 1
    
    if num == a:
        print("Ação bem sucedida!")
        break
        continue

if num != a:
    print("A ação falhou...")
