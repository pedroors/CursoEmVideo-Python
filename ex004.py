a = input("Digite qualquer coisa: ")

print("O tipo primitivo desse valor é: ", type(a))
print("Ele só possui espaços?", a.isspace())
print("É um número? ", a.isnumeric())
print("Está tudo em minúsculo?", a.islower())
print("Está tudo em maiúsculo?", a.isupper())
print("É alfabético? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())