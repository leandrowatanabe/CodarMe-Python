from tkinter import W


def fatorial(n):
    index = 1
    numero = 1
    while(index < n):
        numero =n * n-index - 1
        index+=1
    return numero

print(fatorial(0))
print(fatorial(1))
print(fatorial(3))
print(fatorial(2))
print(fatorial(15))