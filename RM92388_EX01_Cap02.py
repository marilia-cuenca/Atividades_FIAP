"""O projeto HealthTrack é o máximo e tem grande possibilidade de impactar positivamente a vida das pessoas.
Mesmo que a solução final não utilize uma implementação em Python, podemos aproveitar a oportunidade para desenvolver o algoritmo que resolva um problema simples:
o cálculo do IMC sem distinção de sexo biológico. Por isso, você deve desenvolver um script que solicite o PESO e a ALTURA de uma pessoa. 
A partir disso, o script deva calcular o IMC (PESO dividido pelo quadrado da ALTURA) e informar em quais das faixas a pessoa se encontra, de acordo com uma tabela."""

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
