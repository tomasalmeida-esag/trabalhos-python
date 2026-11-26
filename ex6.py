import random

numero = random.randint(1,10)

numero_utilizador = input("Escolha um número:")

if numero_utilizador == numero:
        print("Parabéns! Você acertou o número.")
else:
        print("Que pena! Você errou o numero.")

print (f"Número sorteado:{numero}")