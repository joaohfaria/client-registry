import json

def salvar_cliente(clientes):
    with open("clientes.json", "w") as file:
        json.dump(clientes, file, indent=4)

def carregar_clientes():
    try:
        with open("clientes.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return[]

    except json.JSONDecodeError:
        print("Erro: clientes.json nao e um arquivo JSON valido!  ")
        return[]

def perguntas_ao_usuario():
    while True:
        nome = input("Qual o nome do cliente?").strip()

        if not nome:
            print("Por favor digite um nome valido! ")
        else:
            break

    while True:
        telefone = input("Qual o numero do cliente?").strip()

        if not telefone:
            print("Por favor insira um numero de telefone valido! ")
        else:
            break

    while True:    
        cpf = input("Qual o CPF do cliente?").strip()

        if not cpf:
            print("Insira um CPF valido!")
        else:
            break

    return nome, telefone, cpf

def criar_usuario(nome, telefone, cpf):
    novo_cliente = {
        "nome" : nome,
        "telefone" : telefone,
        "cpf" : cpf
    }

    return novo_cliente

clientes = carregar_clientes()

def excluir_cliente(clientes, nome_remover):
    for cliente in clientes:
        if cliente["nome"].lower() == nome_remover.lower():
            clientes.remove(cliente)
            salvar_cliente(clientes)
            return True

    return False

def listar_contatos(clientes):
    if not clientes:
        print("\nNao existem clientes")
        return

    for cliente in clientes:
        print(f"\nnome: {cliente['nome']}")
        print(f"\ntelefone: {cliente['telefone']}")
        print(f"\ncpf: {cliente['cpf']}")

while True:
    print("\n=== Registro De Clientes ===")
    print("1 - Adicionar Cliente")
    print("2 - Listar Contatos")
    print("3 - Busca Por Nome")
    print("4 - Remover Cliente")
    print("5 - Sair")

    opcao_do_menu = input("\nEscolha uma opcao: ").strip()

    match opcao_do_menu:
        case "1":
            nome, telefone, cpf = perguntas_ao_usuario()

            novo_cliente = criar_usuario(nome, telefone, cpf)

            clientes.append(novo_cliente)

            salvar_cliente(clientes)

            print("\nCliente adicionado com sucesso!")

        case "2":
            listar_contatos(clientes)

        case "3":
            
            nome_busca = input("Digite o nome do cliente que deseja buscar: "
                            ).strip().lower()
            
            encontrou = False

            for cliente in clientes:
                if nome_busca in cliente["nome"].lower():
                    print("\nCliente encontrado:")
                    print(f"Nome: {cliente['nome']}")
                    print(f"Telefone: {cliente['telefone']}")
                    print(f"CPF: {cliente['cpf']}")
                    encontrou = True

            if not encontrou:
                print("\nNenhum cliente encontrado.")      

        case "4":
            
            nome_remover = input("Digite o nome do cliente que deseja remover: ").strip()

            encontrou = False

            for cliente in clientes:
                if cliente["nome"].lower() == nome_remover.lower():
                    encontrou = True
                    break

            if not encontrou:
                print(f"\nCliente '{nome_remover}' não encontrado.")
                continue
            
            confirmacao = input(f"Tem certeza que deseja remover o cliente '{nome_remover}'? (s/n): ").strip().lower()

            if confirmacao == 's':
                if excluir_cliente(clientes, nome_remover):
                    print(f"\nCliente '{nome_remover}' removido com sucesso!")
                else:
                    print(f"\nCliente '{nome_remover}' não encontrado.")
            else:
                print("\nOperação de remoção cancelada.")

        case "5":

            print("Fechando...")
            break

        case _:
            print("Opção inválida. Por favor, escolha uma opção válida.")