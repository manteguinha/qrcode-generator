import qrcode
from tkinter.font import BOLD
import PySimpleGUI as sg

class Tela:
    sg.theme('Dark')
    def __init__(self) :
        layout = [
            [sg.Text('Link', size=(5,0)), sg.Input(size=(40,0), key='_LINK_')],  
            [sg.Text('Onde deseja salvar a imagem?')],
            [sg.FolderBrowse('Buscar', font=("Arial", 10, BOLD) , key='_BUSCAR_', button_color=('White', 'Gray')),sg.Input(size=(40,0))],   
            [sg.Button('Criar QR Code', font=("Arial", 10, BOLD) , button_color=('White', 'Green'))]
        ]
        self.janela = sg.Window("Gerador de codigo QR", font=("Arial", 12)).layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            if self.button == sg.WINDOW_CLOSED:
                break
            
            if self.button == 'Criar QR Code':
                if self.values['_LINK_'] == '' or self.values['_BUSCAR_'] == '':
                    sg.Popup('Há campos vazios a serem preenchidos', title='Atenção')
                else:
                    link = self.values['_LINK_']
                    imagem_qr = qrcode.make(link)
                    caminho = self.values['_BUSCAR_']
                    imagem_qr.save(caminho+'\imagem_qrcode.png')
                    sg.Popup(f'O codigo QR foi salvo em: {caminho}', title='Sucesso!')
                
tela = Tela()
tela.Iniciar()
