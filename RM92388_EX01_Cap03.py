"""O projeto HealthTrack está tomando forma e podemos pensar em algoritmos que possam ser reaproveitados quando estivermos implementando o front e o back do nosso sistema. Uma das funções mais procuradas por usuários de aplicativos de saúde é o de controle de calorias ingeridas em um dia. Por essa razão, você deve elaborar um algoritmo implementado em Python em que o usuário informe quantos alimentos consumiu naquele dia e depois possa informar o número de calorias de cada um dos alimentos. Como não estudamos listas nesse capítulo você não deve se preocupar em armazenar todas as calorias digitadas, mas deve exibir o total de calorias no final."""

alimentos = int(input("Quantos alimentos você ingeriu hoje? "))

calorias_totais = 0

for x in range(0, alimentos):
    calorias = int(input("Informe a quantidade de calorias de cada alimento ingerido: "))
    calorias_totais = calorias_totais + calorias
print("\nO total de calorias ingeridas hoje foi de {} kcal.".format(calorias_totais))
