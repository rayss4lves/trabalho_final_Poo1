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
    def __init__(self, nome, cpf, senha):
        super().__init__(nome, cpf, senha)
        

    def autenticacao(self, senha):
        if self._senha == senha:
            return True, 'Login realizado com sucesso!'
        else:
            return False, 'Dados incorretos!'

class UsuarioSecundario(IUsuario):
    def __init__(self, nome, cpf, senha):
        super().__init__(nome, cpf, senha)
        
    def autenticacao(self, senha):
        if self._senha == senha:
            return True, 'Login realizado com sucesso!'
        else:
            return False, 'Dados incorretos!'

class ControleAutenticacao():
    def __init__(self):
        pass

    def autenticacao(self, usuario, senha):
        if isinstance(usuario, IUsuario):
            return usuario.autenticacao(senha)
        else:
            return False, 'Usuario informado nao tem permissao de login!'
        
 
#####################################################################################################################
#####################################################CLASSE DORAMA###################################################  
#####################################################################################################################     
        
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
    
    def atualizar_dorama(self, nome = None, total_eps = None, nota = None, emissora = None, categorias = None):
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
                              
class Dorama_Favorito(Dorama):
        
    def __init__(self,nome, total_eps, nota, emissora, categorias=[], motivo=None):
        super().__init__(nome, total_eps, nota, emissora, categorias)
        self._motivo = motivo
    
    @property
    def motivo(self):
        return self._motivo
    
    def atualizar_dorama(self,nome = None, total_eps = None, nota = None, emissora = None, categorias = None, motivo = None):
        super().atualizar_dorama(nome, total_eps, nota, emissora, categorias)
        if motivo:
            self._motivo = motivo
        print(f'Dorama favorita {self._nome} atualizada com sucesso!')
           
class Doramas_assistidos(Dorama):
    def __init__(self,nome, total_eps, nota, emissora, categorias=[], data_view = None):
        super().__init__(nome, total_eps, nota, emissora, categorias)
        self._data_view = data_view
    @property
    def data_view(self):
        return self._data_view
    
    def atualizar_dorama(self, nome=None, total_eps=None, nota=None, emissora=None, categorias=None, data_view=None):
        super().atualizar_dorama(nome, total_eps, nota, emissora, categorias)
        if data_view is not None:
            self._data_view = data_view
                  
class Dorama_nao_assistidos(Dorama):
    def __init__(self,nome, total_eps, nota, emissora, categorias=[], prioridade = None):
        super().__init__(nome, total_eps, nota, emissora, categorias)
        self._prioridade = prioridade
        
    @property
    def prioridade(self):
        return self._prioridade
    
    def atualizar_dorama(self, nome=None, total_eps=None, nota=None, emissora=None, categorias=None, prioridade=None):
        super().atualizar_dorama(nome, total_eps, nota, emissora, categorias)
        if prioridade is not None:
            self._prioridade = prioridade
 
 
######################################################################################################################
###############################################CLASSE GERENCIADOR DE DORAMA########################################### 
######################################################################################################################  
      
class GerenciarDoramas():
    def __init__(self):
        self._doramas_favoritos = {}
        self._doramas_assistidos = {}
        self._doramas_nao_assistidos = {}
        self._usuario_atual = None
        
    def set_usuario_atual(self, usuario):
        self._usuario_atual = usuario    
    
    ###############################################DORAMAS FAVORITOS###################################################
     
    def adicionar_doramas_favoritos(self):
        
        if isinstance(self._usuario_atual, UsuarioPrimario):
            categorias = []
            
            nome = input('Nome do dorama: ').capitalize().strip()
            if not nome: 
                print('Nome invalido! Tente novamente.')
                nome = input('Nome do dorama: ').capitalize().strip()
                
            total_eps = int(input('Total de episodios: '))
            if not total_eps:
                print('Total de episodios invalido! Tente novamente.')
                total_eps = int(input('Total de episodios: '))
                
            nota = float(input('Nota do dorama: '))
            if not nota:
                print('Nota invalida! Tente novamente.')
                nota = float(input('Nota do dorama: '))
                
            emissora = input('Emissora do dorama: ').capitalize().strip()
            if not emissora:
                print('Emissora invalida! Tente novamente.')
                emissora = input('Emissora do dorama: ').capitalize().strip()
                
            count = int(input('Quantas categorias tem o dorama: '))
            if not count:
                print('Quantidade de categorias invalida! Tente novamente.')
                count = int(input('Quantas categorias tem o dorama: '))
                
            for i in range(count):
                categoria = input(f'Digite a categoria {i+1}: ').capitalize().strip() 
                if not categoria:
                    print('Categoria invalida! Tente Novamente.')
                    categoria = input(f'Digite a categoria {i+1}: ').capitalize().strip() 
                categorias.append(categoria)
            motivo = input('Informe o motivo por ter favoritado esse dorama: ').capitalize().strip()
            if not motivo:
                print('Motivo invalido! Tente novamente.')
                motivo = input('Informe o motivo por ter favoritado esse dorama: ').capitalize().strip()
                        
            if nome in self._doramas_favoritos:
                        print(f'Dorama {nome} ja existe na lista de favoritos!')
            else:
                novo_dorama = Dorama_Favorito(nome, total_eps, nota, emissora, categorias, motivo)
                self._doramas_favoritos[nome] = novo_dorama
                print(f'Dorama {nome} adicionado aos favoritos.')
        else:
            print('Você nao possui permissao para adicionar doramas favoritas!')    
        print('\n----------------------------------------\n')
                
    def listar_doramas_favoritos(self):
        if self._doramas_favoritos:
            for nome, dados in self._doramas_favoritos.items():
                print(f'Nome ={nome.capitalize()}')
                print(f'Total de Epsodios = {dados.total_eps}')
                print(f'Nota = {dados.nota}')
                print(f'Emissora = {dados.emissora}')
                for dado in dados.categorias:
                    print(f'Categoria = {dado}')
                print(f'Motivo = {dados.motivo}')
                print('------------------------')
        else:
            print('Nao existem doramas favoritas!\n')
        print('==============================================')        
                        
    def remover_doramas_favoritos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            while True:
                try:
                    dorama_nome = input('Dorama que voce deseja remover: ').capitalize().strip()
                    if not dorama_nome:
                        print('Nome invalido! Tente novamente.')
                        continue
                    break
                except ValueError:
                    print('Valor invalido! Tente novamente.')
            
            if dorama_nome in self._doramas_favoritos:
                del self._doramas_favoritos[dorama_nome]
                print('Dorama removido com sucesso!\n')
            else:
                print(f'Dorama {dorama_nome} nao encontrada!\n')
        else:
            print('Você nao possui permissao para remover doramas!')
        print('\n----------------------------------------\n')    
                
    def atualizar_doramas_favoritos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            nome = input('Informe o dorama que deseja atualizar: ').capitalize().strip()
            if nome in self._doramas_favoritos:
                
                print('1 - atualizar nome:')
                print('2 - atualizar total de epsodios:')
                print('3 - atualizar nota:')
                print('4 - atualizar emissora:')
                print('5 - atualizar categoria:')
                print('6 - atualizar motivo:')
                op = input('Informe o que deseja atualizar: ')
                dorama =  self._doramas_favoritos[nome]

                if op == '1':
                    novo_nome = input('Informe o novo nome do dorama: ').capitalize().strip()
                    if novo_nome:
                        dorama.atualizar_dorama(nome=novo_nome)
                        self._doramas_favoritos[novo_nome] = self._doramas_favoritos.pop(nome)
                        print(f'Dorama {nome} atualizado com sucesso!')
                        
                elif op == '2':
                    novo_total_eps = int(input('Informe o novo total de episodios: '))
                    if novo_total_eps:
                        dorama.atualizar_dorama(total_eps = novo_total_eps)
                        print(f'Dorama {nome} atualizado com sucesso!')
                
                elif op == '3':
                    novo_nota = float(input('Informe a nova nota do dorama: '))
                    if novo_nota:
                        dorama.atualizar_dorama(nota = novo_nota)
                        print(f'Dorama {nome} atualizado com sucesso!')
                        
                elif op == '4':
                    novo_emissora = input('Informe a nova emissora do dorama: ').capitalize().strip()
                    if novo_emissora:
                        dorama.atualizar_dorama(emissora = novo_emissora)
                        print(f'Dorama {nome} atualizado com sucesso!')
                elif op == '5':
                    antiga_categoria = input('Antiga categoria do dorama: ').capitalize().strip()
                    nova_categoria = input('Informe a nova categoria do dorama: ').capitalize().strip()
                    for i in range(len(dorama.categorias)):
                        if antiga_categoria == dorama.categorias[i]:
                            dorama.categorias[i] = nova_categoria
                            break
                    print(f'Dorama {nome} atualizado com sucesso!')
                elif op == '6':
                    novo_motivo = input('Informe o novo motivo por ter favoritado esse dorama: ').capitalize().strip()
                    if novo_motivo:
                        dorama.atualizar_dorama(motivo = novo_motivo)
                        print(f'Dorama {nome} atualizado com sucesso!')
                else:
                    print('Opcao invalida!\n')
        else:
            print('Você nao possui permissao para atualizar doramas!')
        print('\n----------------------------------------\n')
        
    def pesquisar_doramas_favoritos(self):
        
        dorama_pesquisar = input('Informe o nome do dorama que deseja pesquisar: ').capitalize().strip()
        if not dorama_pesquisar:
            print('Nome invalido! Tente novamente.')
            dorama_pesquisar = input('Informe o nome do dorama que deseja pesquisar: ').capitalize().strip()
            
        if dorama_pesquisar in self._doramas_favoritos:
            dados = self._doramas_favoritos[dorama_pesquisar]
            print(f'Nome ={dorama_pesquisar.capitalize()}')
            print(f'Total de Epsodios = {dados.total_eps}')
            print(f'Nota = {dados.nota}')
            print(f'Emissora = {dados.emissora}')
            for dado in dados.categorias:
                print(f'Categoria = {dado}')
            print(f'Motivo = {dados.motivo}')
        else:
            print(f'Dorama {dorama_pesquisar} nao foi encontrada na lista!')
        print('\n----------------------------------------\n')
            
###############################################DORAMAS ASSISTIDOS###################################################
                    
    def adicionar_doramas_assistidos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            categorias = []
            nome = input('Nome do dorama: ').capitalize().strip()
            if not nome: 
                print('Nome invalido! Tente novamente.')
                nome = input('Nome do dorama: ').capitalize().strip()
                
            total_eps = int(input('Total de episodios: '))
            if not total_eps:
                print('Total de episodios invalido! Tente novamente.')
                total_eps = int(input('Total de episodios: '))
                
            nota = float(input('Nota do dorama: '))
            if not nota:
                print('Nota invalida! Tente novamente.')
                nota = float(input('Nota do dorama: '))
                
            emissora = input('Emissora do dorama: ').capitalize().strip()
            if not emissora:
                print('Emissora invalida! Tente novamente.')
                emissora = input('Emissora do dorama: ').capitalize().strip()
                
            count = int(input('Quantas categorias tem o dorama: '))
            if not count:
                print('Quantidade de categorias invalida! Tente novamente.')
                count = int(input('Quantas categorias tem o dorama: '))
                
            for i in range(count):
                categoria = input(f'Digite a categoria {i+1}: ').capitalize().strip() 
                if not categoria:
                    print('Categoria invalida! Tente Novamente.')
                    categoria = input(f'Digite a categoria {i+1}: ').capitalize().strip() 
                categorias.append(categoria)
                
            data_view = input('Informe a data em que esta assistindo esse dorama: ').capitalize().strip()
            if not data_view:
                print('Data invalida! Tente novamente.')
                data_view = input('Informe a data em que esta assistindo esse dorama: ').capitalize().strip()
                
            if nome in self._doramas_assistidos:
                print(f'Dorama {nome} ja existe na lista de favoritos!')
            else:
                novo_dorama = Doramas_assistidos(nome, total_eps, nota, emissora, categorias, data_view)
                self._doramas_assistidos[nome] = novo_dorama
                print(f'Dorama {nome} adicionado aos assistidos.\n')
        else:
            print('Você nao possui permissao para adicionar doramas assistidos!')
        print('\n----------------------------------------\n')
        
    def listar_doramas_assistidos(self):
        if self._doramas_assistidos:
            for nome, dados in self._doramas_assistidos.items():
                print(f'Nome = {nome.capitalize()}')
                print(f'Total de epsodios = {dados.total_eps}')
                print(f'Nota = {dados.nota}')
                print(f'Emissora = {dados.emissora}')
                for dado in dados.categorias:
                    print(f'Categoria = {dado}')
                print(f'Data assistido = {dados.data_view}')
                print('------')   
        else:
            print('Nenhuma dorama foi adicionada aos assistidos.\n')
    
    def remover_doramas_assistidos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            while True:
                try:
                    dorama_nome = input('Dorama que voce deseja remover: ').capitalize().strip()
                    if not dorama_nome: 
                        print('Nome invalido! Tente novamente.')
                        continue
                    break
                except ValueError:
                    print('Valor invalido! Tente novamente.')
                break
            
            if dorama_nome in self._doramas_assistidos:
                del self._doramas_assistidos[dorama_nome]
                print('Dorama removido com sucesso!\n')
            else:
                print(f'Dorama {dorama_nome} nao encontrada!\n')
        else:
            print('Você nao possui permissao para remover doramas!')
        print('\n----------------------------------------\n')
            
    def atualizar_doramas_assistidos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            nome = input('Informe o dorama que deseja atualizar: ').capitalize().strip()
            if nome in self._doramas_assistidos:   
                print('1 - atualizar nome:')
                print('2 - atualizar total de epsodios:')
                print('3 - atualizar nota:')
                print('4 - atualizar emissora:')
                print('5 - atualizar categoria:')
                print('6 - atualizar data de assistido:')
                op = input('Informe o que deseja atualizar: ')
                dorama =  self._doramas_assistidos[nome]
                if op == '1':
                    novo_nome = input('Informe o novo nome do dorama: ').capitalize().strip()
                    if novo_nome:
                        dorama.atualizar_dorama(nome = novo_nome)
                        self._doramas_assistidos[novo_nome] = self._doramas_assistidos.pop(nome)
                    print(f'Dorama {nome} atualizado com sucesso!')
                       
                elif op == '2':
                    novo_total_eps = int(input('Informe o novo total de episodios: '))
                    if novo_total_eps:
                        dorama.atualizar_dorama(total_eps = novo_total_eps)
                    print(f'Dorama {nome} atualizado com sucesso!')
                    
                elif op == '3':
                    novo_nota = float(input('Informe a nova nota do dorama: '))
                    if novo_nota:
                        dorama.atualizar_dorama(nota = novo_nota)
                    print(f'Dorama {nome} atualizado com sucesso!')
                        
                elif op == '4':
                    novo_emissora = input('Informe a nova emissora do dorama: ').capitalize().strip()
                    if novo_emissora:
                        dorama.atualizar_dorama(emissora = novo_emissora)
                    print(f'Dorama {nome} atualizado com sucesso!')
                elif op == '5':
                    antiga_categoria = input('Antiga categoria do dorama: ').capitalize().strip()
                    nova_categoria = input('Informe a nova categoria do dorama: ').capitalize().strip()
                    for i in range(len(dorama.categorias)):
                        if antiga_categoria == dorama.categorias[i]:
                            dorama.categorias[i] = nova_categoria
                            break
                    print(f'Dorama {nome} atualizado com sucesso!')
                elif op == '6':
                    nova_data_view = input('Informe a nova data em que assistiu esse dorama: ').capitalize().strip()
                    if nova_data_view:
                        dorama.atualizar_dorama(data_view = nova_data_view)
                        print(f'Dorama {nome} atualizado com sucesso!')
                            
                else:
                    print('Opcao invalida!\n')
        else:
            print('Você nao possui permissao para atualizar doramas!')  
        print('\n----------------------------------------\n') 
    
    def pesquisar_doramas_assistidos(self):
        
        dorama_pesquisar = input('Informe o nome do dorama que deseja pesquisar: ').capitalize().strip()
        if not dorama_pesquisar:
            print('Nome invalido! Tente novamente.')
            dorama_pesquisar = input('Informe o nome do dorama que deseja pesquisar: ').capitalize().strip()
            
        if dorama_pesquisar in self._doramas_assistidos:
            dados = self._doramas_assistidos[dorama_pesquisar]
            print(f'Nome = {dorama_pesquisar.capitalize()}')
            print(f'Total de epsodios = {dados.total_eps}')
            print(f'Nota = {dados.nota}')
            print(f'Emissora = {dados.emissora}')
            for dado in dados.categorias:
                print(f'Categoria = {dado}')
            print(f'Motivo = {dados.data_view}')
            print('------')
        else:
            print(f'Dorama {dorama_pesquisar} nao foi encontrada na lista!')
        print('\n----------------------------------------\n')
                    
   
    def favoritar_doramas_assitidos(self):
        dorama_nome = input('Informe o nome do dorama que deseja favoritar: ').capitalize().strip()
        if not dorama_nome:
            print('Você nao possui permissao para favoritar doramas!')
            dorama_nome = input('Informe o nome do dorama que deseja favoritar: ').capitalize().strip()
            
        if dorama_nome in self._doramas_assistidos:
            dados = self._doramas_nao_assistidos[dorama_nome]
            motivo = input('Motivo por ter favoritado: ').strip()
            dorama = Dorama_Favorito(dorama_nome, dados.total_eps, dados.nota, dados.emissora, dados.categorias, dados.prioridade, motivo)
            self._doramas_favoritos[dorama_nome] = dorama
            
            del self._doramas_assistidos[dorama_nome]
            print(f'Dorama {dorama_nome} favoritado com sucesso!')
        else:
            print(f'Dorama {dorama_nome} nao foi encontrada na lista!')
        print('\n----------------------------------------\n')    

###############################################DORAMAS NAO ASSISTIDOS###################################################
 
    def adicionar_doramas_nao_assistidos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            categorias = []
            nome = input('Nome do dorama: ').capitalize().strip()
            if not nome: 
                print('Nome invalido! Tente novamente.')
                nome = input('Nome do dorama: ').capitalize().strip()
                
            total_eps = int(input('Total de episodios: '))
            if not total_eps:
                print('Total de episodios invalido! Tente novamente.')
                total_eps = int(input('Total de episodios: '))
                
            nota = float(input('Nota do dorama: '))
            if not nota:
                print('Nota invalida! Tente novamente.')
                nota = float(input('Nota do dorama: '))
                
            emissora = input('Emissora do dorama: ').capitalize().strip()
            if not emissora:
                print('Emissora invalida! Tente novamente.')
                emissora = input('Emissora do dorama: ').capitalize().strip()
                
            count = int(input('Quantas categorias tem o dorama: '))
            if not count:
                print('Quantidade de categorias invalida! Tente novamente.')
                count = int(input('Quantas categorias tem o dorama: '))
                
            for i in range(count):
                categoria = input(f'Digite a categoria {i+1}: ').capitalize().strip() 
                if not categoria:
                    print('Categoria invalida! Tente Novamente.')
                    categoria = input(f'Digite a categoria {i+1}: ').capitalize().strip() 
                categorias.append(categoria)
            
            prioridade = input(f'informe a prioridade do dorama: ').capitalize().strip()
            if not prioridade:
                print('prioridade invalida! Tente novamente.')
                prioridade = input(f'informe a prioridade do dorama: ').capitalize().strip()
            
            if nome in self._doramas_nao_assistidos:
                print(f'Dorama {nome} ja existe no dicionario de nao assistidos!')
            else:
                novo_dorama = Dorama_nao_assistidos(nome, total_eps, nota, emissora, categorias, prioridade)
                self._doramas_nao_assistidos[nome] = novo_dorama
                print(f'Dorama {nome} adicionado aos assistidos.\n')
        else:
            print('Você nao possui permissao para adicionar doramas!')
        print('\n----------------------------------------\n')
        
    def listar_doramas_nao_assistidos(self):
        if self._doramas_nao_assistidos:
            for nome, dados in self._doramas_nao_assistidos.items():
                print(f'Nome = {nome.capitalize()}')
                print(f'Total de epsodios = {dados.total_eps}')
                print(f'Nota = {dados.nota}')
                print(f'Emissora = {dados.emissora}')
                for dado in dados.categorias:
                    print(f'Categoria = {dado}')
                print(f'prioridade = {dados.prioridade}')
                print('------')  
        else:
            print('Nao existem doramas nao assistidos!')  
    
    def remover_doramas_nao_assistidos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            while True:
                try:
                    dorama_nome = input(f'Informe o nome do Dorama que deseja remover: ').capitalize().strip()
                    if dorama_nome not in self._doramas_nao_assistidos:
                        print('nOme inavalido!')
                        dorama_nome = input(f'Informe o nome do Dorama que deseja remover: ').capitalize().strip()
                        continue
                    break
                except ValueError:
                    print('Valor invalido! Tente novamente.')

            if dorama_nome in self._doramas_nao_assistidos:
                del self._doramas_nao_assistidos[dorama_nome]
                print('Dorama removido com sucesso!\n')
            else:
                print(f'Dorama {dorama_nome} nao encontrada!\n')
        else:
            print('Você nao possui permissao para remover doramas!')
        print('\n----------------------------------------\n')
            
    def atualizar_doramas_nao_assistidos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            nome = input('Informe o dorama que deseja atualizar: ').capitalize().strip()
            if nome in self._doramas_nao_assistidos:
                
                print('1 - atualizar nome:')
                print('2 - atualizar total de epsodios:')
                print('3 - atualizar nota:')
                print('4 - atualizar emissora:')
                print('5 - atualizar categoria:')
                print('6 - atualizar prioridade:')
                op = input('Informe o que deseja atualizar: ')
                dorama =  self._doramas_nao_assistidos[nome]
                if op == '1':
                    novo_nome = input('Informe o novo nome do dorama: ').capitalize().strip()
                    if novo_nome:
                        dorama.atualizar_dorama(nome = novo_nome)
                        self._doramas_nao_assistidos[novo_nome] = self._doramas_nao_assistidos.pop(nome) 
                    print(f'Dorama {nome} atualizado com sucesso!') 
                       
                elif op == '2':
                    novo_total_eps = int(input('Informe o novo total de episodios: '))
                    if novo_total_eps:
                        dorama.atualizar_dorama(total_eps = novo_total_eps)
                    print(f'Dorama {nome} atualizado com sucesso!')
                    
                elif op == '3':
                    novo_nota = float(input('Informe a nova nota do dorama: '))
                    if novo_nota:
                        dorama.atualizar_dorama(nota = novo_nota)
                    print(f'Dorama {nome} atualizado com sucesso!')
                        
                elif op == '4':
                    novo_emissora = input('Informe a nova emissora do dorama: ').capitalize().strip()
                    if novo_emissora:
                        dorama.atualizar_dorama(emissora = novo_emissora)
                    print(f'Dorama {nome} atualizado com sucesso!')
                    
                elif op == '5':
                    antiga_categoria = input('Antiga categoria do dorama: ').capitalize().strip()
                    nova_categoria = input('Informe a nova categoria do dorama: ').capitalize().strip()
                    for i in range(len(dorama.categorias)):
                        if antiga_categoria == dorama.categorias[i]:
                            dorama.categorias[i] = nova_categoria
                            break
                    print(f'Dorama {nome} atualizado com sucesso!')
                elif op == '6':
                    novo_prioridade = input('Informe a nova prioridade do dorama: ').capitalize().strip()
                    if novo_prioridade:
                        dorama.atualizar_dorama(prioridade = novo_prioridade)
                    print(f'Dorama {nome} atualizado com sucesso!')
                           
                else:
                    print('Opcao invalida!\n')
        else:
            print('Você nao possui permissao para atualizar doramas!')
        print('\n----------------------------------------\n')
            
    def pesquisar_doramas_nao_assistidos(self):
        while True:
            try:
                dorama_pesquisar = input('Informe o nome do dorama que deseja pesquisar: ').capitalize().strip()
                if not dorama_pesquisar:
                    print('Nome invalido! Tente novamente.')
                    continue
            except:
                print('Nome invalido! Tente novamente.')
                continue
            break
        if dorama_pesquisar in self._doramas_nao_assistidos:
            dados = self._doramas_nao_assistidos[dorama_pesquisar]
            print(f'Nome = {dorama_pesquisar.capitalize()}')
            print(f'Total de epsodios = {dados.total_eps}')
            print(f'Nota = {dados.nota}')
            print(f'Emissora = {dados.emissora}')
            for dado in dados.categorias:
                print(f'Categoria = {dado}')
            print(f'Prioridade = {dados.prioridade}')
        else:
            print(f'Dorama {dorama_pesquisar} nao foi encontrada na lista!')
        print('\n----------------------------------------\n')
            
    def assistir_doramas_nao_assistidos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            dorama_nome = input('Informe o nome do dorama que deseja confirmar que assistiu: ').capitalize().strip()
            if not dorama_nome:
                print('Nome invalido! Tente novamente.')
                dorama_nome = input('Informe o nome do dorama que deseja confirmar que assistiu: ').capitalize().strip()
            
            if dorama_nome in self._doramas_nao_assistidos:
                dados = self._doramas_nao_assistidos[dorama_nome]
                data = input('Informe a data que assistiu: ')
                dorama = Doramas_assistidos(dorama_nome, dados.total_eps, dados.nota, dados.emissora, dados.categorias, data)
                self._doramas_assistidos[dorama_nome] = dorama
                del self._doramas_nao_assistidos[dorama_nome]
            else:
                print(f'Dorama {dorama_nome} nao foi encontrada na lista!')
        else:
            print('Você nao possui permissao para assistir doramas!')
        print('\n----------------------------------------\n')

    def favoritar_doramas_nao_assistidos(self):
        if isinstance(self._usuario_atual, UsuarioPrimario):
            dorama_nome = input('Informe o nome do dorama que deseja favoritar: ').capitalize().strip()
            if not dorama_nome:
                print('Nome invalido! Tente novamente.')
                dorama_nome = input('Informe o nome do dorama que deseja favoritar: ').capitalize().strip()
                
            if dorama_nome in self._doramas_nao_assistidos:
                dados = self._doramas_nao_assistidos[dorama_nome]
                motivo = input('Motivo por ter favoritado: ').strip()
                dorama = Dorama_Favorito(dorama_nome, dados.total_eps, dados.nota, dados.emissora, dados.categorias, dados.prioridade, motivo)
                self._doramas_favoritos[dorama_nome] = dorama
                
                del self._doramas_nao_assistidos[dorama_nome]
                print(f'Dorama {dorama_nome} favoritado com sucesso!')
            else:
                print(f'Dorama {dorama_nome} nao foi encontrada na lista!')
        else:
            print('Você nao possui permissao para favoritar doramas!')
        print('\n----------------------------------------\n')

##########################################MENU GERENCIAR DORAMAS FAVORITOS###############################################

    def menu_favoritos(self):
        try:
            while True:
                print('==============================================')
                print('================Menu Favoritos================')
                print('1 - Adicionar doramas')
                print('2 - Listar doramas')
                print('3 - Remover dorama')
                print('4 - Pesquisar dorama')
                print('5 - Atualizar dorama')
                print('0 - Voltar ao menu gerenciador de doramas')
                opcao = input('Escolha uma opcao: ')
                print('==============================================\n')
                
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
                    print('Voltando para o menu gerenciador de doramas...')
                    break
        except Exception as e:
            print(f'Erro: {str(e)}')
    
##########################################MENU GERENCIAR DORAMAS ASSISTIDOS#############################################
        
    def menu_assistidos(self):
        try:
            while True:
                print('==============================================')
                print('===============Menu Assisitidos===============')
                print('1 - Adicionar doramas assistidos')
                print('2 - Listar doramas assistidos')
                print('3 - Remover dorama assistido')
                print('4 - Pesquisar dorama')
                print('5 - Atualizar dorama')
                print('6 - Favoritar dorama assistido')
                print('0 - Voltar ao menu gerenciador de doramas')
                opcao = input('Escolha uma opcao: ')
                print('==============================================\n')
                
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
                elif opcao == '6':
                    self.favoritar_doramas_assitidos()
                elif opcao == '0':
                    print('Voltando para o menu gerenciador de doramas...')
                    break
        except Exception as e:
            print(f'Erro: {str(e)}')

##########################################MENU GERENCIAR DORAMAS NAO ASSITIDOS##############################################
           
    def menu_nao_assistidos(self):
        try:
            while True:
                print('==============================================')
                print('=============Menu Não Assistidos==============')
                print('1. Adicionar doramas nao assistidos')
                print('2. Listar doramas nao assistidos')
                print('3. Remover dorama nao assistido')
                print('4. Pesquisar dorama nao assistido')
                print('5. Atualizar dorama nao assistido')
                print('6. Favoritar dorama nao assistido')
                print('7. Assistir dorama nao assistido')
                print('0 - Voltar ao menu gerenciador de doramas')
                opcao = input('Escolha uma opcao: ')
                print('==============================================\n')
                
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
                elif opcao == '6':
                    self.favoritar_doramas_nao_assistidos()
                elif opcao == '7':
                    self.assistir_doramas_nao_assistidos()
                elif opcao == '0':
                    print('Voltando para o menu gerenciador de doramas...')
                    break
        except Exception as e:
            print(f'Erro: {str(e)}')
 
 ##########################################MENU GERENCIAR DORAMAS###############################################
                
    def exibir_menu(self):
        try:
            while True:
                print('=====================Menu=====================\n')
                print('1 - Menu Doramas favoritos')
                print('2 - Menu Doramas assistidos')
                print('3 - Menu Doramas nao assistidos')
                print('0 - Voltar ao menu do sistema')
                opcao = input('Escolha uma opcao: ')
                print('==============================================\n')

                if opcao == '1':
                    self.menu_favoritos()
                elif opcao == '2':
                    self.menu_assistidos()
                elif opcao == '3':
                    self.menu_nao_assistidos()
                elif opcao == '0':
                    print('Voltando para o menu do sistema...')
                    break
        except Exception as e:
            print(f'Erro: {str(e)}')


 #####################################################################################################################
 ####################################################CLASSE SISTEMA###################################################  
 #####################################################################################################################
 

class Sistema:
    def __init__(self):
        self._usuarios = {}  
        self._gerenciar_doramas = GerenciarDoramas()  
        self._usuario_atual = None  

    def cadastrar_usuario(self):
        usuario_nome = input('Nome do usuario: ').strip().capitalize()
        if not usuario_nome:
            print('Nome do usuario invalido!\n')
            usuario_nome = input('Nome do usuario: ').strip().capitalize()
            
        usuario_cpf = input('CPF do usuario: ').strip().upper()
        if not usuario_cpf:
            print('CPF invalido!\n')
            usuario_cpf = input('CPF do usuario: ').strip().upper()
            
        usuario_senha = input('Senha do usuario: ').strip().upper()
        if not usuario_senha:
            print('Senha invalida!\n')
            usuario_senha = input('Senha do usuario: ').strip().upper()
            
        if usuario_cpf in self._usuarios:
            print('Usuario ja cadastrado!\n')
        else:
            tipo = input('Tipo de usuario [PRIMARIO = P or SECUNDARIO = S]: ').upper()
            if tipo == 'P':
                self._usuarios[usuario_nome] = UsuarioPrimario(usuario_nome, usuario_cpf, usuario_senha)
                print('Usuario primario cadastrado!\n')
            elif tipo == 'S':
                self._usuarios[usuario_nome] = UsuarioSecundario(usuario_nome, usuario_cpf, usuario_senha)
                print('Usuario secundario cadastrado!\n')
            else:
                print('Tipo de usuario invalido!\n')
            print('---------------------------\n')

    def login(self):
        usuario_nome = input('Nome do usuario: ').strip().capitalize()
        if not usuario_nome:
            print('Nome do usuario invalido!\n')
            usuario_nome = input('Nome do usuario: ').strip().capitalize()
            
        usuario_cpf = input('CPF do usuario: ').strip().upper()
        if not usuario_cpf:
            print('CPF invalido!\n')
            usuario_cpf = input('CPF do usuario: ').strip().upper()
            
        usuario_senha = input('Senha do usuario: ').strip().upper()
        if not usuario_senha:
            print('Senha invalida!\n')
            usuario_senha = input('Senha do usuario: ').strip().upper()

        if usuario_nome in self._usuarios:
            usuario = self._usuarios[usuario_nome]
            if usuario.cpf == usuario_cpf:
                autenticado, mensagem = usuario.autenticacao(usuario_senha)
                if autenticado:
                    self._usuario_atual = usuario
                    self._gerenciar_doramas.set_usuario_atual(usuario)
                    print(mensagem)
                    self._gerenciar_doramas.exibir_menu()
                else:
                    print(mensagem)
            else:
                print('CPF esta incorreto!\n')
        else:
            print('Usuario nao encontrado!\n')
        print('---------------------------------------------\n')
            
    def listar_usuarios(self):
        if self._usuarios:
            for usuario_nome, usuario in self._usuarios.items():
                print(f'Nome: {usuario_nome}, CPF: {usuario.cpf}')
                print('---------------------\n')
        else:
            print('Nenhum usuario cadastrado!\n')

#############################################MENU DO SISTEMA#################################################

    def menu(self):
        try:
            while True:
                print('===============================')
                print('Menu Principal:')
                print('1 - Cadastrar usuario')
                print('2 - Login')
                print('3 - Listar Usuarios')
                print('0 - Sair')
                print('-------------------------------')
                opcao = input('Escolha uma opcao: ')
                print('===============================')
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
                    print('Opcao invalida. Tente novamente.')
        except Exception as e:
            print(f'Erro: {str(e)}')
if __name__ == '__main__':
    sistema = Sistema()
    sistema.menu()