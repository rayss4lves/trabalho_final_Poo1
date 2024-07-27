class Dorama:
    def __init__(self, nome, total_eps, nota, emissora):
        self._nome = nome
        self._total_eps = total_eps
        self._nota = nota
        self._emissora = emissora

#arrumar as classes dos doramas e as suas respctivas funções
        
class Dorama_Favorito(Dorama):
        
    def __init__(self,nome, total_eps, nota, emissora):
        super().__init__(nome, total_eps, nota, emissora)
        self._doramas_favoritos = {}
        
    def adicionar_doramas(self, nome, total_eps, nota, emissora):
        
        dorama_favorito = Dorama_Favorito(nome, total_eps, nota, emissora)
        self._doramas_favoritos[dorama_favorito._nome] = dorama_favorito
    
    def remover_doramas(self, nome):
        pass   

class Dorama_assistidos(Dorama):
    def __init__(self,nome, total_eps, nota, emissora):
        super().__init__(nome, total_eps, nota, emissora)
        
class Dorama_nao_assistidos(Dorama):
    def __init__(self,nome, total_eps, nota, emissora):
        super().__init__(nome, total_eps, nota, emissora)
        
class GerenciarDoramas():
    def __init__(self):
        self._doramas = []
        self._doramas_favoritos = []
        self._doramas_assistidos = []
        self._doramas_nao_assistidos = []
        
    def adicionar_doramas(self, dorama):
        dorama = input('Nome do dorama: ')
        eps = int(input('Total de episódios: '))
        nota = float(input('Nota do dorama: '))
        emissora = input('Emissora do dorama: ')
        for dorama in self._doramas:
            if dorama._nome not in self._doramas:
                self._doramas[dorama._nome] = dorama
            else:
                print(f'Dorama {dorama._nome} já existe na lista!')
    
    def adicionar_doramas_favoritos(self, dorama):
        for dorama in self._doramas_favoritos:
            if dorama._nome in self._doramas_favoritos:
                self._doramas_favoritos[dorama._nome] = dorama
            else:
                print(f'Dorama {dorama._nome} não existe na lista!')
    
    def adicionar_doramas_assistidos(self, dorama):
        for dorama in self._doramas_assistidos:
            if dorama._nome in self._doramas_assistidos:
                self._doramas_assistidos[dorama._nome] = dorama
            else:
                print(f'Dorama {dorama._nome} não existe na lista!')
    
    def adicionar_doramas_nao_assistidos(self, dorama):
        for dorama in self._doramas_nao_assistidos:
            if dorama._nome in self._doramas_nao_assistidos:
                self._doramas_nao_assistidos[dorama._nome] = dorama
            else:
                print(f'Dorama {dorama._nome} não existe na lista!')
    
    def imprimir_doramas(self):
        print('Doramas:')
        for dorama in self._doramas.values():
            print(f'{dorama._nome} - Episodios: {dorama._total_eps}, Nota: {dorama._nota}, Emissora: {dorama._emissora}')
            
    def imprimir_doramas_favoritos(self):
        print('Doramas Favoritas:')
        for dorama in self._doramas_favoritos.values():
            print(f'{dorama._nome} - Episodios: {dorama._total_eps}, Nota: {dorama._nota}, Emissora: {dorama._emissora}')
            
    def imprimir_doramas_assistidos(self):
        print('Doramas Assistidas:')
        for dorama in self._doramas_assistidos.values():
            print(f'{dorama._nome} - Episodios: {dorama._total_eps}, Nota: {dorama._nota}, Emissora: {dorama._emissora}')
    
    def imprimir_doramas_nao_assistidos(self):
        print('Doramas Não Assistidas:')
        for dorama in self._doramas_nao_assistidos.values():
            print(f'{dorama._nome} - Episodios: {dorama._total_eps}, Nota: {dorama._nota}, Emissora: {dorama._emissora}')
            
    def assistir_dorama(self, dorama_nome):
        if dorama_nome in self._doramas_assistidos:
            del self._doramas_assistidos[dorama_nome]
            self._doramas_nao_assistidos[dorama_nome] = self._doramas[dorama_nome]
        else:
            print(f'Dorama {dorama_nome} não está assistindo!')
    
    def favoritar_dorama_assitidos(self, dorama_nome):
        if dorama_nome in self._doramas_assistidos:
            del self._doramas_assistidos[dorama_nome]
            self._doramas_favoritos[dorama_nome] = self._doramas[dorama_nome]
        else:
            print(f'Dorama {dorama_nome} não está assistindo!')
            
    def favoritar_dorama_nao_assistidos(self, dorama_nome):
        if dorama_nome in self._doramas_nao_assistidos:
            del self._doramas_nao_assistidos[dorama_nome]
            self._doramas_favoritos[dorama_nome] = self._doramas[dorama_nome]
        else:
            print(f'Dorama {dorama_nome} não está não assistindo!')
            
    def remover_dorama(self, dorama_nome):
        if dorama_nome in self._doramas:
            del self._doramas[dorama_nome]
        else:
            print(f'Dorama {dorama_nome} não existe na lista!')
    
    def pesquisar_doramas(self, nome_pesquisa):
        print('Resultado da Pesquisa:')
        for dorama in self._doramas.values():
            if nome_pesquisa.lower() in dorama._nome.lower():
                print(f'{dorama._nome} - Episodios: {dorama._total_eps}, Nota: {dorama._nota}, Emissora: {dorama._emissora}')
                
    def relatorio_doramas_assistidas(self):
        pass
    def relatorio_doramas_favoritos(self):
        print('Relatório das Doramas Mais Favoritas:')
        favoritas = sorted(self._doramas_favoritos.items(), key=lambda x: x[1]._total_eps, reverse=True)
        for dorama, total_eps in favoritas[:10]:
            print(f'{dorama._nome} - Episodios: {total_eps._total_eps}, Nota: {total_eps._nota}, Emissora: {total_eps._emissora}')
            
    def remover_doramas(self):
        dorama = input('Informe o nome do dorama que voce deseja remover: ')
        for dorama in self._doramas:
            if dorama._nome == self._doramas:
                del self._doramas[dorama]
                print(f'Dorama {dorama} removida com sucesso!')
            else:
                print(f'Dorama {dorama} não encontrada!')
                
    def remover_doramas_favoritos(self):
        dorama = input('Informe o nome do dorama que voce deseja remover: ')
        for dorama in self._doramas:
            if dorama._nome == self._doramas_favoritos:
                del self._doramas_favoritos[dorama]
                print(f'Dorama {dorama} removida com sucesso!')
            else:
                print(f'Dorama {dorama} não encontrada!')
                
    def remover_doramas_assistidos(self):
        dorama = input('Informe o nome do dorama que voce deseja remover: ')
        for dorama in self._doramas:
            if dorama._nome == self._doramas_assistidos:
                del self._doramas_assistidos[dorama]
                print(f'Dorama {dorama} removida com sucesso!')
            else:
                print(f'Dorama {dorama} não encontrada!')


#Função para Atualizar Dados do Dorama
#Função para Listar Doramas por Categoria
#Função para Contar Quantidade de Doramas por Categoria
#Função para Encontrar Doramas por Intervalo de Episódios
#Função para Agrupar Doramas por Emissora
#  
              