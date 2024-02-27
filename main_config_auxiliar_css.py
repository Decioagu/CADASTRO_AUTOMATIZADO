# ============ Configurar estilo texto_titulo "main" ==============
def configTextoTitulo(texto_titulo):
    texto_titulo.setStyleSheet('font-size: 40px; color: white') # tamanho e cor

# ============ Configurar estilo texto_botao_executar "main" ==============
def configTexto(texto_botao_executar):

        # estilo do texto (cor, tamanho)
        texto_botao_executar.setStyleSheet('font-size: 20px; color: green')

        # dimensão espaço do texto (tamanho máximo)
        texto_botao_executar.setMaximumSize(300,100) # definir a "altura" mínima de um widget
