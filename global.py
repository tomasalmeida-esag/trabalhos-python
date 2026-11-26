opcao = ""
while opcao != "0"
    print("\n======= MENU PRINCIPAL =======")
    print("1 - Classificação")
    print("2- Matemática")
    print("0 - Sair")
    opcao = input("escolha uma opção: ")

    if opcao =="1"
        apresentar_classificaçoes(notas)
    elif opcao == "2"
        executar_matematica()

