import qrcode
import PySimpleGUI as sg

class Tela:
    sg.theme('Dark')
    def __init__(self) :
        layout = [
            [sg.Text('Link', size=(4,0),  font=("Arial", 14)), sg.Input(size=(55,0),  font=("Arial", 12) , key='_LINK_')],  
            [sg.Text('Onde deseja salvar a imagem?',  font=("Arial", 12))],
            [ sg.FolderBrowse('Buscar',  font=("Arial", 12) , key='_BUSCAR_', button_color=('White', 'Gray')),sg.Input(size=(51,0), font=("Arial", 12))],   
            [sg.Button('Criar QR Code',  font=("Arial", 12) , button_color=('White', 'Green'))]
        ]
        self.janela = sg.Window("Gerador de codigo QR").layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            if self.button == sg.WINDOW_CLOSED:
                break
            
            if self.button == 'Criar QR Code':
                if self.values['_LINK_'] == '' or self.values['_BUSCAR_'] == '':
                    sg.Popup('Há campos vazios a serem preenchidos',  font=("Arial", 14) , title='Atenção')
                else:
                    link = self.values['_LINK_']
                    imagem_qr = qrcode.make(link)
                    caminho = self.values['_BUSCAR_']
                    imagem_qr.save(caminho+'\imagem_qrcode.png')
                    sg.Popup(f'O codigo QR foi salvo em: {caminho}',  font=("Arial", 14) , title='Sucesso!')
                
tela = Tela()
tela.Iniciar()
