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
