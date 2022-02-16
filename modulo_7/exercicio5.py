def detecta(lista, elemento):
    qtd = len(lista) - 1 
    index = 0
    
    while(index < qtd):
        if(lista[index] == elemento):
            return True
        index+=1
        
    return False

print(detecta([1,2,3,4,5,6,8,0],1))

print(detecta([1,2,3,4,5,6,8,0],10))