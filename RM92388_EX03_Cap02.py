"""Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives.
Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira,
quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido."""

segunda = int(input("Informe a quantidade de votos para segunda-feira: "))
terca = int(input("Informe a quantidade de votos para terça-feira: "))
quarta = int(input("Informe a quantidade de votos para quarta-feira: "))
quinta = int(input("Informe a quantidade de votos para quinta-feira: "))
sexta = int(input("Informe a quantidade de votos para sexta-feira: "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("O dia escolhido é segunda-feira.")

elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("O dia escolhido é terça-feira.")

elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("O dia escolhido é quarta-feira.")

elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("O dia escolhido é quinta-feira.")

elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("O dia escolhido é sexta-feira.")
