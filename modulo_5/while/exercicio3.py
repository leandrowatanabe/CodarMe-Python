numero = int(input("Digite um numero inteiro: \n"))
index = 1
primo = 0

while(index<=numero):
    if(numero%index==0):
        primo = primo + 1
    index = index + 1

if(primo==2):
    print("Numero e primo")
else:
    print("Nao e primo")