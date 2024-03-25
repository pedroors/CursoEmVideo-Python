preco = float(input("Qual é o preço do produto? R$"))
novo = preco - (preco * 5 / 100)

print("O produto que custava R${}, na promoção com desconto de 5% irá passar a custar R${}".format(preco, novo))