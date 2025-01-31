from opcoes import add_contact, src_contact


def deletar_contato(agenda):
    if not agenda:  # Verifica se a agenda está vazia
        print("Não há contatos para deletar.")
        return agenda
    while True:
        nome = add_contact.p_nome()
        # retorna o índice do nome ou vazio
        p = src_contact.pesquisa(nome, agenda)
        if p is not None:  # Se encontrou o contato
            del agenda[p]  # exclui o contato
            add_contact.print_line(char='-')
            print("Registro APAGADO com Sucesso!")
            add_contact.print_line(char='-')
            return agenda
        else:
            # não encontrou o registro para excluir
            print("Nome não encontrado.")
