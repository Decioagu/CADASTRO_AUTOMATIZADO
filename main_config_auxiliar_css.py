def configTextoTitulo(texto_titulo): # (QLineEdit) configuração do display
    texto_titulo.setStyleSheet('font-size: 40px; color: white') # tamanho e cor

def configTextoBotao(texto_botao_executar): # (QLineEdit) configuração do display

        # estilo do texto (cor, tamanho)
        texto_botao_executar.setStyleSheet('font-size: 20px; color: green')

        # dimensão espaço do texto
        texto_botao_executar.setMaximumSize(300,100) # definir a "altura" mínima de um widget
