"""Olhando para o mercado de educação infantil, você e sua equipe decidem criar um aplicativo onde as crianças aprendam a controlar os seus gastos. Como forma de validar um protótipo, foi solicitado que você crie um script simples, em que o usuário deve informar QUANTAS TRANSAÇÕES financeiras realizou ao longo de um dia e, na sequência, deve informar o VALOR DE CADA UMA das transações que realizou. Seu programa deverá exibir, ao final, o valor total gasto pelo usuário e também a média do valor de cada transação."""

transacoes = int(input("Informe quantas transações financeiras você realizou hoje: "))

valor_total = 0

for x in range(0,transacoes):
    valor = float(input("Informe o valor de cada transação realizada: R$ "))
    valor_total = valor_total + valor
    media = valor_total/transacoes

print("\nO valor total gasto hoje foi de R$ {:.2f}".format(valor_total))
print("A média do valor de cada transação foi de R$ {:.2f}".format(media))
