from opcoes import add_contact, edit_contact, src_contact, list_contact, del_contact


def menu():
    agenda = []
    # Exibir o menu e a opção para digitar
    while True:
        print("\nMENU:")
        print("1 - Adicionar novo contato")
        print("2 - Editar um contato")
        print("3 - Pesquisar contato")
        print("4 - Lista de contatos")
        print("5 - Apagar um contato")
        print("6 - Sair")
        opcao_menu = input("Digite uma opção: ")
        print("")

    # Novos campos
        if opcao_menu == str("1"):
            agenda = add_contact.adicionar_contato(agenda)
        elif opcao_menu == str("2"):
            agenda = edit_contact.editar_contato(agenda)
        elif opcao_menu == str("3"):
            agenda = src_contact.pesquisar_contato(agenda)
        elif opcao_menu == str("4"):
            agenda = list_contact.listar(agenda)
        elif opcao_menu == str("5"):
            agenda = del_contact.deletar_contato(agenda)
        elif opcao_menu == str("6"):
            print("Saindo do progra1ma...")
            break  # Isso irá quebrar o loop e terminar o programa
        else:
            print("Opção inválida. Por favor, tente novamente.")


menu()
