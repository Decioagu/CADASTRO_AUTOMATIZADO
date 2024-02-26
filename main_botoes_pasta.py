import shutil
from time import sleep
from pathlib import Path
from threading import Thread

from PySide6.QtWidgets import QPushButton, QGridLayout, QLabel
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt

from main_window import MainWindow

from download_pdf import verifica_conexao_internet
from Etapa_01_pdf_em_txt import pdf_em_txt
from Etapa_02_selecionar_paragrafo import selecionar_paragrafo
from Etapa_03_cadastro import cadastrar_pessoas

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
        self.setMaximumSize(150, 75) # (largura, altura)

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
                                font-size: 15px
                            """)


class BotoesPastaGrid(QGridLayout, QLabel, Qt):
    def __init__(self, window: MainWindow,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # ==== Gerenciamento "Barra de Status"  janela principal ====
        self.window = window
        self.status_bar = window.statusBar()

        # ================= Executar Pastas ==================
        # configure botão
        self.executar = Botoes('Executar') # método botão
        self.addWidget(self.executar, 1, 1, alignment=Qt.AlignCenter)
        self.executar.clicked.connect(self.botao_clicado) # .clicked verifica se botão foi clicado pelo usuário)

        # ================== Limpar Pastas ===================
        # configure botão
        self.limpar = Botoes('Excluir') # método botão
        self.addWidget(self.limpar, 1, 3, alignment=Qt.AlignCenter)
        self.limpar.clicked.connect(self.botao_clicado) # .clicked verifica se botão foi clicado pelo usuário)


    @Slot()
    def botao_clicado(self):
        botao = self.sender() # Identifica o botão clicado
        conexao_internet = verifica_conexao_internet()

        if botao.text() == 'Executar' and conexao_internet == "Conectado à internet!":
            print(f"Botão clicado: {botao.text()}") # Exibe o texto do botão clicado
            Thread(target=self.message_status_bar).start() # executar em paralelo
            Thread(target=self.executar_pasta).start() # executar em paralelo

        elif botao.text() == 'Excluir' and conexao_internet == "Conectado à internet!":
            self._show_excluir_('Deseja excluir pastas')

    @Slot()
    def executar_pasta(self):
        pdf_em_txt()
        selecionar_paragrafo()
        cadastrar_pessoas()
        self.status_bar.showMessage('Finalizado...')
        Thread(target=self.atualizar_status_bar).start() # executar em paralelo

    @Slot()
    def message_status_bar(self):
        # Mostra a mensagem "Processando..." na barra de status
        self.status_bar.showMessage('Processando...')

    @Slot()
    def atualizar_status_bar(self):
        conexao_internet = verifica_conexao_internet()
        sleep(3)
        self.status_bar.showMessage(conexao_internet)

    def _show_excluir_(self, text):
        msgBox = self.window.makeMsgBox() # (módulo "main_window")
        msgBox.setText(text) # exibi texto na caixa de diálogo
        msgBox.setIcon(msgBox.Icon.Warning) # define o ícone da caixa de diálogo.
        msgBox.setWindowTitle("Deletar Pastas") # define o título da caixa de diálogo.
        msgBox.setStandardButtons(msgBox.StandardButton.Ok | msgBox.StandardButton.Cancel) # define os botões padrão da caixa de diálogo.
        result = msgBox.exec() # executa a caixa de diálogo

        if result == msgBox.StandardButton.Ok:
            print('Caixa de diálogo = OK')
            # caminho do arquivo
            PASTA_RAIZ = Path(__file__).parent
            PASTA_PDF = PASTA_RAIZ / 'PDF'
            PASTA_CADASTROS = PASTA_RAIZ / 'CADASTROS'
            shutil.rmtree(PASTA_PDF, ignore_errors=True) # apagar pasta (delete)
            shutil.rmtree(PASTA_CADASTROS, ignore_errors=True) # apagar pasta (delete)
        elif result == msgBox.StandardButton.Cancel:
            print('Caixa de diálogo = Cancel')













