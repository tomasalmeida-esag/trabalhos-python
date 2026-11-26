positivas = 0

for aluno in range(1, 9):
    nota = float(input(f"Nota do aluno {aluno}: "))

    if nota >= 10:
        positivas += 1

print("Número de classificações positivas:", positivas)