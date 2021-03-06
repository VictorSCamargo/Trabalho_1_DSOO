from abc import ABC, abstractmethod


class AbstractCtrl(ABC):
    @abstractmethod
    def __init__(self):
        self.__tela = None
        self.__objetos = []
        self.__usuario_logado = None

    @abstractmethod
    def menu(self):
        while True:
            opcoes = []
            count = 0
            for objeto in self.__lista_de_objetos():
                count += 1
                opcoes.append("{} - Nome: {}.".format(count, objeto.nome)) #TODO revisar

            botao, opcao_selecionada = self.__tela.menu_opcoes(opcoes)

            print(botao)
            print(opcao_selecionada)

            # processa os botoes/valores lidos
            if botao is None:
                return None

            elif botao == 'SELECIONAR':
                if opcao_selecionada is None:
                    self.__tela.pop_up('Erro ao selecionar:', 'Favor selecionar uma opcao.')
                else:
                    return self.__lista_de_objetos()[opcao_selecionada]

            elif botao == 'NOVO':
                dados = self.__tela.menu_criacao('Registre a categoria.') #TODO revisar
                if dados is None:
                    return None
                else:
                    novo = self.novo(dados[0]) #TODO revisar
                    if novo is not None:
                        self.incluir(novo)

            elif botao == 'EXCLUIR':
                if opcao_selecionada is None:
                    self.__tela.pop_up('Erro ao excluir:', 'Favor selecionar uma opcao para excluir.')
                else:
                    self.excluir(opcao_selecionada)

            elif botao == 'EDITAR':
                if opcao_selecionada is None:
                    self.__tela.pop_up('Erro ao editar:', 'Favor selecionar uma opcao para editar.')
                else:
                    self.alterar(opcao_selecionada)
            else:
                return None

    @abstractmethod
    def novo(self, nome: str):
        try:
            if isinstance(nome, str): #TODO revisar
                return Categoria(nome, self.__usuario_logado)
            else:
                raise TypeError
        except TypeError:
            self.__tela.pop_up("Falha ao criar objeto:", "Variavel de entrada em formato invalido.")
            return None

    @abstractmethod
    def busca(self, nome: str):
        for objeto in self.__lista_de_objetos():
            if objeto.nome == nome: #TODO revisar
                return objeto
        else:
            return None

    @abstractmethod
    def incluir(self, objeto_novo):
        try:
            if isinstance(objeto_novo, Categoria): #TODO revisar
                for objeto in self.__lista_de_objetos():
                    if objeto.nome == objeto_novo.nome: #TODO revisar
                        raise TypeError
                else:
                    self.__lista_de_objetos().append(objeto_novo)
                    self.__tela.pop_up("Sucesso.", "Objeto incluido no sistema.")
            else:
                raise TypeError
        except TypeError:
            self.__tela.pop_up("Falha ao incluir objeto:", "Variavel de entrada em formato invalido.")
        except Exception:
            self.__tela.pop_up("Falha ao incluir objeto:", "Ja incluido no sistema.")

    @abstractmethod
    def excluir(self, index_opcao):
        del self.__lista_de_objetos()[index_opcao]

    @abstractmethod
    def alterar(self, index_opcao):
        objeto_selecionado = self.__lista_de_objetos()[index_opcao]
        while True:
            dados = self.__tela.menu_criacao('Insira as novas informacoes.')
            if dados is None:
                return None
            else:
                nome = dados[0] #TODO revisar

                for objeto in self.__lista_de_objetos():
                    if objeto.nome == nome: #TODO revisar
                        self.__tela.pop_up("Problema:", "Ja existe uma categoria com esses dados.")
                        break
                else:
                    objeto_selecionado.nome = nome
                    objeto_selecionado.cadastrador = self.__usuario_logado
                    return True
