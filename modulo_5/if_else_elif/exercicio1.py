numero = int(input("Digite um numero:\n"))
if(numero%3==0):
    if(numero%5==0):
        print("FizzBuzz")
    else:
        print("Fizz")
elif (numero%5==0):
    print("Buzz")