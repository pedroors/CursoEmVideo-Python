real = float(input("Quanto de dinheiro que você tem na carteira? "))
dolar = real / 5.03
print("Com R${}, você pode comprar U${:.2f}".format(real, dolar))