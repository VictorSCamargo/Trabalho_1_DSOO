from visao.tela import Tela

class TelaUsuario(Tela):
    def __init__(self):
        pass

    def pedeTipoUsuario(self):
        print("Escolha o tipo de pessoa: \n1 - Pessoa Fisica \n2 - Pessoa Juridica\n")
        opcao = self._seleciona_opcao_int(2)
        super().imprime_linha_de_fechamento()
        return(opcao)
