from opcoes import add_contact


def listar_dados(nome, celular, email):
    print(f"Nome: {nome}\nCelular: {celular}\nEmail: {email}")


def listar(agenda):  # Função para mostrar lista de contatos.
    add_contact.print_line(char='-')
    print("CONTATOS DA AGENDA")
    add_contact.print_line(char='-')
    for e in agenda:
        print("")
        listar_dados(e[0], e[1], e[2])
        print("")
    add_contact.print_line(char='-')
    print("FIM DA AGENDA")
    add_contact.print_line(char='-')
    return agenda
