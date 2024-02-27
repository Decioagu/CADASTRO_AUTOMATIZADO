from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox

#  Superclasse QMainWindow()
class MainWindow(QMainWindow):
    # ============ Construtor ==============
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # ============= Gerenciamento "janela" ================
        self.cw = QWidget() # criar "janela principal"
        self.setCentralWidget(self.cw) # definir o conteúdo exibido no centro da janela principal

        # =========== Gerenciamento Layout "janela principal"============
        self.vertical_layout = QVBoxLayout() # widgets verticalmente
        self.cw.setLayout(self.vertical_layout) # método = "Classe Container" para layout

        self.setWindowTitle('Diário Oficial') # Título da janela

    # ======================= Métodos =========================
    # Estilo da "janela principal"
    def adjustFixedSize(self):
        self.adjustSize() # usado para ajustar o tamanho de um widget ou janela
        self.setFixedSize(self.width(), self.height()) # ajuste fixo automático conforme conteúdo (largura, altura)

    # Criar widgets
    def addWidgetLayout(self, widget: QWidget):
            self.vertical_layout.addWidget(widget) # widgets interfaces gráficas do usuário

    # caixa de diálogo para usuário
    def makeMsgBox(self):
        return QMessageBox(self)


