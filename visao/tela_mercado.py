from visao.tela import Tela
from visao.tela_menu_basico import TelaMenuBasico
import PySimpleGUI as sg

class TelaMercado():
    def __init__(self):
        self.__init_components()

    def __init_components(self):
        sg.theme('DarkAmber')

    def menu_opcoes(self, opcoes: list):
        return TelaMenuBasico().open(opcoes, "Tela mercado", "Menu mercado")

    def menu_criacao(self, titulo: str):
        while True:
            layout = [
                [sg.Text(titulo,
                         size=(30, 1), font=('Arial', 15))],
                [sg.Text('Nome', size=(15, 1)), sg.InputText()],
                [sg.Text('End.', size=(15, 1)), sg.InputText()],
                [sg.Button('PRONTO'), sg.Button('CANCELAR')]
            ]
            window = sg.Window('Edicao de dados', default_element_size=(40, 1)).Layout(layout)

            button, values = window.Read()
            value_list = list(values.values())
            window.Close()

            if button == 'PRONTO':
                if '' in value_list:
                    self.pop_up('Erro: campo vazio', 'Preencha todos os campos.')
                else:
                    return value_list
            else:
                return None

    def pop_up(self, titulo: str, msg: str):
        TelaMenuBasico().pop_up(titulo, msg)