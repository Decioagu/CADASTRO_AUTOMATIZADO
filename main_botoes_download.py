from threading import Thread
from time import sleep

from PySide6.QtWidgets import QPushButton, QGridLayout, QLabel
from PySide6.QtCore import Slot, Qt

from download_pdf import download_pfd, verifica_conexao_internet
from Etapa_01_pdf_em_txt import pdf_em_txt
from Etapa_02_selecionar_paragrafo import selecionar_paragrafo
from Etapa_03_cadastro import cadastrar_pessoas

from main_window import MainWindow
from main_display import Display

# criar botão e estilo
class Botoes(QPushButton):
    # ============ Construtor ==============
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle() # método

    # ======================== Método ============================
    def configStyle(self):

        # dimensão espaço do texto (tamanho máximo)
        self.setMaximumSize(75, 75) # (largura, altura)

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
                                font-size: 20px
                            """)



class BotoesDownloadGrid(QGridLayout, QLabel, Qt):
    # ============ Construtor ==============
    def __init__(self, window: MainWindow, display: Display,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # ================== Módulo display ===================
        self.display = display
        print(self.display.text())

        # ==== Gerenciamento "Barra de Status"  janela principal ====
        self.window = window
        self.status_bar = window.statusBar()

        # ================= Região Rio de Janeiro ===================
        # configure texto acima do botão
        self.regiao_rio_de_janeiro = QLabel("Rio de Janeiro") # adicionar texto
        self.addWidget(self.regiao_rio_de_janeiro, 0, 1, alignment=Qt.AlignCenter) # (widget, linha, coluna, expandir_linha, expandir_coluna)
        self.regiao_rio_de_janeiro.setStyleSheet('font-size: 20px; color: green; min-width: 150px') # tamanho e cor
        # configure botão
        self.botao1 = Botoes('RJ') # método botão
        self.addWidget(self.botao1, 1, 1, alignment=Qt.AlignCenter) # (widget, linha, coluna, alinhamento)
        self.botao1.clicked.connect(self.botao_clicado) # .clicked verifica se botão foi clicado pelo usuário)

        # # ================= Região Duque de Caxias ==================
        # # configure texto acima do botão
        # self.duque_de_caixas = QLabel("Duque de Caxias") # adicionar texto
        # self.addWidget(self.duque_de_caixas, 0, 2, alignment=Qt.AlignCenter) # (widget, linha, coluna, expandir_linha, expandir_coluna)
        # # configure botão
        # self.duque_de_caixas.setStyleSheet('font-size: 20px; color: green; min-width: 180px') # tamanho e cor
        # self.botao2 = Botoes('DQ') # método botão
        # self.addWidget(self.botao2, 1, 2, alignment=Qt.AlignCenter)

        # # ================= Região Duque de Caxias ==================
        # # configure texto acima do botão
        # self.arraial_do_cabo = QLabel("Arraial do Cabo") # adicionar texto
        # self.addWidget(self.arraial_do_cabo, 0, 3, alignment=Qt.AlignCenter) # (widget, linha, coluna, expandir_linha, expandir_coluna)
        # # configure botão
        # self.arraial_do_cabo.setStyleSheet('font-size: 20px; color: green; min-width: 150px') # tamanho e cor
        # self.botao2 = Botoes('AC') # método botão
        # self.addWidget(self.botao2, 1, 3, alignment=Qt.AlignCenter)

    @Slot()
    def botao_clicado(self):
        Thread(target=self.download_status_bar).start() # executar em paralelo
        Thread(target=self.executar_download).start() # executar em paralelo

    @Slot()
    def executar_download(self):
        botao = self.sender() # Identifica o botão clicado

        conexao_internet = verifica_conexao_internet() # verifica conexão internet

        data = str(self.display.text()) # converte em string texto atual do "display"

        if botao.text() == 'RJ' and conexao_internet == "Conectado à internet!":
            print(f"Botão clicado: {botao.text()}") # Exibe o texto do botão clicado
            teste = download_pfd(data)
            if teste:
                Thread(target=self.processando_status_bar).start() # executar em paralelo
                Thread(target=self.executar_pasta).start() # executar em paralelo
        else:
            self.atualizar_status_bar() # mensagem barra de status

    @Slot()
    def executar_pasta(self):
        # executar funções (método do negocio)
        pdf_em_txt()
        selecionar_paragrafo()
        cadastrar_pessoas()

        self.status_bar.showMessage('Finalizado...') # mensagem barra de status
        Thread(target=self.atualizar_status_bar).start() # executar em paralelo

    @Slot()
    def download_status_bar(self):
        self.status_bar.showMessage('Download...')  # mensagem barra de status

    @Slot()
    def processando_status_bar(self):
        self.status_bar.showMessage('Processando...')  # mensagem barra de status

    @Slot()
    def atualizar_status_bar(self):
        conexao_internet = verifica_conexao_internet() # verifica conexão internet
        sleep(3) # aguardar
        self.status_bar.showMessage(conexao_internet) # mensagem barra de status












