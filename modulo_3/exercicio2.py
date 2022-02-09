valor_compras       = int(input())
desconto            = float(input())
quantidade_itens    = int(input())

valor_final = valor_compras*(1-desconto)
custo_medio = valor_compras/quantidade_itens

print("Valor final: ", valor_final)
print("Valor medio: ", custo_medio)