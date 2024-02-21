from PySide6.QtWidgets import QPushButton, QGridLayout, QLabel
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt

from download_pdf import download_pfd, verifica_conexao_internet

class Botoes(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle() # método

    # ======================== Método ============================
    def configStyle(self):
        '''
        Em Python, o método .font() é usado para definir a fonte de um widget Tkinter.
        O método aceita um único argumento, que é uma tupla que especifica as
        propriedades da fonte.

        Python
        label = Label(root, text="Hello, world!")
        label.font = ("Arial", 12, "bold italic") # (fonte, tamanho, estilo)
        # '''
        self.setMaximumSize(75, 75) # (largura, altura)

        self.setStyleSheet(f"""
                                QPushButton {{
                                    background-color: #436850;
                                    color: white;
                                }}
                                :hover {{
                                    background-color: #12372A;
                                    color: white;
                                }}
                                :pressed {{
                                    background-color: #201658;
                                    color: white;
                                }};
                                font-size: 20px
                            """)



class BotoesGrid(QGridLayout, QLabel, Qt):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # ================= Região Rio de Janeiro ==================
        # configure texto acima do botão
        self.regiao_rio_de_janeiro = QLabel("Rio de Janeiro") # adicionar texto
        self.addWidget(self.regiao_rio_de_janeiro, 0, 1, alignment=Qt.AlignCenter) # (widget, linha, coluna, expandir_linha, expandir_coluna)
        self.regiao_rio_de_janeiro.setStyleSheet('font-size: 20px; color: green') # tamanho e cor
        # configure botão
        self.botao1 = Botoes('RJ') # método botão
        self.addWidget(self.botao1, 1, 1, alignment=Qt.AlignCenter)
        self.botao1.clicked.connect(self.botao_clicado) # .clicked verifica se botão foi clicado pelo usuário)

        # # ================= Região Duque de Caxias ==================
        # # configure texto acima do botão
        # self.duque_de_caixas = QLabel("Duque de Caxias") # adicionar texto
        # self.addWidget(self.duque_de_caixas, 0, 3, alignment=Qt.AlignCenter) # (widget, linha, coluna, expandir_linha, expandir_coluna)
        # # configure botão
        # self.duque_de_caixas.setStyleSheet('font-size: 20px; color: green') # tamanho e cor
        # self.botao2 = Botoes('DQ') # método botão
        # self.addWidget(self.botao2, 1, 3, alignment=Qt.AlignCenter)

    @Slot()
    def botao_clicado(self):
        botao = self.sender() # Identifica o botão clicado
        conexao_internet = verifica_conexao_internet()

        if botao.text() == 'RJ' and conexao_internet == "Conectado à internet!":
            print(f"Botão clicado: {botao.text()}") # Exibe o texto do botão clicado
            download_pfd()











