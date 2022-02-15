lista = ['banana', 1, 'acabate', True, False, 'arroz', 3]
lista_nova = []
qtd = len(lista)
i=0

while(i<qtd):
    lista_nova.append(lista[(qtd-1)-i])
    i+=1

print(lista)
print(lista_nova)
