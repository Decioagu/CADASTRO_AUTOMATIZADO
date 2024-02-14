from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox, QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    # ============= Superclasse QMainWindow() ================
    # construtor
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # ============= Gerenciamento "janela" ================
        self.cw = QWidget() # classe para gerencia janela criada
        self.setCentralWidget(self.cw) # definir o conteúdo exibido no centro da janela principal

        # =========== Gerenciamento Layout "janela principal"============
        self.vertical_layout = QVBoxLayout() # classe de layout que alinha os widgets verticalmente
        self.cw.setLayout(self.vertical_layout) # método = "Classe Container" para layout

        self.setWindowTitle('Diário Oficial') # Título da janela

        self.texto = QLabel("Diário Oficial") # Texto título
        self.vertical_layout.addWidget(self.texto, alignment=Qt.AlignCenter) # adicionar "QLabel()" em "QVBoxLayout()"
        self.texto.setStyleSheet('font-size: 40px; color: white') # tamanho e cor

    # ======================= Métodos =========================
    # Janela principal
    def adjustFixedSize(self):
        self.adjustSize() # usado para ajustar o tamanho de um widget ou janela
        self.setFixedSize(self.width(), self.height()) # ajuste fixo automático conforme conteúdo (largura, altura)

    # Criar widgets
    def addWidgetLayout(self, widget: QWidget):
            self.vertical_layout.addWidget(widget) # widgets interfaces gráficas do usuário

    # caixa de diálogo para usuário
    def makeMsgBox(self):
        return QMessageBox(self)

