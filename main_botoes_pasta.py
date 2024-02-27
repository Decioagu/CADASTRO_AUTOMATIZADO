import shutil
from time import sleep
from pathlib import Path
from threading import Thread

from PySide6.QtWidgets import QPushButton, QGridLayout, QLabel
from PySide6.QtCore import Slot, Qt

from main_window import MainWindow

from download_pdf import verifica_conexao_internet
from Etapa_01_pdf_em_txt import pdf_em_txt
from Etapa_02_selecionar_paragrafo import selecionar_paragrafo
from Etapa_03_cadastro import cadastrar_pessoas

# criar botão e estilo
class Botoes(QPushButton):
    # ============ Construtor ==============
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle() # estilo

    # ======================== Método ============================
    def configStyle(self):
        # dimensão espaço do texto (tamanho máximo)
        self.setMaximumSize(150, 75) # (largura, altura)

        # cores do botão e tamanho da fonte
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
    # ============ Construtor ==============
    def __init__(self, window: MainWindow,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # ==== Gerenciamento "Barra de Status"  janela principal ====
        self.window = window
        self.status_bar = window.statusBar()

        # ================= Executar Pastas ==================
        # configure botão
        self.executar = Botoes('Executar') # criar botão e estilo do texto
        self.addWidget(self.executar, 1, 1, alignment=Qt.AlignCenter) # widget
        self.executar.clicked.connect(self.botao_clicado) # .clicked verifica se botão foi clicado pelo usuário)

        # ================== Limpar Pastas ===================
        # configure botão
        self.limpar = Botoes('Excluir') # criar botão e estilo do texto
        self.addWidget(self.limpar, 1, 2, alignment=Qt.AlignCenter) # widget
        self.limpar.clicked.connect(self.botao_clicado) # .clicked verifica se botão foi clicado pelo usuário)

    # ======================= Métodos =========================
    @Slot()
    def botao_clicado(self):
        botao = self.sender() # Identifica o botão clicado (texto)

        if botao.text() == 'Executar':
            print(f"Botão clicado: {botao.text()}") # Exibe o texto do botão clicado
            Thread(target=self.message_status_bar).start() # executar em paralelo
            Thread(target=self.executar_pasta).start() # executar em paralelo

        elif botao.text() == 'Excluir':
            self._show_excluir_('Deseja excluir arquivos e pastas?') # excluir pasta

    @Slot()
    def executar_pasta(self):
        # executar funções (método do negocio)
        pdf_em_txt()
        selecionar_paragrafo()
        cadastrar_pessoas()

        self.status_bar.showMessage('Finalizado...') # mensagem barra de status
        Thread(target=self.atualizar_status_bar).start() # executar em paralelo

    @Slot()
    def message_status_bar(self):
        self.status_bar.showMessage('Processando...')  # mensagem barra de status

    @Slot()
    def atualizar_status_bar(self):
        conexao_internet = verifica_conexao_internet() # verifica conexão internet
        sleep(3) # aguardar
        self.status_bar.showMessage(conexao_internet) # mensagem barra de status

    # mensagem de alerta
    def _show_excluir_(self, text):
        msgBox = self.window.makeMsgBox() # (módulo "main_window")
        msgBox.setText(text) # exibi texto na caixa de diálogo
        msgBox.setIcon(msgBox.Icon.Warning) # define o ícone da caixa de diálogo.
        msgBox.setWindowTitle("Deletar Pastas") # define o título da caixa de diálogo.
        msgBox.setStandardButtons(msgBox.StandardButton.Ok | msgBox.StandardButton.Cancel) # define os botões padrão da caixa de diálogo.
        msgBox.setButtonText(msgBox.StandardButton.Ok, "Confirmar") # renomear os botões padrão da caixa de diálogo
        msgBox.setButtonText(msgBox.StandardButton.Cancel, "Cancelar") # renomear os botões padrão da caixa de diálogo
        result = msgBox.exec() # executa a caixa de diálogo

        # opções de alerta
        if result == msgBox.StandardButton.Ok:
            print('Caixa de diálogo = "Confirmar"')
            # caminho do arquivo
            PASTA_RAIZ = Path(__file__).parent
            PASTA_PDF = PASTA_RAIZ / 'PDF'
            PASTA_CADASTROS = PASTA_RAIZ / 'CADASTROS'
            shutil.rmtree(PASTA_PDF, ignore_errors=True) # apagar pasta (delete)
            shutil.rmtree(PASTA_CADASTROS, ignore_errors=True) # apagar pasta (delete)
        elif result == msgBox.StandardButton.Cancel:
            print('Caixa de diálogo = "Cancelar"')


'''
Tipos de alignment em Qt:
Alinhamento horizontal:

Qt.AlignLeft: Alinha à esquerda.
Qt.AlignRight: Alinha à direita.
Qt.AlignHCenter: Alinha horizontalmente ao centro.
Alinhamento vertical:

Qt.AlignTop: Alinha ao topo.
Qt.AlignBottom: Alinha ao fundo.
Qt.AlignVCenter: Alinha verticalmente ao centro.
Combinações:

Qt.AlignCenter: Combina Qt.AlignHCenter e Qt.AlignVCenter.
Qt.AlignTop | Qt.AlignRight: Alinha ao topo e à direita.
'''









