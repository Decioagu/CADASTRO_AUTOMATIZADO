from PySide6.QtWidgets import QLineEdit

class Display(QLineEdit):
    # ============ Construtor ==============
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle() # configuração estilo do texto

    # ======================== Método ============================
    def configStyle(self): # (QLineEdit) configuração do display

        # estilo do texto (cor, tamanho)
        self.setStyleSheet(f'color: black; background-color: #2D9596; font-size: 30px')

        # dimensão espaço do texto (tamanho máximo)
        self.setMaximumSize(200, 70) # (largura, altura)




