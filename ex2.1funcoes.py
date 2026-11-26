def CalcularPrecoFinal(preco, desconto):
    valor_desconto = preco * desconto / 100
    preco_final = preco - valor_desconto
    return preco_final


# Programa principal
preco = float(input("Introduza o preço do produto: "))
desconto = float(input("Introduza a percentagem de desconto: "))

preco_final = CalcularPrecoFinal(preco, desconto)

print("O preço final do produto é:", round(preco_final, 2), "€")

# tomás almeida