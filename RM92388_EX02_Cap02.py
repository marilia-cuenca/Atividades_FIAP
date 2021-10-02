"""Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.

Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês."""

cliente = str(input("Digite o nome do cliente: "))
assinatura = str(input("Digite o tipo da assinatura: ")).upper()
faturamento = float(input("Digite o faturamento anual: R$ "))

if assinatura == "BASIC":
    bonus = faturamento * 0.30
    print("O valor do bônus que o cliente {} deve pagar é de R$ {:.2f}.".format(cliente, bonus))

elif assinatura == "SILVER":
    bonus = faturamento * 0.20
    print("O valor do bônus que o cliente {} deve pagar é de R$ {:.2f}.".format(cliente, bonus))

elif assinatura == "GOLD":
    bonus = faturamento * 0.10
    print("O valor do bônus que o cliente {} deve pagar é de R$ {:.2f}.".format(cliente, bonus))   

elif assinatura == "PLATINUM":
    bonus = faturamento * 0.05
    print("O valor do bônus que o cliente {} deve pagar é de R$ {:.2f}.".format(cliente, bonus))
