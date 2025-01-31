from opcoes import add_contact, src_contact


def editar_contato(agenda):
    if not agenda:  # Verifica se a agenda está vazia
        print("Não há contatos para editar.")
        return agenda
    while True:
        add_contact.print_line(char='-')
        print("Pesquise o  contato:")
        add_contact.print_line(char='-')
        p = src_contact.pesquisa(add_contact.p_nome(), agenda)  # Passando a agenda como argumento
        if p is not None:
            nome = agenda[p][0]
            print("Nome: ", nome)
            celular = input("Celular: ")
            email = input("E-mail: ")
            print("")
            agenda[p] = [nome, celular, email]  # Atualizando o contato na agenda
            add_contact.print_line(char='-')
            print("Registro editado com Sucesso!")
            add_contact.print_line(char='-')
            return agenda  # Retornando a agenda atualizada
        else:
            print("Nome não encontrado.")
