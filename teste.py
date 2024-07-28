class Dorama:
    def __init__(self, nome, total_eps, nota, emissora):
        self._nome = nome
        self._total_eps = total_eps
        self._nota = nota
        self._emissora = emissora

class Dorama_Favorito(Dorama):
    def __init__(self, nome, total_eps, nota, emissora):
        super().__init__(nome, total_eps, nota, emissora)

    def para_dict(self):
        return {
            'nome': self._nome,
            'total_eps': self._total_eps,
            'nota': self._nota,
            'emissora': self._emissora
        }

class GerenciarDoramas:
    def __init__(self):
        self._doramas_favoritos = {}  # Dicionário para armazenar doramas favoritos

    def adicionar_doramas_favoritos(self):
        nome = input('Nome do dorama: ')
        total_eps = int(input('Total de episódios: '))
        nota = float(input('Nota do dorama: '))
        emissora = input('Emissora do dorama: ')

        # Verificar se o dorama já existe na lista de favoritos
        if nome in self._doramas_favoritos:
            print(f'Dorama {nome} já existe na lista de favoritos!')
            return  # Interromper a execução se o dorama já estiver na lista

        # Criar uma instância do Dorama_Favorito
        novo_dorama = Dorama_Favorito(nome, total_eps, nota, emissora)
        # Adicionar o dorama ao dicionário de favoritos
        self._doramas_favoritos[nome] = novo_dorama.para_dict()
        print(f'Dorama {nome} adicionado aos favoritos.')

    def listar_doramas(self):
        if not self._doramas_favoritos:
            print("Nenhum dorama na lista de favoritos.")
            return

        print("Lista de doramas favoritos:")
        for nome, dados in self._doramas_favoritos.items():
            print(f"Nome: {nome}")
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
            print("------")

    def remover_dorama(self):
        nome = input('Nome do dorama que você deseja remover: ')

        if nome in self._doramas_favoritos:
            del self._doramas_favoritos[nome]
            print(f'Dorama {nome} removido com sucesso!')
        else:
            print(f'Dorama {nome} não encontrada!')

    def atualizar_dorama(self):
        nome_atual = input('Nome do dorama que você deseja atualizar: ')

        if nome_atual in self._doramas_favoritos:
            novo_nome = input('Novo nome (deixe em branco para manter o atual): ')
            novo_total_eps = input('Novo total de episódios (deixe em branco para manter o atual): ')
            novo_nota = input('Nova nota (deixe em branco para manter a atual): ')
            novo_emissora = input('Nova emissora (deixe em branco para manter a atual): ')

            dados = self._doramas_favoritos[nome_atual]
            
            # Atualizar apenas os campos fornecidos
            if novo_nome:
                dados['nome'] = novo_nome
                self._doramas_favoritos[novo_nome] = self._doramas_favoritos.pop(nome_atual)
            if novo_total_eps:
                dados['total_eps'] = int(novo_total_eps)
            if novo_nota:
                dados['nota'] = float(novo_nota)
            if novo_emissora:
                dados['emissora'] = novo_emissora

            print(f'Dorama {novo_nome if novo_nome else nome_atual} atualizado com sucesso!')
        else:
            print(f'Dorama {nome_atual} não encontrada!')

    def exibir_menu(self):
        while True:
            print("\nMenu:")
            print("1. Adicionar doramas favoritos")
            print("2. Listar doramas favoritos")
            print("3. Remover dorama favorito")
            print("4. Atualizar dorama favorito")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.adicionar_doramas_favoritos()
            elif opcao == '2':
                self.listar_doramas()
            elif opcao == '3':
                self.remover_dorama()
            elif opcao == '4':
                self.atualizar_dorama()
            elif opcao == '5':
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Exemplo de uso
gerenciar = GerenciarDoramas()
gerenciar.exibir_menu()
