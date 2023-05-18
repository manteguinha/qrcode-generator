# Documentação do Gerador de Código QR

Este código é um gerador de códigos QR que utiliza a biblioteca `qrcode` e a biblioteca `PySimpleGUI` para criar uma interface gráfica simples.

## Requisitos

Você precisará das seguintes bibliotecas para executar este código:

- qrcode
- PySimpleGUI

Para instalar as bibliotecas necessárias, execute os seguintes comandos:

```sh
pip install qrcode
pip install PySimpleGUI
```

## Como usar

O código é um script que, quando executado, exibe uma janela com uma interface gráfica para inserir um link e selecionar um local para salvar o código QR gerado.

### Interface gráfica

A interface possui os seguintes campos e botões:

- **Link**: Campo para inserir o link que será transformado em código QR.
- **Onde deseja salvar a imagem?**: Botão "Buscar" para selecionar o diretório onde a imagem do código QR será salva.
- **Criar QR Code**: Botão para gerar o código QR com base no link fornecido e salvar a imagem no diretório selecionado.

## Estrutura do código

O código possui uma classe chamada `Tela` que contém a estrutura e a lógica da interface gráfica.

### Classe Tela

A classe `Tela` possui os seguintes métodos:

- `__init__(self)`: Construtor da classe. Define o layout da interface gráfica e cria a janela usando a biblioteca `PySimpleGUI`.
- `Iniciar(self)`: Método que inicia a interface gráfica e aguarda a interação do usuário. Quando o botão "Criar QR Code" é pressionado, verifica se todos os campos estão preenchidos e, em seguida, gera o código QR, salva a imagem no diretório selecionado e exibe uma mensagem de sucesso.

## Exemplo de uso

Para usar o gerador de código QR, siga estas etapas:

1. Salve o código em um arquivo chamado, por exemplo, `gerador_qrcode.py`.
2. Execute o script `gerador_qrcode.py`:

```sh
python gerador_qrcode.py
```

A janela da interface gráfica será exibida. Insira um link no campo "Link", selecione o diretório onde deseja salvar a imagem do código QR e clique no botão "Criar QR Code". A imagem será salva no diretório selecionado e uma mensagem de sucesso será exibida.
