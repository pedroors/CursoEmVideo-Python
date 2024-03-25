km = int(input("Informe a quantidade de quilômetros percorridos com o carro: "))
dias = int(input("Informe a quantidade de dias que passou com o carro: "))
precoKm = km * 0.15
precoDias = dias * 60
precoTotal = precoKm + precoDias

print("-" * 15)
print("Você percorreu {}Km e passou {} dias com ele".format(km, dias))
print("Preço por Km percorridos: {}".format(precoKm))
print("Preço por dias utilizados: {}".format(precoDias))
print("Preço total: {}".format(precoTotal))
print("-" * 15)

