"""Hora de decidir! Os colaboradores da sua equipe foram sorteados para ganharem um console de última geração cada um por conta do bom desempenho que tiveram nos últimos projetos. Por uma questão de logística, porém, a empresa pede que todos os 5 membros da equipe recebam o mesmo aparelho.

Crie um algoritmo onde o usuário possa digitar o voto de cada um dos 5 membros da equipe e, ao final, exiba qual foi o console escolhido e com quantos votos.

As opções são: PLAYSTATION, XBOX e NINTENDO."""

voto1 = int(input("Digite o 1º voto \n[1]-Playstation; [2]-XBOX; [3]-Nintendo: "))
voto2 = int(input("Digite o 2º voto \n[1]-Playstation; [2]-XBOX; [3]-Nintendo: "))
voto3 = int(input("Digite o 3º voto \n[1]-Playstation; [2]-XBOX; [3]-Nintendo: "))
voto4 = int(input("Digite o 4º voto \n[1]-Playstation; [2]-XBOX; [3]-Nintendo: "))
voto5 = int(input("Digite o 5º voto \n[1]-Playstation; [2]-XBOX; [3]-Nintendo: "))

playstation = 0
xbox = 0
nintendo = 0

if voto1 == 1 or voto1 == 2 or voto1 == 3:
    if voto1 == 1:
        playstation += 1
    elif voto1 == 2:
        xbox += 1
    elif voto1 == 3:
        nintendo += 1
if voto2 == 1 or voto2 == 2 or voto2 == 3:
    if voto2 == 1:
        playstation += 1
    elif voto2 == 2:
        xbox += 1
    elif voto2 == 3:
        nintendo += 1      
if voto3 == 1 or voto3 == 2 or voto3 == 3:
    if voto3 == 1:
        playstation += 1
    elif voto3 == 2:
        xbox += 1
    elif voto3 == 3:
        nintendo += 1   
if voto4 == 1 or voto4 == 2 or voto4 == 3:
    if voto4 == 1:
        playstation += 1
    elif voto4 == 2:
        xbox += 1
    elif voto4 == 3:
        nintendo += 1   
if voto5 == 1 or voto5== 2 or voto5 == 3:
    if voto5 == 1:
        playstation += 1
    elif voto5 == 2:
        xbox += 1
    elif voto5 == 3:
        nintendo += 1                             

print("\nA quantidade de votos foi:")
print("Playstation: {} voto(s)".format(playstation))
print("XBOX: {} voto(s)".format(xbox))
print("Nintendo: {} voto(s)".format(nintendo))

if playstation > xbox and playstation > nintendo:
    print("\nO console escolhido é o Playstation.")
elif xbox > playstation and xbox > nintendo:
    print("\nO console escolhido é o XBOX.")
elif nintendo > playstation and nintendo > xbox:
    print("\nO console escolhido é o Nintendo.") 
else:
    print("Deu empate. Faça a votação novamente.")
