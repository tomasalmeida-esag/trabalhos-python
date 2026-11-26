def CalcularRetangulo(comprimento, largura):
    area = comprimento * largura
    perimetro = 2 * (comprimento + largura)
    return area, perimetro


# Programa principal
comprimento = float(input("Introduza o comprimento do retângulo: "))
largura = float(input("Introduza o largura do retângulo: "))

area, perimetro = CalcularRetangulo(comprimento, largura)

print("Área do retângulo:", area)
print("Perimetro do retângulo:", perimetro)

#Tomás Almeida