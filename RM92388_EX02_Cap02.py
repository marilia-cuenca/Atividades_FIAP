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
