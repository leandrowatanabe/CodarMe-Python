str = input("Digite uma string\n")
letras = set()
dict = {}

for char in str:
    letras.add(char)

count = 0
for letra in letras:
    for char in str:
        if letra == char:
            count += 1
    dict.update({letra : count})
    count = 0

print(dict)