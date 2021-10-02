"""O projeto HealthTrack é o máximo e tem grande possibilidade de impactar positivamente a vida das pessoas.
Mesmo que a solução final não utilize uma implementação em Python, podemos aproveitar a oportunidade para desenvolver o algoritmo que resolva
um problema simples: verificar se os batimentos cardíacos por minuto se encontram na faixa adequada. Para isso, você deve solicitar que o usuário informe
o seu número de BATIMENTOS POR MINUTO (BPM) e a IDADE. A partir disso o script deva verificar e exibir uma mensagem informando se os batimentos
do usuário encontram-se DENTRO da faixa adequada, ACIMA da faixa adequada ou ABAIXO da faixa adequada)"""

bpm = int(input("Informe os batimentos por minuto (bpm): "))
idade = int(input("Informe a idade: "))

if idade <= 2 and 120 <= bpm <= 140:
    print("Os batimentos estão dentro do normal.")
elif idade <= 2 and bpm < 120:
    print("Os batimentos estão ABAIXO do normal. Consulte um médico.")
elif idade <= 2 and bpm > 140:
    print("Os batimentos estão ACIMA do normal. Consulte um médico.")
elif idade >= 3 and idade <= 7 and bpm >= 60 and bpm <= 120:
    print("Os batimentos estão dentro do normal.")
elif idade >= 3 and idade <= 7 and bpm < 60:
    print("Os batimentos estão ABAIXO do normal. Consulte um médico.")
elif idade >= 3 and idade <= 7 and bpm > 120:
    print("Os batimentos estão ACIMA do normal. Consulte um médico.")
elif idade >= 8 and idade <= 17 and bpm >= 80 and bpm <= 100:
    print("Os batimentos estão dentro do normal.")
elif idade >= 8 and idade <= 17 and bpm < 80:
    print("Os batimentos estão ABAIXO do normal. Consulte um médico.")
elif idade >= 8 and idade <= 17 and bpm > 100:
    print("Os batimentos estão ACIMA do normal. Consulte um médico.")
elif idade >= 18 and idade <= 65 and bpm >= 70 and bpm <= 80:
    print("Os batimentos estão dentro do normal.")
elif idade >= 18 and idade <= 65 and bpm < 70:
    print("Os batimentos estão ABAIXO do normal. Consulte um médico.")
elif idade >= 18 and idade <= 65 and bpm > 80:
    print("Os batimentos estão ACIMA do normal. Consulte um médico.")
elif idade >= 66 and bpm >= 50 and bpm <= 60:
    print("Os batimentos estão dentro do normal.")
elif idade >= 66 and bpm < 50:
    print("Os batimentos estão ABAIXO do normal. Consulte um médico.")
elif idade >= 66 and bpm > 60:
    print("Os batimentos estão ACIMA do normal. Consulte um médico.")
