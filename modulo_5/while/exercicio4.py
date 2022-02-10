numero = 5
tentativas = 1

while(tentativas<=3):
    tentativa = int(input("Digite sua tentativa: \n"))
    if(tentativa == numero):
        print("Acertou!!\n")
        break
    else:
        tentativas = tentativas + 1
        print("Errou!!\n")
