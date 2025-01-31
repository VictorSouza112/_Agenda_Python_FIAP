from opcoes import add_contact, list_contact


def pesquisar_contato(agenda):
    if not agenda:  # Verifica se a agenda está vazia
        print("Não há contatos para pesquisar.")
        return agenda
    while True:
        # pesquisa o nome
        p = pesquisa(add_contact.p_nome(), agenda)
        if p is not None:
            print("Registro encontrado!")
            # atualiza as variáveis se encontrou
            nome = agenda[p][0]
            celular = agenda[p][1]
            email = agenda[p][2]
            # mostra o registro
            list_contact.listar_dados(nome, celular, email)
            return agenda
        else:
            # exibe a mensagem de insucesso na procura do registro
            print("Nome não encontrado!")


def pesquisa(nome, agenda):  # Adicionando a agenda como argumento
    name = nome.lower()
    for d, e in enumerate(agenda):
        if e[0].lower() == name:
            return d
    return agenda
