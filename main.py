import abc 

class IUsuario(abc.ABC):
    def __init__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha
    @abc.abstractmethod
    def autenticar(self, senha):
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
    def __init__(self, nome, cpf, senha) -> None:
        super().__init__(nome, cpf, senha)
    
    def autenticacao(self, senha = None):
        return True, 'Login realizado como conidado'

class ControleAutenticacao():
    def __init__(self):
        pass

    def autentica(self, usuario, senha):
        if isinstance(usuario, IUsuario):
            return usuario.autenticacao(senha)
        else:
            return False, 'Usuário informado não tem permissão permissão de login!'

class Dorama:
    def __init__(self, nome, total_eps, nota, emissora):
        self._nome = nome
        self._total_eps = total_eps
        self._nota = nota
        self._emissora = emissora
        # adicionar uma lista com a categoria dos doramas
    
        

#arrumar as classes dos doramas e as suas respctivas funções
        
class Dorama_Favorito(Dorama):
        
    def __init__(self,nome, total_eps, nota, emissora):
        super().__init__(nome, total_eps, nota, emissora)
        
    def adicionar_doramas_favoritos(self):
        return {
            'nome': self._nome,
            'total_eps': self._total_eps,
            'nota': self._nota,
            'emissora': self._emissora
        }
    
    def atualizar_doramas(self, nome = None, total_eps = None, nota = None, emissora = None):
        if nome:
            self._nome = nome
        if total_eps:
            self._total_eps = total_eps
        if nota:
            self._nota = nota
        if emissora:
            self._emissora = emissora
        print(f'Dorama {self._nome} atualizado com sucesso!')

    def remover_doramas_favoritos(self):
        self._nome = None
        self._nota = None
        self._emissora = None
        self._nota = None

class Doramas_assistidos(Dorama):
    def __init__(self,nome, total_eps, nota, emissora):
        super().__init__(nome, total_eps, nota, emissora)
        
    def adicionar_doramas_assistidos(self):
        return {
            'nome': self._nome,
            'total_eps': self._total_eps,
            'nota': self._nota,
            'emissora': self._emissora
        }
        
    def atualizar_doramas(self, nome = None, total_eps = None, nota = None, emissora = None):
        if nome:
            self._nome = nome
        if total_eps:
            self._total_eps = total_eps
        if nota:
            self._nota = nota
        if emissora:
            self._emissora = emissora
        print(f'Dorama {self._nome} atualizado com sucesso!')
        
    def remover_dorama_assistido(self):
        self._nome = None
        self._nota = None
        self._emissora = None
        self._nota = None
        
        
class Dorama_nao_assistidos(Dorama):
    def __init__(self,nome, total_eps, nota, emissora):
        super().__init__(nome, total_eps, nota, emissora)
 
        
class GerenciarDoramas():
    def __init__(self):
        self._doramas = {}
        self._doramas_favoritos = {}
        self._doramas_assistidos = {}
        self._doramas_nao_assistidos = {}
        self._usuario_atual = None
    
    def setar_usuario(self):
        nome = input('Informe o seu nome: ') 
        cpf = input('Informe o seu cpf: ')
        senha = input('Informe o seu senha: ')
        self._usuario_atual = UsuarioPrimario(nome, cpf, senha)
     
    def adicionar_doramas_favoritos(self):
        
        if not isinstance(self._usuario_atual, UsuarioPrimario):
            nome = input('Nome do dorama: ')
            total_eps = int(input('Total de episodios: '))
            nota = float(input('Nota do dorama: '))
            emissora = input('Emissora do dorama: ')

            
            if nome in self._doramas_favoritos:
                print(f'Dorama {nome} já existe na lista de favoritos!')
            else:
                novo_dorama = Dorama_Favorito(nome, total_eps, nota, emissora)
                self._doramas_favoritos[nome] = novo_dorama.adicionar_doramas_favoritos()
                print(f'Dorama {nome} adicionado aos favoritos.')
        else:
            print('Você não possui permissão para adicionar doramas favoritas!')
            
                
    def listar_doramas(self):
        for nome, dados in self._doramas_favoritos.items():
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
            print("------")
            
    def remover_dorama(self):
        if not isinstance(self._usuario_atual, UsuarioPrimario):
            dorama_nome = input('Dorama que voce deseja remover: ')
            
            if dorama_nome in self._doramas_favoritos:
                dorama = self._doramas_favoritos[dorama_nome]
                dorama.remover_doramas_favoritos()
                del self._doramas_favoritos[dorama_nome]
                print('Dorama removido com sucesso!\n')
            else:
                print(f'Dorama {dorama_nome} não encontrada!\n')
        else:
            print('Você não possui permissão para remover doramas!')
            
                
    def atualizar_dorama(self):
        if not isinstance(self._usuario_atual, UsuarioPrimario):
            nome = input('Informe o dorama que deseja atualizar: ')
            if nome in self._doramas_favoritos:
                op = input('Informe o que deseja atualizar: ')
                print('1 - atualizar nome:')
                print('2 - atualizar total de epsodios:')
                print('3 - atualizar nota:')
                print('4 - atualizar emissora:')
                #print('5 - atualizar categoria:')
                dorama =  self._doramas_favoritos[nome]
                if op == '1':
                    novo_nome = input('Informe o dorama que deseja atualizar: ')
                    if novo_nome:
                        dorama.atualizar_dorama(nome = novo_nome)
                        
                elif op == '2':
                    novo_total_eps = int(input('Informe o novo total de episodios: '))
                    if novo_total_eps:
                        dorama.atualizar_dorama(total_eps = novo_total_eps)
                
                elif op == '3':
                    novo_nota = float(input('Informe a nova nota do dorama: '))
                    if novo_nota:
                        dorama.atualizar_dorama(nota = novo_nota)
                        
                elif op == '4':
                    novo_emissora = input('Informe a nova emissora do dorama: ')
                    if novo_emissora:
                        dorama.atualizar_dorama(emissora = novo_emissora)
                else:
                    print('Opção invalida!\n')
        else:
            print('Você não possui permissão para atualizar doramas!')
        
    def pesquisar_doramas(self):
        
        dorama_pesquisar = input('Informe o nome do dorama que deseja pesquisar: ')
        
        if dorama_pesquisar in self._doramas_favoritos:
            dados = self._doramas_favoritos[dorama_pesquisar]
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
            print("------")
        else:
            print(f'Dorama {dorama_pesquisar} não foi encontrada na lista!')
 
            
##################################################################################################
 
                    
    def adicionar_doramas_assistidos(self):
        
        nome = input('Nome do dorama: ')
        total_eps = int(input('Total de episodios: '))
        nota = float(input('Nota do dorama: '))
        emissora = input('Emissora do dorama: ')

        
        if nome in self._doramas_favoritos:
            print(f'Dorama {nome} já existe na lista de favoritos!')
        else:
            novo_dorama = Doramas_assistidos(nome, total_eps, nota, emissora)
            self._doramas_assistidos[nome] = novo_dorama.adicionar_doramas_assistidos()
            print(f'Dorama {nome} adicionado aos assistidos.\n')
        
    def listar_doramas_assistidos(self):
         for nome, dados in self._doramas_assistidos.items():
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
            print("------")   
    
    def remover_dorama(self):
        dorama_nome = input('Dorama que voce deseja remover: ')
        
        if dorama_nome in self._doramas_favoritos:
            dorama = self._doramas_favoritos[dorama_nome]
            dorama.remover_doramas_favoritos()
            del self._doramas_favoritos[dorama_nome]
            print('Dorama removido com sucesso!\n')
        else:
            print(f'Dorama {dorama_nome} não encontrada!\n')
            
    def atualizar_dorama(self):
        nome = input('Informe o dorama que deseja atualizar: ')
        if nome in self._doramas_favoritos:
            op = input('Informe o que deseja atualizar: ')
            print('1 - atualizar nome:')
            print('2 - atualizar total de epsodios:')
            print('3 - atualizar nota:')
            print('4 - atualizar emissora:')
            #print('5 - atualizar categoria:')
            dorama =  self._doramas_favoritos[nome]
            if op == '1':
                novo_nome = input('Informe o dorama que deseja atualizar: ')
                if novo_nome:
                    dorama.atualizar_dorama(nome = novo_nome)
                    
            elif op == '2':
                novo_total_eps = int(input('Informe o novo total de episodios: '))
                if novo_total_eps:
                    dorama.atualizar_dorama(total_eps = novo_total_eps)
            
            elif op == '3':
                novo_nota = float(input('Informe a nova nota do dorama: '))
                if novo_nota:
                    dorama.atualizar_dorama(nota = novo_nota)
                    
            elif op == '4':
                novo_emissora = input('Informe a nova emissora do dorama: ')
                if novo_emissora:
                    dorama.atualizar_dorama(emissora = novo_emissora)
            else:
                print('Opção invalida!\n')
    
    def pesquisar_doramas(self):
        
        dorama_pesquisar = input('Informe o nome do dorama que deseja pesquisar: ')
        
        if dorama_pesquisar in self._doramas_favoritos:
            dados = self._doramas_favoritos[dorama_pesquisar]
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
            print("------")
        else:
            print(f'Dorama {dorama_pesquisar} não foi encontrada na lista!')
                    
           
#     def assistir_dorama(self, dorama_nome):
#         
    
#     def favoritar_dorama_assitidos(self, dorama_nome):
#         
            
#     def favoritar_dorama_nao_assistidos(self, dorama_nome):
#         
        

# #Função para Encontrar Doramas por Intervalo de Episodios
 

    def exibir_menu(self):
            while True:
                print("\nMenu:")
                print("1. Adicionar doramas favoritos")
                print("2. Listar doramas favoritos")
                print("3. Remover dorama favorito")
                print("4. Sair")
                opcao = input("Escolha uma opção: ")

                if opcao == '1':
                    self.adicionar_doramas_favoritos()
                elif opcao == '2':
                    self.listar_doramas()
                elif opcao == '3':
                    self.remover_dorama()
                elif opcao == '4':
                    print("Saindo do programa.")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

# Exemplo de uso
gerenciar = GerenciarDoramas()
gerenciar.exibir_menu()