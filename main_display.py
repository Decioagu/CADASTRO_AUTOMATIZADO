from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QLabel

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self): # (QLineEdit) configuração do display

        # estilo do texto (cor, tamanho)
        self.setStyleSheet(f'background-color: #2D9596; font-size: 30px')

        # dimensão espaço do texto
        self.setMaximumSize(200, 70) # (largura, altura)




