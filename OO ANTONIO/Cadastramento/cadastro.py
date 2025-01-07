import json


class Usuario:
    def __init__(self, nome, email, idade):
        self._nome = nome
        self._email = email
        self._idade = idade

    def to_dict(self):
        return {
            "nome": self._nome,
            "email": self._email,
            "idade": self._idade
        }

    @staticmethod
    def from_dict(d):
        return Usuario(d["nome"], d["email"], d["idade"])


    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome

    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email

    def get_idade(self):
        return self._idade
    
    def set_idade(self, idade):
        self._idade = idade

    def exibir_dados(self):
        print(f"Usuário: {self.get_nome()}, {self.get_email()}, {self.get_idade()}")


class Admin(Usuario):
    def __init__(self, nome, email, idade, permissao_adicional):
        super().__init__(nome, email, idade)
        self.permissao_adicional = permissao_adicional

    def to_dict(self):
        dados_usuario = super().to_dict()
        dados_usuario["permissao_adicional"] = self.permissao_adicional
        return dados_usuario

    def excluir_usuario(self, usuario, usuarios):
        usuarios.remove(usuario)
        print(f"Usuário {usuario.get_nome()} excluído com sucesso.")

 
    def exibir_dados(self):
        print(f"Administrador: {self.get_nome()}, {self.get_email()}, {self.get_idade()}, Permissão: {self.permissao_adicional}")


class UsuarioComum(Usuario):
    def __init__(self, nome, email, idade):
        super().__init__(nome, email, idade)

   
    def exibir_dados(self):
        print(f"Usuário Comum: {self.get_nome()}, {self.get_email()}, {self.get_idade()}")


def carregar_usuarios():
    try:
        with open('usuarios.json', 'r') as f:
            usuarios = json.load(f)
            return [Usuario.from_dict(u) for u in usuarios]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_usuarios(usuarios):
    with open('usuarios.json', 'w') as f:
        json.dump([u.to_dict() for u in usuarios], f, indent=4)

def cadastrar_usuario(usuarios):
    tipo_usuario = input("Digite o tipo de usuário (comum/admin): ").strip().lower()
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    
    if tipo_usuario == "admin":
        permissao_adicional = input("Digite a permissão adicional do administrador: ")
        novo_usuario = Admin(nome, email, idade, permissao_adicional)
    else:
        novo_usuario = UsuarioComum(nome, email, idade)
    
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    print(f"Usuário {nome} cadastrado com sucesso!")

def listar_usuarios(usuarios):
    if usuarios:
        for usuario in usuarios:
            usuario.exibir_dados()
    else:
        print("Nenhum usuário cadastrado.")

def buscar_usuario(usuarios):
    nome_busca = input("Digite o nome do usuário a ser buscado: ")
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario.get_nome().lower() == nome_busca.lower():
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        usuario_encontrado.exibir_dados()
    else:
        print("Usuário não encontrado.")

def excluir_usuario(usuarios):
    nome_excluir = input("Digite o nome do usuário a ser excluído: ")
    usuario_para_excluir = None
    for usuario in usuarios:
        if usuario.get_nome().lower() == nome_excluir.lower():
            usuario_para_excluir = usuario
            break

    if usuario_para_excluir:
        usuarios.remove(usuario_para_excluir)
        salvar_usuarios(usuarios)
        print(f"Usuário {nome_excluir} excluído com sucesso.")
    else:
        print("Usuário não encontrado.")


def menu():
    usuarios = carregar_usuarios()

    while True:
        print("\nMenu de opções:")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Buscar usuário")
        print("4. Excluir usuário")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_usuario(usuarios)
        elif opcao == '2':
            listar_usuarios(usuarios)
        elif opcao == '3':
            buscar_usuario(usuarios)
        elif opcao == '4':
            excluir_usuario(usuarios)
        elif opcao == '5':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
