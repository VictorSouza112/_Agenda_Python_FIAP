def print_line(char='-'):
    print(char * 50)


def adicionar_contato(agenda):
    print_line()
    print("Preencha o novo contato:")
    print_line()
    nome = p_nome()
    celular = input("Celular: ")
    email = input("E-mail: ")
    print("")
    agenda.append([nome, celular, email])  # Adicionando os dados na agenda
    print_line()
    print("Registro gravado com sucesso!")
    print_line()
    return agenda


def p_nome():
    return input("\nNome: ")
