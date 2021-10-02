bruto = float(input("Digite o valor bruto do pacote: R$ "))
categoria = str(input("Digite a categoria dos assentos no vôo: ")).upper()
viajantes = int(input("Digite a quantidade de viajantes: "))

if categoria == 'ECONOMICA' and viajantes == 2:
    desconto = bruto * 0.03
    liquido = bruto - desconto
    media = liquido/viajantes
elif categoria == 'ECONOMICA' and viajantes == 3:
    desconto = bruto * 0.04
    liquido = bruto - desconto
    media = liquido/viajantes
elif categoria == 'ECONOMICA' and viajantes >= 4:
    desconto = bruto * 0.05
    liquido = bruto - desconto
    media = liquido/viajantes
elif categoria == 'EXECUTIVA' and viajantes == 2:
    desconto = bruto * 0.05
    liquido = bruto - desconto
    media = liquido/viajantes
elif categoria == 'EXECUTIVA' and viajantes == 3:
    desconto = bruto * 0.07
    liquido = bruto - desconto
    media = liquido/viajantes
elif categoria == 'EXECUTIVA' and viajantes >= 4:
    desconto = bruto * 0.08
    liquido = bruto - desconto
    media = liquido/viajantes
elif categoria == 'PRIMEIRA CLASSE' and viajantes == 2:
    desconto = bruto * 0.10
    liquido = bruto - desconto
    media = liquido/viajantes
elif categoria == 'PRIMEIRA CLASSE' and viajantes == 3:
    desconto = bruto * 0.15
    liquido = bruto - desconto
    media = liquido/viajantes
elif categoria == 'PRIMEIRA CLASSE' and viajantes >= 4:
    desconto = bruto * 0.20
    liquido = bruto - desconto
    media = liquido/viajantes

print("O valor bruto da viagem é de R$ {:.2f}.".format(bruto))
print("O valor do desconto para {} viajantes na categoria {} é de R$ {:.2f}.".format(viajantes, categoria, desconto))
print("O valor líquido da viagem é de R$ {:.2f}.".format(liquido))
print("O valor médio por viajante é de R$ {:.2f}.".format(media))
