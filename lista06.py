
#dados do usuários para serem guardados:
#tupla no seguinte formato: (nome, idade, peso, altura)


def cadastrar_membro(qtdUsuarios):
    membros = []
    while qtdUsuarios > 0:
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        peso = float(input("Digite o peso do usuário: "))
        altura = float(input("Digite a altura do usuário: "))
        membros.append((nome, idade, peso, altura))
        qtdUsuarios -= 1
    print("Membros cadastrados com sucesso!\n")
    return membros

