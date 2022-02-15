flag = True
lista = []
while(flag):
    numero = int(input("Digite um numero inteiro\n"))
    if(numero<0):
        break
    else:
        lista.append(numero)

print(lista)