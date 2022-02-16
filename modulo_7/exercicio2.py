def maior_numero(lista):
    qtd = len(lista)-1
    iterador = 0
    maior = lista[0]
    indice = 0
    while(iterador < qtd):
        if(lista[iterador] > maior):
            maior = lista[iterador]
            indice = iterador
        iterador+=1

    return {indice:maior}

print(maior_numero([1, 20, 2, 5, 13, 3, 15]))