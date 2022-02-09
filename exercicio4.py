valor_de_compra = float(input())
valor_do_frete = float(input())
cadastro_fidelidade = (input())

cupom = valor_de_compra + valor_do_frete > 100 or cadastro_fidelidade == 's'
print(cupom)
