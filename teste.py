import abc

# Definição das interfaces e classes de usuario

class IUsuario(abc.ABC):
    def __init__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha

    @abc.abstractmethod
    def autenticacao(self, senha):
        pass

class UsuarioPrimario(IUsuario):
    def __init__(self, nome, cpf, senha) -> None:
        super().__init__(nome, cpf, senha)
        
    def autenticacao(self, senha):
        if self._senha == senha:
            return True, 'Login realizado com sucesso!'
        else:
            return False, 'Dados incorretos!'

class UsuarioSecundario(IUsuario):
    def __init__(self, nome, cpf, senha=None) -> None:
        super().__init__(nome, cpf, senha)

class ControleAutenticacao():
    def __init__(self):
        pass

    def autenticacao(self, usuario, senha):
        if isinstance(usuario, IUsuario):
            return usuario.autenticacao(senha)
        else:
            return False, 'Usuario informado não tem permissão de login!'

class Dorama:
    def __init__(self, nome, total_eps, nota, emissora):
        self._nome = nome
        self._total_eps = total_eps
        self._nota = nota
        self._emissora = emissora

    def adicionar_doramas(self):
        return {
            'nome': self._nome,
            'total_eps': self._total_eps,
            'nota': self._nota,
            'emissora': self._emissora
        }
    
    def atualizar_doramas(self, nome=None, total_eps=None, nota=None, emissora=None):
        if nome:
            self._nome = nome
        if total_eps:
            self._total_eps = total_eps
        if nota:
            self._nota = nota
        if emissora:
            self._emissora = emissora
        print(f'Dorama {self._nome} atualizado com sucesso!')

    def remover_dorama(self):
        self._nome = None
        self._nota = None
        self._emissora = None
        self._total_eps = None

class Dorama_Favorito(Dorama):
    pass

class Doramas_assistidos(Dorama):
    pass

class Dorama_nao_assistidos(Dorama):
    pass

class GerenciarDoramas():
    def __init__(self):
        self._doramas_favoritos = {}
        self._doramas_assistidos = {}
        self._doramas_nao_assistidos = {}
        self._usuario_atual = None
        # self._controle_autenticacao = ControleAutenticacao()

    def set_usuario_atual(self, usuario):
        self._usuario_atual = usuario

    def adicionar_doramas_favoritos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            nome = input('Nome do dorama: ')
            total_eps = int(input('Total de episodios: '))
            nota = float(input('Nota do dorama: '))
            emissora = input('Emissora do dorama: ')
            if nome in self._doramas_favoritos:
                print(f'Dorama {nome} ja existe na lista de favoritos!')
            else:
                novo_dorama = Dorama_Favorito(nome, total_eps, nota, emissora)
                self._doramas_favoritos[nome] = novo_dorama.adicionar_doramas()
                print(f'Dorama {nome} adicionado aos favoritos.')
        else:
            print('Você não possui permissão para adicionar doramas favoritos!')

    def listar_doramas_favoritos(self):
        for nome, dados in self._doramas_favoritos.items():
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
            print("------")

    def remover_doramas_favoritos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            dorama_nome = input('Dorama que você deseja remover: ')
            if dorama_nome in self._doramas_favoritos:
                del self._doramas_favoritos[dorama_nome]
                print('Dorama removido com sucesso!\n')
            else:
                print(f'Dorama {dorama_nome} não encontrada!\n')
        else:
            print('Você não possui permissão para remover doramas!')

    def atualizar_doramas_favoritos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            nome = input('Informe o dorama que deseja atualizar: ')
            if nome in self._doramas_favoritos:
                op = input('Informe o que deseja atualizar: ')
                print('1 - atualizar nome:')
                print('2 - atualizar total de episodios:')
                print('3 - atualizar nota:')
                print('4 - atualizar emissora:')
                dorama = self._doramas_favoritos[nome]
                if op == '1':
                    novo_nome = input('Informe o novo nome do dorama: ')
                    if novo_nome:
                        dorama.atualizar_doramas(nome=novo_nome)
                elif op == '2':
                    novo_total_eps = int(input('Informe o novo total de episodios: '))
                    if novo_total_eps:
                        dorama.atualizar_doramas(total_eps=novo_total_eps)
                elif op == '3':
                    novo_nota = float(input('Informe a nova nota do dorama: '))
                    if novo_nota:
                        dorama.atualizar_doramas(nota=novo_nota)
                elif op == '4':
                    novo_emissora = input('Informe a nova emissora do dorama: ')
                    if novo_emissora:
                        dorama.atualizar_doramas(emissora=novo_emissora)
                else:
                    print('Opção invalida!\n')
        else:
            print('Você não possui permissão para atualizar doramas!')

    def pesquisar_doramas_favoritos(self):
        dorama_pesquisar = input('Informe o nome do dorama que deseja pesquisar: ')
        if dorama_pesquisar in self._doramas_favoritos:
            dados = self._doramas_favoritos[dorama_pesquisar]
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
            print("------")
        else:
            print(f'Dorama {dorama_pesquisar} não foi encontrada na lista!')

    # Implementação similar para doramas assistidos e não assistidos

    def exibir_menu(self):
        while True:
            print("\nMenu:")
            print("1. Adicionar doramas favoritos")
            print("2. Listar doramas favoritos")
            print("3. Remover dorama favorito")
            print("4. Pesquisar doramas favoritos")
            print("5. Adicionar doramas assistidos")
            print("6. Listar doramas assistidos")
            print("7. Remover dorama assistido")
            print("8. Pesquisar doramas assistidos")
            print("9. Adicionar doramas não assistidos")
            print("10. Listar doramas não assistidos")
            print("11. Remover dorama não assistido")
            print("12. Pesquisar doramas não assistidos")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                self.adicionar_doramas_favoritos()
            elif opcao == '2':
                self.listar_doramas_favoritos()
            elif opcao == '3':
                self.remover_doramas_favoritos()
            elif opcao == '4':
                self.pesquisar_doramas_favoritos()
            elif opcao == '5':
                self.adicionar_doramas_assistidos()
            elif opcao == '6':
                self.listar_doramas_assistidos()
            elif opcao == '7':
                self.remover_doramas_assistidos()
            elif opcao == '8':
                self.pesquisar_doramas_assistidos()
            elif opcao == '9':
                self.adicionar_doramas_nao_assistidos()
            elif opcao == '10':
                self.listar_doramas_nao_assistidos()
            elif opcao == '11':
                self.remover_doramas_nao_assistidos()
            elif opcao == '12':
                self.pesquisar_doramas_nao_assistidos()
            elif opcao == '0':
                print('Programa encerrado.')
                break
            else:
                print("Opção invalida. Tente novamente.")

# Classe para gerenciar o sistema de cadastro e login

class Sistema:
    def __init__(self):
        self._usuarios = {}  # Dicionario para armazenar os usuarios
        self.gerenciar_doramas = GerenciarDoramas()  # Instância do gerenciador de doramas
        self.usuario_atual = None  # Usuario atualmente logado

    def cadastrar_usuario(self):
        usuario_nome = input('Nome do usuario: ')
        usuario_cpf = input('CPF do usuario: ')
        usuario_senha = input('Senha do usuario: ')
        if usuario_cpf in self._usuarios:
            print('Usuario ja cadastrado!\n')
        else:
            tipo = input('Tipo de usuario (primario/secundario): ')
            if tipo == 'primario':
                self.usuarios[usuario_nome] = UsuarioPrimario(usuario_nome, usuario_cpf, usuario_senha)
            elif tipo == 'secundario':
                self.usuarios[usuario_nome] = UsuarioSecundario(usuario_nome, usuario_cpf, usuario_senha)
            else:
                print('Tipo de usuario invalido!\n')

    def login(self):
        usuario_nome = input('Nome do usuario: ')
        usuario_senha = input('Senha do usuario: ')
        if usuario_nome in self.usuarios:
            usuario = self.usuarios[usuario_nome]
            autenticado, mensagem = usuario.autenticacao(usuario_senha)
            if autenticado:
                self.usuario_atual = usuario
                self.gerenciar_doramas.set_usuario_atual(usuario)
                print(mensagem)
                self.gerenciar_doramas.exibir_menu()
            else:
                print(mensagem)
        else:
            print('Usuario não encontrado!\n')

    def menu(self):
        while True:
            print("Menu Principal:")
            print("1 - Cadastrar usuario")
            print("2 - Login")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                self.cadastrar_usuario()
            elif opcao == '2':
                self.login()
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("Opção invalida. Tente novamente.")

if __name__ == "__main__":
    sistema = Sistema()
    sistema.menu()
