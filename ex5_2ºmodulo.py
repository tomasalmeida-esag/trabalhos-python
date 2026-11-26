import os
os.system("cls") # limpar o ecrã


def contar_positivas(notas):
    return sum(1 for nota in notas if nota >= 10)


def contar_bons(notas):
    return sum(1 for nota in notas if 14 <= nota < 18)


def contar_excelentes(notas):
    return sum(1 for nota in notas if 18 <= nota <= 20)


def mostrar_relatorio(notas):
    print("----------------------------------------------:",)
    print("Lista das classificações:", notas)
    print(f"A maior classificação é: {max(notas)}")
    print(f"A menor classificação é: {min(notas)}")

    print(f"Número de classificações positivas: {contar_positivas(notas)}")
    print(f"Número de classificações negativas: {len(notas) - contar_positivas(notas)}")
    print(f"Número de alunos com classificação Bom: {contar_bons(notas)}")
    print(f"Número de alunos com classificação Excelente: {contar_excelentes(notas)}")


# Programa principal

notas = []

# Ler as classificações dos 10 alunos
for i in range(10):
    nota = float(input(f"Introduza a classificação do aluno {i + 1}: "))

    while nota < 0 or nota > 20:
        print("Classificação inválida! Introduza uma nota entre 0 e 20.")
        nota = float(input(f"Introduza novamente a classificação do aluno {i + 1}: "))

    notas.append(nota)

# Apresentar o relatório
mostrar_relatorio(notas)

# Identificação do trabalho
print("\nTrabalho realizado por: Tomás Almeida - Nº 27")