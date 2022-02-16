def maior_idade(info):
    nome, idade = info
    if(idade>=18):
        return "Maior de idade"
    else:
        return "Menor de idade"

print(maior_idade(("Angela",15)))
print(maior_idade(("Lucas",18)))
print(maior_idade(("Marcos",25)))
print(maior_idade(("Bianca",13)))