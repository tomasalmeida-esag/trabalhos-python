classificacoes = []

for i in range(5):
    nota = float(input("Introduza a classificação do aluno: "))
    classificacoes.append(nota)

maior = max(classificacoes)

positivas = 0
negativas = 0

for nota in classificacoes:
    if nota >= 10:
        positivas += 1
    else:
        negativas += 1

print("Classificações:", classificacoes)
print("Maior classificação:", maior)
print("Número de alunos com classificação positiva:", positivas)
print("Número de alunos com classificação negativa:", negativas)