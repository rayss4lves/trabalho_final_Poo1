import abc

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

    def autenticacao(self, senha=None):
        return True, 'Login realizado como convidado'

class ControleAutenticacao():
    def __init__(self):
        pass

    def autentica(self, usuario, senha):
        if isinstance(usuario, IUsuario):
            return usuario.autenticacao(senha)
        else:
            return False, 'Usuário informado não tem permissão de login!'

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

    def remover_doramas(self):
        self._nome = None
        self._total_eps = None
        self._nota = None
        self._emissora = None

class Dorama_Favorito(Dorama):
    def __init__(self, nome, total_eps, nota, emissora):
        super().__init__(nome, total_eps, nota, emissora)

class Doramas_assistidos(Dorama):
    def __init__(self, nome, total_eps, nota, emissora):
        super().__init__(nome, total_eps, nota, emissora)

class Dorama_nao_assistidos(Dorama):
    def __init__(self, nome, total_eps, nota, emissora):
        super().__init__(nome, total_eps, nota, emissora)

class GerenciarDoramas():
    def __init__(self):
        self._doramas = {}
        self._doramas_favoritos = {}
        self._doramas_assistidos = {}
        self._doramas_nao_assistidos = {}
        self._usuario_atual = None
        self._controle_autenticacao = ControleAutenticacao()

    def setar_usuario(self):
        nome = input('Informe o seu nome: ')
        cpf = input('Informe o seu cpf: ')
        senha = input('Informe a sua senha: ')
        if senha:
            usuario = UsuarioPrimario(nome, cpf, senha)
        else:
            usuario = UsuarioSecundario(nome, cpf)
        sucesso, mensagem = self._controle_autenticacao.autentica(usuario, senha)
        if sucesso:
            self._usuario_atual = usuario
            print(mensagem)
        else:
            print(mensagem)

    def verificar_permissao(self):
        return isinstance(self._usuario_atual, UsuarioPrimario)

    def adicionar_doramas_favoritos(self):
        if self.verificar_permissao():
            nome = input('Nome do dorama: ')
            total_eps = int(input('Total de episodios: '))
            nota = float(input('Nota do dorama: '))
            emissora = input('Emissora do dorama: ')
            if nome in self._doramas_favoritos:
                print(f'Dorama {nome} já existe na lista de favoritos!')
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
        if self.verificar_permissao():
            dorama_nome = input('Dorama que voce deseja remover: ')
            if dorama_nome in self._doramas_favoritos:
                dorama = self._doramas_favoritos[dorama_nome]
                dorama.remover_doramas()
                del self._doramas_favoritos[dorama_nome]
                print('Dorama removido com sucesso!\n')
            else:
                print(f'Dorama {dorama_nome} não encontrada!\n')
        else:
            print('Você não possui permissão para remover doramas!')

    def atualizar_doramas_favoritos(self):
        if self.verificar_permissao():
            nome = input('Informe o dorama que deseja atualizar: ')
            if nome in self._doramas_favoritos:
                op = input('Informe o que deseja atualizar: ')
                print('1 - Atualizar nome:')
                print('2 - Atualizar total de episodios:')
                print('3 - Atualizar nota:')
                print('4 - Atualizar emissora:')
                dorama = self._doramas_favoritos[nome]
                if op == '1':
                    novo_nome = input('Informe o novo nome: ')
                    if novo_nome:
                        dorama.atualizar_doramas(nome=novo_nome)
                elif op == '2':
                    novo_total_eps = int(input('Informe o novo total de episodios: '))
                    if novo_total_eps:
                        dorama.atualizar_doramas(total_eps=novo_total_eps)
                elif op == '3':
                    nova_nota = float(input('Informe a nova nota: '))
                    if nova_nota:
                        dorama.atualizar_doramas(nota=nova_nota)
                elif op == '4':
                    nova_emissora = input('Informe a nova emissora: ')
                    if nova_emissora:
                        dorama.atualizar_doramas(emissora=nova_emissora)
                else:
                    print('Opção inválida!\n')
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
            print(f'Dorama {dorama_pesquisar} não foi encontrado na lista!')

    def adicionar_doramas_assistidos(self):
        nome = input('Nome do dorama: ')
        total_eps = int(input('Total de episodios: '))
        nota = float(input('Nota do dorama: '))
        emissora = input('Emissora do dorama: ')
        if nome in self._doramas_assistidos:
            print(f'Dorama {nome} já existe na lista de assistidos!')
        else:
            novo_dorama = Doramas_assistidos(nome, total_eps, nota, emissora)
            self._doramas_assistidos[nome] = novo_dorama.adicionar_doramas()
            print(f'Dorama {nome} adicionado aos assistidos.\n')

    def listar_doramas_assistidos(self):
        for nome, dados in self._doramas_assistidos.items():
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
            print("------")

    def remover_doramas_assistidos(self):
        dorama_nome = input('Dorama que você deseja remover: ')
        if dorama_nome in self._doramas_assistidos:
            del self._doramas_assistidos[dorama_nome]
            print('Dorama removido com sucesso!\n')
        else:
            print(f'Dorama {dorama_nome} não encontrada!\n')

    def atualizar_doramas_assistidos(self):
        nome = input('Informe o dorama que deseja atualizar: ')
        if nome in self._doramas_assistidos:
            op = input('Informe o que deseja atualizar: ')
            print('1 - Atualizar nome:')
            print('2 - Atualizar total de episodios:')
            print('3 - Atualizar nota:')
            print('4 - Atualizar emissora:')
            dorama = self._doramas_assistidos[nome]
            if op == '1':
                novo_nome = input('Informe o novo nome: ')
                if novo_nome:
                    dorama.atualizar_doramas(nome=novo_nome)
            elif op == '2':
                novo_total_eps = int(input('Informe o novo total de episodios: '))
                if novo_total_eps:
                    dorama.atualizar_doramas(total_eps=novo_total_eps)
            elif op == '3':
                nova_nota = float(input('Informe a nova nota: '))
                if nova_nota:
                    dorama.atualizar_doramas(nota=nova_nota)
            elif op == '4':
                nova_emissora = input('Informe a nova emissora: ')
                if nova_emissora:
                    dorama.atualizar_doramas(emissora=nova_emissora)
            else:
                print('Opção inválida!\n')
        else:
            print('Dorama não encontrado!\n')

    def pesquisar_doramas_assistidos(self):
        dorama_pesquisar = input('Informe o nome do dorama que deseja pesquisar: ')
        if dorama_pesquisar in self._doramas_assistidos:
            dados = self._doramas_assistidos[dorama_pesquisar]
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
            print("------")
        else:
            print(f'Dorama {dorama_pesquisar} não foi encontrado na lista!')

    def adicionar_doramas_nao_assistidos(self):
        nome = input('Nome do dorama: ')
        total_eps = int(input('Total de episodios: '))
        nota = float(input('Nota do dorama: '))
        emissora = input('Emissora do dorama: ')
        if nome in self._doramas_nao_assistidos:
            print(f'Dorama {nome} já existe na lista de não assistidos!')
        else:
            novo_dorama = Dorama_nao_assistidos(nome, total_eps, nota, emissora)
            self._doramas_nao_assistidos[nome] = novo_dorama.adicionar_doramas()
            print(f'Dorama {nome} adicionado aos não assistidos.\n')

    def listar_doramas_nao_assistidos(self):
        for nome, dados in self._doramas_nao_assistidos.items():
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
            print("------")

    def remover_doramas_nao_assistidos(self):
        dorama_nome = input('Dorama que você deseja remover: ')
        if dorama_nome in self._doramas_nao_assistidos:
            del self._doramas_nao_assistidos[dorama_nome]
            print('Dorama removido com sucesso!\n')
        else:
            print(f'Dorama {dorama_nome} não encontrada!\n')

    def atualizar_doramas_nao_assistidos(self):
        nome = input('Informe o dorama que deseja atualizar: ')
        if nome in self._doramas_nao_assistidos:
            op = input('Informe o que deseja atualizar: ')
            print('1 - Atualizar nome:')
            print('2 - Atualizar total de episodios:')
            print('3 - Atualizar nota:')
            print('4 - Atualizar emissora:')
            dorama = self._doramas_nao_assistidos[nome]
            if op == '1':
                novo_nome = input('Informe o novo nome: ')
                if novo_nome:
                    dorama.atualizar_doramas(nome=novo_nome)
            elif op == '2':
                novo_total_eps = int(input('Informe o novo total de episodios: '))
                if novo_total_eps:
                    dorama.atualizar_doramas(total_eps=novo_total_eps)
            elif op == '3':
                nova_nota = float(input('Informe a nova nota: '))
                if nova_nota:
                    dorama.atualizar_doramas(nota=nova_nota)
            elif op == '4':
                nova_emissora = input('Informe a nova emissora: ')
                if nova_emissora:
                    dorama.atualizar_doramas(emissora=nova_emissora)
            else:
                print('Opção inválida!\n')
        else:
            print('Dorama não encontrado!\n')

    def pesquisar_doramas_nao_assistidos(self):
        dorama_pesquisar = input('Informe o nome do dorama que deseja pesquisar: ')
        if dorama_pesquisar in self._doramas_nao_assistidos:
            dados = self._doramas_nao_assistidos[dorama_pesquisar]
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
            print("------")
        else:
            print(f'Dorama {dorama_pesquisar} não foi encontrado na lista!')

    def exibir_menu(self):
        self.setar_usuario()
        while True:
            print('1 - Setar usuário')
            print('2 - Adicionar dorama aos favoritos')
            print('3 - Listar doramas favoritos')
            print('4 - Remover dorama dos favoritos')
            print('5 - Atualizar dorama favorito')
            print('6 - Pesquisar dorama favorito')
            print('7 - Adicionar dorama assistido')
            print('8 - Listar doramas assistidos')
            print('9 - Remover dorama assistido')
            print('10 - Atualizar dorama assistido')
            print('11 - Pesquisar dorama assistido')
            print('12 - Adicionar dorama não assistido')
            print('13 - Listar doramas não assistidos')
            print('14 - Remover dorama não assistido')
            print('15 - Atualizar dorama não assistido')
            print('16 - Pesquisar dorama não assistido')
            print('0 - Sair')
            opcao = input('Escolha uma opção: ')

            if opcao == '1':
                pass
            elif opcao == '2':
                self.adicionar_doramas_favoritos()
            elif opcao == '3':
                self.listar_doramas_favoritos()
            elif opcao == '4':
                self.remover_doramas_favoritos()
            elif opcao == '5':
                self.atualizar_doramas_favoritos()
            elif opcao == '6':
                self.pesquisar_doramas_favoritos()
            elif opcao == '7':
                self.adicionar_doramas_assistidos()
            elif opcao == '8':
                self.listar_doramas_assistidos()
            elif opcao == '9':
                self.remover_doramas_assistidos()
            elif opcao == '10':
                self.atualizar_doramas_assistidos()
            elif opcao == '11':
                self.pesquisar_doramas_assistidos()
            elif opcao == '12':
                self.adicionar_doramas_nao_assistidos()
            elif opcao == '13':
                self.listar_doramas_nao_assistidos()
            elif opcao == '14':
                self.remover_doramas_nao_assistidos()
            elif opcao == '15':
                self.atualizar_doramas_nao_assistidos()
            elif opcao == '16':
                self.pesquisar_doramas_nao_assistidos()
            elif opcao == '0':
                break
            else:
                print('Opção inválida!\n')

gerenciador = GerenciarDoramas()
gerenciador.exibir_menu()
