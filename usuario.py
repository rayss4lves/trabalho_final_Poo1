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
            return False, 'Usuario informado nao tem permissao de login!'