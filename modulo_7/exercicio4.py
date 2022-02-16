def maior_idade(info):
    if(type(info)==tuple):
        nome, idade = info
        if(idade>=18):
            return "Maior de idade"
        else:
            return "Menor de idade"
    else:
        for item in info.items():
            if(item[1]>=18):
                return "Maior de idade"
            else:
                return "Menor de idade"
                
print(maior_idade(("Angela",15)))
print(maior_idade({"Lucas":18}))