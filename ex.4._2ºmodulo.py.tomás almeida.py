def CalcularResultados(a, b):
    soma = a + b
    produto = a * b
    return soma, produto


# Programa principal
numero1 = int(input("Introduza o primeiro número: "))
numero2 = int(input("Introduza o segundo número: "))

soma, produto = CalcularResultados(numero1, numero2)

print("Soma:", soma)
print("Produto:", produto)


#Tomás Almeida