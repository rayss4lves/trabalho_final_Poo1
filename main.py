import abc

class IUsuario(abc.ABC):
    def __init__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def senha(self):
        return self._senha

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

    def adicionar_doramas(self):
        return {
            'nome': self._nome,
            'total_eps': self._total_eps,
            'nota': self._nota,
            'emissora': self._emissora,
            'categorias' : self._categorias
        }
    
    def atualizar_doramas(self, nome = None, total_eps = None, nota = None, emissora = None, categorias = None):
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
        self._nota = None
        self._emissora = None
        self._nota = None
        self._categorias = None
        

#arrumar as classes dos doramas e as suas respctivas funções
        
class Dorama_Favorito(Dorama):
        
    def __init__(self,nome, total_eps, nota, emissora, categorias=[]):
        super().__init__(nome, total_eps, nota, emissora, categorias)
        
    

class Doramas_assistidos(Dorama):
    def __init__(self,nome, total_eps, nota, emissora, categorias=[]):
        super().__init__(nome, total_eps, nota, emissora, categorias)
        
    
        
        
class Dorama_nao_assistidos(Dorama):
    def __init__(self,nome, total_eps, nota, emissora, categorias=[]):
        super().__init__(nome, total_eps, nota, emissora, categorias)
 
        
class GerenciarDoramas():
    def __init__(self):
        self._doramas = {}
        self._doramas_favoritos = {}
        self._doramas_assistidos = {}
        self._doramas_nao_assistidos = {}
        self._usuario_atual = None
        
    def set_usuario_atual(self, usuario):
        self._usuario_atual = usuario    

     
    def adicionar_doramas_favoritos(self):
        
        if isinstance(self._usuario_atual, UsuarioPrimario):
            categorias = []
            nome = input('Nome do dorama: ')
            total_eps = int(input('Total de episodios: '))
            nota = float(input('Nota do dorama: '))
            emissora = input('Emissora do dorama: ')
            count = int(input('Quantas categorias tem o dorama: '))
            
            for i in range(count):
                categorias.append(input(f'Digite a categoria {i+1}: '))
                
            if nome in self._doramas_favoritos:
                print(f'Dorama {nome} ja existe na lista de favoritos!')
            else:
                novo_dorama = Dorama_Favorito(nome, total_eps, nota, emissora, categorias)
                self._doramas_favoritos[nome] = novo_dorama.adicionar_doramas()
                print(f'Dorama {nome} adicionado aos favoritos.')
        else:
            print('Você não possui permissão para adicionar doramas favoritas!')
            
                
    def listar_doramas_favoritos(self):
        for nome, dados in self._doramas_favoritos.items():
            for chave, valor in dados.items():
                print(f'{chave.capitalize()}: {valor}')
            print('------')
            
    def remover_doramas_favoritos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
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
        if isinstance(self._usuario_atual, UsuarioPrimario):
            nome = input('Informe o dorama que deseja atualizar: ')
            if nome in self._doramas_favoritos:
                op = input('Informe o que deseja atualizar: ')
                print('1 - atualizar nome:')
                print('2 - atualizar total de epsodios:')
                print('3 - atualizar nota:')
                print('4 - atualizar emissora:')
                print('5 - atualizar categoria:')
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
                elif op == '5':
                    antiga_categoria = input('Antiga categoria do dorama: ')
                    nova_categoria = input('Informe a nova emissora do dorama: ')
                    for i in range(len(dorama.categoria)):
                        if antiga_categoria == dorama.categoria[i]:
                            dorama.categoria[i] = nova_categoria
                            break
                else:
                    print('Opção invalida!\n')
        else:
            print('Você não possui permissão para atualizar doramas!')
        
    def pesquisar_doramas_favoritos(self):
        
        dorama_pesquisar = input('Informe o nome do dorama que deseja pesquisar: ')
        
        if dorama_pesquisar in self._doramas_favoritos:
            dados = self._doramas_favoritos[dorama_pesquisar]
            for chave, valor in dados.items():
                print(f'{chave.capitalize()}: {valor}')
            print('------')
        else:
            print(f'Dorama {dorama_pesquisar} não foi encontrada na lista!')
 
            
###############################################DORAMAS ASSISTIDOS###################################################
 
                    
    def adicionar_doramas_assistidos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            categorias = []
            nome = input('Nome do dorama: ')
            total_eps = int(input('Total de episodios: '))
            nota = float(input('Nota do dorama: '))
            emissora = input('Emissora do dorama: ')
            count = input('Quantas categorias tem o dorama: ')
            
            for i in range(count):
                categorias.append(input(f'Digite a categoria {i+1}: '))
            
            if nome in self._doramas_assistidos:
                print(f'Dorama {nome} ja existe na lista de favoritos!')
            else:
                novo_dorama = Doramas_assistidos(nome, total_eps, nota, emissora, categorias)
                self._doramas_assistidos[nome] = novo_dorama.adicionar_doramas()
                print(f'Dorama {nome} adicionado aos assistidos.\n')
        else:
            print('Você não possui permissão para adicionar doramas assistidos!')
    def listar_doramas_assistidos(self):
         for nome, dados in self._doramas_assistidos.items():
            for chave, valor in dados.items():
                print(f'{chave.capitalize()}: {valor}')
            print('------')   
    
    def remover_doramas_assistidos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            dorama_nome = input('Dorama que voce deseja remover: ')
            
            if dorama_nome in self._doramas_assistidos:
                del self._doramas_assistidos[dorama_nome]
                print('Dorama removido com sucesso!\n')
            else:
                print(f'Dorama {dorama_nome} não encontrada!\n')
        else:
            print('Você não possui permissão para remover doramas!')
            
    def atualizar_doramas_assistidos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            nome = input('Informe o dorama que deseja atualizar: ')
            if nome in self._doramas_assistidos:
                op = input('Informe o que deseja atualizar: ')
                print('1 - atualizar nome:')
                print('2 - atualizar total de epsodios:')
                print('3 - atualizar nota:')
                print('4 - atualizar emissora:')
                #print('5 - atualizar categoria:')
                dorama =  self._doramas_assistidos[nome]
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
                elif op == '5':
                    antiga_categoria = input('Antiga categoria do dorama: ')
                    nova_categoria = input('Informe a nova emissora do dorama: ')
                    for i in range(len(dorama.categoria)):
                        if antiga_categoria == dorama.categoria[i]:
                            dorama.categoria[i] = nova_categoria
                            break
                else:
                    print('Opção invalida!\n')
        else:
            print('Você não possui permissão para atualizar doramas!')   
    
    def pesquisar_doramas(self):
        
        dorama_pesquisar = input('Informe o nome do dorama que deseja pesquisar: ')
        
        if dorama_pesquisar in self._doramas_assistidos:
            dados = self._doramas_assistidos[dorama_pesquisar]
            for chave, valor in dados.items():
                print(f'{chave.capitalize()}: {valor}')
            print('------')
        else:
            print(f'Dorama {dorama_pesquisar} não foi encontrada na lista!')
                    
           
    def assistir_dorama(self):
        dorama_nome = input('Informe o nome do dorama que deseja confirmar que assistiu: ')
        if dorama_nome in self._doramas_nao_assistidos:
            self._doramas_assistidos[dorama_nome] = self._doramas_nao_assistidos[dorama_nome]
            del self._doramas_nao_assistidos[dorama_nome]
        else:
            print(f'Dorama {dorama_nome} não foi encontrada na lista!')
                    
#         
    
    def favoritar_dorama_assitidos(self):
        dorama_nome = input('Informe o nome do dorama que deseja favoritar: ')
        if dorama_nome in self._doramas_assistidos:
            self._doramas_favoritos[dorama_nome] = self._doramas_assistidos[dorama_nome]
            del self._doramas_assistidos[dorama_nome]
        else:
            print(f'Dorama {dorama_nome} não foi encontrada na lista!')
#         
            
    
#         
        

###############################################DORAMAS NAO ASSISTIDOS###################################################
 
    def adicionar_doramas_nao_assistidos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            categorias = []
            nome = input('Nome do dorama: ')
            total_eps = int(input('Total de episodios: '))
            nota = float(input('Nota do dorama: '))
            emissora = input('Emissora do dorama: ')
            count = input('Quantas categorias tem o dorama: ')
            
            for i in range(count):
                categorias.append(input(f'Digite a categoria {i+1}: '))
            
            if nome in self._doramas_nao_assistidos:
                print(f'Dorama {nome} ja existe na lista de favoritos!')
            else:
                novo_dorama = Doramas_assistidos(nome, total_eps, nota, emissora, categorias)
                self._doramas_nao_assistidos[nome] = novo_dorama.adicionar_doramas()
                print(f'Dorama {nome} adicionado aos assistidos.\n')
        else:
            print('Você não possui permissão para adicionar doramas!')
        
    def listar_doramas_nao_assistidos(self):
         for nome, dados in self._doramas_nao_assistidos.items():
            for chave, valor in dados.items():
                print(f'{chave.capitalize()}: {valor}')
            print('------')   
    
    def remover_dorama_nao_assistido(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            dorama_nome = input('Dorama que voce deseja remover: ')
            
            if dorama_nome in self._doramas_nao_assistidos:
                del self._doramas_nao_assistidos[dorama_nome]
                print('Dorama removido com sucesso!\n')
            else:
                print(f'Dorama {dorama_nome} não encontrada!\n')
        else:
            print('Você não possui permissão para remover doramas!')
            
    def atualizar_doramas_nao_assistidos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            nome = input('Informe o dorama que deseja atualizar: ')
            if nome in self._doramas_nao_assistidos:
                
                print('1 - atualizar nome:')
                print('2 - atualizar total de epsodios:')
                print('3 - atualizar nota:')
                print('4 - atualizar emissora:')
                print('5 - atualizar categoria:')
                op = input('Informe o que deseja atualizar: ')
                dorama =  self._doramas_nao_assistidos[nome]
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
                elif op == '5':
                    antiga_categoria = input('Antiga categoria do dorama: ')
                    nova_categoria = input('Informe a nova emissora do dorama: ')
                    for i in range(len(dorama.categoria)):
                        if antiga_categoria == dorama.categoria[i]:
                            dorama.categoria[i] = nova_categoria
                            break
                else:
                    print('Opção invalida!\n')
        else:
            print('Você não possui permissão para atualizar doramas!')
            
    def pesquisar_doramas_nao_assistidos(self):
        
        dorama_pesquisar = input('Informe o nome do dorama que deseja pesquisar: ')
        
        if dorama_pesquisar in self._doramas_favoritos:
            dados = self._doramas_favoritos[dorama_pesquisar]
            for chave, valor in dados.items():
                print(f'{chave.capitalize()}: {valor}')
            print('------')
        else:
            print(f'Dorama {dorama_pesquisar} não foi encontrada na lista!')

    def favoritar_dorama_nao_assistidos(self):
        dorama_nome = input('Informe o nome do dorama que deseja favoritar: ')
        if dorama_nome in self._doramas_nao_assistidos:
            self._doramas_favoritos[dorama_nome] = self._doramas_nao_assistidos[dorama_nome]
            del self._doramas_nao_assistidos[dorama_nome]
        else:
            print(f'Dorama {dorama_nome} não foi encontrada na lista!')


##########################################MENU GERENCIAR DORAMAS###################################################

    def menu_favoritos(self):
        while True:
            print('\n----------------------------------\n')
            print('1. Adicionar doramas')
            print('2. Listar doramas')
            print('3. Remover dorama')
            print('4. Pesquisar dorama')
            print('5. Atualizar dorama')
            print('\n----------------------------------\n')
            print('6. Voltar')
            opcao = input('Escolha uma opção: ')
            
            if opcao == '1':
                self.adicionar_doramas_favoritos()
            elif opcao == '2':
                self.listar_doramas_favoritos()
            elif opcao == '3':
                self.remover_doramas_favoritos()
            elif opcao == '4':
                self.pesquisar_doramas_favoritos()
            elif opcao == '5':
                self.atualizar_doramas_favoritos()
            else:
                print('Programa encerrando!')
                break
            
    def menu_assistidos(self):
        while True:
            print('\n----------------------------------\n')
            print('1. Adicionar doramas assistidos')
            print('2. Listar doramas assistidos')
            print('3. Remover dorama assistido')
            print('4. Pesquisar dorama')
            print('5. Atualizar dorama')
            print('\n----------------------------------\n')
            print('6. Voltar')
            opcao = input('Escolha uma opção: ')
            
            if opcao == '1':
                self.adicionar_doramas_assistidos()
            elif opcao == '2':
                self.listar_doramas_assistidos()
            elif opcao == '3':
                self.remover_doramas_assistidos()
            elif opcao == '4':
                self.pesquisar_doramas_assistidos()
            elif opcao == '5':
                self.atualizar_doramas_assistidos()
            else:
                print('Programa encerrando!')
                break
            
    def menu_nao_assistidos(self):
        while True:
            print('\n----------------------------------\n')
            print('1. Adicionar doramas nao assistidos')
            print('2. Listar doramas nao assistidos')
            print('3. Remover dorama nao assistido')
            print('4. Pesquisar dorama')
            print('5. Atualizar dorama')
            print('\n----------------------------------\n')
            print('6. Voltar')
            opcao = input('Escolha uma opção: ')
            
            if opcao == '1':
                self.adicionar_doramas_nao_assistidos()
            elif opcao == '2':
                self.listar_doramas_nao_assistidos()
            elif opcao == '3':
                self.remover_doramas_nao_assistidos()
            elif opcao == '4':
                self.pesquisar_doramas_nao_assistidos()
            elif opcao == '5':
                self.atualizar_doramas_nao_assistidos()
            else:
                print('Programa encerrando!')
                break
                
    def exibir_menu(self):
        while True:
            print('\nMenu:')
            print('1. Menu Doramas favoritos')
            print('2. Menu Doramas assistidos')
            print('3. Menu Doramas nao assistidos')
            
            opcao = input('Escolha uma opção: ')

            if opcao == '1':
                self.menu_favoritos()
            elif opcao == '2':
                self.menu_assistidos()
            elif opcao == '3':
                self.menu_nao_assistidos()
            elif opcao == '4':
                print('Programa encerrado.')
                break
            else:
                print('Opção invalida. Tente novamente.')


###########################################CLASSE SISTEMA######################################
class Sistema:
    def __init__(self):
        self._usuarios = {}  
        self._gerenciar_doramas = GerenciarDoramas()  
        self._usuario_atual = None  

    def cadastrar_usuario(self):
        usuario_nome = input('Nome do usuario: ')
        usuario_cpf = input('CPF do usuario: ')
        usuario_senha = input('Senha do usuario: ')
        if usuario_cpf in self._usuarios:
            print('Usuario ja cadastrado!\n')
        else:
            tipo = input('Tipo de usuario (primario/secundario): ')
            if tipo == 'primario':
                self._usuarios[usuario_nome] = UsuarioPrimario(usuario_nome, usuario_cpf, usuario_senha)
            elif tipo == 'secundario':
                self._usuarios[usuario_nome] = UsuarioSecundario(usuario_nome, usuario_cpf, usuario_senha)
            else:
                print('Tipo de usuario invalido!\n')

    def login(self):
        usuario_nome = input('Nome do usuario: ')
        usuario_senha = input('Senha do usuario: ')
        if usuario_nome in self._usuarios:
            usuario = self._usuarios[usuario_nome]
            autenticado, mensagem = usuario.autenticacao(usuario_senha)
            if autenticado:
                self._usuario_atual = usuario
                self._gerenciar_doramas.set_usuario_atual(usuario)
                print(mensagem)
                self._gerenciar_doramas.exibir_menu()
            else:
                print(mensagem)
        else:
            print('Usuario não encontrado!\n')
            
    def listar_usuarios(self):
        for usuario_nome, usuario in self._usuarios.items():
            print(f'Nome: {usuario_nome}, CPF: {usuario.cpf}')


    def menu(self):
        while True:
            print('Menu Principal:')
            print('1 - Cadastrar usuario')
            print('2 - Login')
            print('3 - Listar Usuarios')
            print('0 - Sair')
            opcao = input('Escolha uma opção: ')
            if opcao == '1':
                self.cadastrar_usuario()
            elif opcao == '2':
                self.login()
            elif opcao == '3':
                self.listar_usuarios()
            elif opcao == '0':
                print('Saindo...')
                break
            else:
                print('Opção invalida. Tente novamente.')

sistema = Sistema()
sistema.menu()