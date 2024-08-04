class Dorama:
    def __init__(self, nome, total_eps, nota, emissora, categorias=[]):
        self._nome = nome
        self._total_eps = total_eps
        self._nota = nota
        self._emissora = emissora
        self._categorias = categorias
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def total_eps(self):
        return self._total_eps
    
    @property
    def nota(self):
        return self._nota
    
    @property
    def emissora(self):
        return self._emissora
    
    @property
    def categorias(self):
        return self._categorias
    
    def atualizar_dorama(self, nome=None, total_eps=None, nota=None, emissora=None, categorias=None):
        if nome:
            self._nome = nome
        if total_eps:
            self._total_eps = total_eps
        if nota:
            self._nota = nota
        if emissora:
            self._emissora = emissora
        if categorias:
            self._categorias = categorias
        print(f'Dorama {self._nome} atualizado com sucesso!')

    def remover_dorama(self):
        self._nome = None
        self._total_eps = None
        self._nota = None
        self._emissora = None
        self._categorias = None
        print('Dorama removido com sucesso!')

class DoramaFavorito(Dorama):
    pass

class DoramasAssistidos(Dorama):
    pass

class DoramaNaoAssistido(Dorama):
    pass

class GerenciarDoramas:
    def __init__(self):
        self._doramas_favoritos = {}
        self._doramas_assistidos = {}
        self._doramas_nao_assistidos = {}
       

    def adicionar_dorama_favoritos(self):
        categorias = []
        nome = input('Nome do dorama: ')
        total_eps = int(input('Total de episodios: '))
        nota = float(input('Nota do dorama: '))
        emissora = input('Emissora do dorama: ')
        count = int(input('Quantas categorias tem o dorama: '))
        
        for i in range(count):
            categorias.append(input(f'Digite a categoria {i+1}: '))
            
        if nome in self._doramas_favoritos:
            print(f'Dorama {nome} já existe na lista de favoritos!')
        else:
            novo_dorama = DoramaFavorito(nome, total_eps, nota, emissora, categorias)
            self._doramas_favoritos[nome] = novo_dorama
            print(f'Dorama {nome} adicionado aos favoritos.')
    
    def listar_doramas_favoritos(self):
        for nome, dados in self._doramas_favoritos.items():
            for chave, valor in dados.items():
                print(f'{chave.capitalize()}: {valor}')
            print('------')
            
    def remover_dorama_favoritos(self):
        dorama_nome = input('Dorama que você deseja remover: ')
        
        if dorama_nome in self._doramas_favoritos:
            del self._doramas_favoritos[dorama_nome]
            print('Dorama removido com sucesso!\n')
        else:
            print(f'Dorama {dorama_nome} não encontrada!\n')
    
    def atualizar_dorama_favoritos(self):
        nome = input('Informe o dorama que deseja atualizar: ')
        if nome in self._doramas_favoritos:
            op = input('Informe o que deseja atualizar: \n1 - atualizar nome\n2 - atualizar total de episodios\n3 - atualizar nota\n4 - atualizar emissora\n5 - atualizar categoria\n')
            if op == '1':
                novo_nome = input('Informe o novo nome do dorama: ')
                if novo_nome:
                    self._doramas_favoritos[nome].atualizar_dorama(novo_nome) 
            elif op == '2':
                novo_total_eps = int(input('Informe o novo total de episodios: '))
                if novo_total_eps:
                    self._doramas_favoritos[nome]['total_eps'] = novo_total_eps

        
    def pesquisar_doramas_favoritos(self):
        dorama_pesquisar = input('Informe o nome do dorama que deseja pesquisar: ')
        if dorama_pesquisar in self._doramas_favoritos:
            dados = self._doramas_favoritos[dorama_pesquisar]
            for chave, valor in dados.items():
                print(f'{chave.capitalize()}: {valor}')
            print('------')
        else:
            print(f'Dorama {dorama_pesquisar} não foi encontrada na lista!')
            
    def menu(self):
        
        
        while True:
            print("===== Menu de Gerenciamento de Doramas =====")
            print("1. Adicionar Dorama aos Favoritos")
            print("2. Listar Doramas Favoritos")
            print("3. Remover Dorama dos Favoritos")
            print("4. Atualizar Dorama nos Favoritos")
            print("5. Pesquisar Dorama nos Favoritos")
            print("0. Sair")
            
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.adicionar_dorama_favoritos()
            elif opcao == '2':
                self.listar_doramas_favoritos()
            elif opcao == '3':
                self.remover_dorama_favoritos()
            elif opcao == '4':
                self.atualizar_dorama_favoritos()
            elif opcao == '5':
                self.pesquisar_doramas_favoritos()
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")

gerenciador = GerenciarDoramas()
gerenciador.menu()
