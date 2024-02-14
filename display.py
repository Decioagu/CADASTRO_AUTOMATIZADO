from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QLabel


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self): # (QLineEdit) configuração do display

        # estilo do texto (cor, tamanho)
        self.setStyleSheet(f'background-color: red; font-size: 30px')

        # espaço margem do texto
        # margins = [TEXT_MARGIN for _ in range(4)]
        # self.setTextMargins(*margins) # configura margem de texto

        # dimensão espaço do texto
        self.setMinimumHeight(30 * 2) # definir a "altura" mínima de um widget
        self.setMinimumWidth(20) # definir a "largura" mínima de um widget
        self.setAlignment(Qt.AlignmentFlag.AlignCenter) # alinhamento pela direita
        



