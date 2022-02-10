numero1 = float(input("Digite o primeiro operando:\n"))
numero2 = float(input("Digite o segundo operando:\n"))
op = input("Digite o operando:\n")

if(op=='+'):
    print("Resultado: ", numero1+numero2)
elif(op=='-'):
    print("Resultado: ", numero1-numero2)
elif(op=='*'):
    print("Resultado: ", numero1*numero2)
elif(op=='/'):
    print("Resultado: ", numero1/numero2)
else:
    print("Operecao invalida")