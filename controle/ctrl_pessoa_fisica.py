from abstract_ctrl import AbstractCtrl
from entidade.pessoa_fisica import PessoaFisica
from tela.tela_pessoa_fisica import TelaPessoaFisica

class PessoaFisicaCtrl(AbstractCtrl):
    def __init__(self):
        self.__usuarios = []
        self.__tela = TelaPessoaFisica

    def signin():
        info = self.__tela.telaSignin()
        self.__usuarios.append(PessoaFisica(info["nome"],info["numDoc"],info["email"]))
       
    def login():
        info = self.__tela.telaLogin()
        for usuario in self.__usuarios:
            if usuario.__numDoc == info["numDoc"] and usuario.__email == info["email"]:
                return(usuario)
        else:
            print("Usuario nao cadastrado")

    def novo(self):
        pass
  
    def busca(self):
        pass

    def incluir(self):
        pass

    def listar(self):
        pass

    def alterar(self):
        pass

    def excluir(self):
        pass

