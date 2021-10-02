peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/(altura * altura)

if imc < 16.00:
    print("Seu IMC é de {:.2f} e está na categoria 'Baixo Peso Grau III'.".format(imc))
elif imc >= 16.00 and imc <= 16.99:
    print("Seu IMC é de {:.2f} e está na categoria 'Baixo Peso Grau II'.".format(imc))
elif imc >= 17.00 and imc <= 18.49:
    print("Seu IMC é de {:.2f} e está na categoria 'Baixo Peso Grau I'.".format(imc))
elif imc >= 18.50 and imc <= 24.99:
    print("Seu IMC é de {:.2f} e está na categoria 'Peso Ideal'.".format(imc))
elif imc >= 25.00 and imc <= 29.99:
    print("Seu IMC é de {:.2f} e está na categoria 'Sobrepeso'.".format(imc))
elif imc >= 30.00 and imc <= 34.99:
    print("Seu IMC é de {:.2f} e está na categoria 'Obesidade Grau I'.".format(imc))
elif imc >= 35.00 and imc <= 39.99:
    print("Seu IMC é de {:.2f} e está na categoria 'Obesidade Grau II'.".format(imc))
elif imc >= 40.00:
    print("Seu IMC é de {:.2f} e está na categoria 'Obesidade Grau III'.".format(imc))
