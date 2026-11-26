
import os
import random

os.system("cls")  # Limpar o ecrã

# Gerar automaticamente as classificações de 10 alunos
notas = []

for i in range(10):
    nota = random.randint(0, 20)
    notas.append(nota)


# Função para calcular a média da turma
def calcular_media(notas):
    return sum(notas) / len(notas)


# Função para contar classificações positivas (>= 10)
def contar_positivas(notas):
    return sum(1 for nota in notas if nota >= 10)


# Função para contar classificações Bom (14 a 17)
def contar_bons(notas):
    return sum(1 for nota in notas if 14 <= nota < 18)


# Função para contar classificações Excelente (18 a 20)
def contar_excelentes(notas):
    return sum(1 for nota in notas if 18 <= nota <= 20)


# Procedimento para apresentar o relatório
def mostrar_relatorio(notas):
    media = calcular_media(notas)
    positivas = contar_positivas(notas)
    negativas = len(notas) - positivas
    bons = contar_bons(notas)
    excelentes = contar_excelentes(notas)

    print("-------------------------")
    print("Lista das classificações:", notas)
    print(f"A média da turma é: {media:.2f}")
    print(f"A maior classificação: {max(notas)}")
    print(f"A menor classificação: {min(notas)}")
    print(f"Número de classificações positivas: {positivas}")
    print(f"Número de classificações negativas: {negativas}")
    print(f"Número de alunos com classificação Bom: {bons}")
    print(f"Número de alunos com classificação Excelente: {excelentes}")


# Apresentar o relatório
mostrar_relatorio(notas)

# Identificação do aluno
print("Trabalho realizado por: [Tomás Almeida] - [27]")