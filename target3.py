import json

with open("dados.json") as file:
    data = json.load(file)

maior = 0.0
media = 0
zeros = 0

for i in range(29):
    if data[i]["valor"] == 0.0:
        zeros = zeros + 1
        continue

    media = media + data[i]["valor"]

    if data[i]["valor"] > maior:
        maior = data[i]["valor"]

media = media / (30 - zeros)

lista =[]
menor = maior
for i in range(29):
    if data[i]["valor"] == 0.0:
        continue

    if data[i]["valor"] >= media:
        lista.append(data[i]["dia"])

    if data[i]["valor"] < menor:
        menor = data[i]["valor"]

print(f"""
O menor valor faturado foi de R${menor:.4f}
O maior valor fatura foi de R${maior:.4f}
Os dias do mês que obtiveram faturamento maior do que a media foram:""")
print(*lista)
