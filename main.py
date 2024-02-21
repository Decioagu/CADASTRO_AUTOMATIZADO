import sys
from time import sleep
from datetime import date
from threading import Thread

from PySide6.QtWidgets import QApplication, QLabel, QPushButton
from qt_material import apply_stylesheet
from PySide6.QtCore import Qt

from main_window import MainWindow
from main_display import Display
from main_botoes import BotoesGrid

from download_pdf import verifica_conexao_internet
from Etapa_01_pdf_em_txt import pdf_em_txt
from Etapa_02_selecionar_paragrafo import selecionar_paragrafo
from Etapa_03_cadastro import cadastrar_pessoas
from main_config_auxiliar_css import configTextoTitulo, configTextoBotao, configBotao

# botão executar
def botao_clicado():
    Thread(target=message_status_bar).start() # executar em paralelo
    Thread(target=executar_pasta).start() # executar em paralelo

def executar_pasta():
    pdf_em_txt()
    selecionar_paragrafo()
    cadastrar_pessoas()
    status_bar.showMessage('Finalizado...')
    Thread(target=atualizar_status_bar).start() # executar em paralelo

def message_status_bar():
    # Mostra a mensagem "Processando..." na barra de status
    status_bar.showMessage('Processando...')

def atualizar_status_bar():
    conexao_internet = verifica_conexao_internet()
    sleep(3)
    status_bar.showMessage(conexao_internet)

conexao_internet = verifica_conexao_internet()

if __name__ == '__main__':
    # ============ Gerenciamento "aplicação" ==============
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml') # qt-material (tema escuro)

    # ============= Gerenciamento "janela principal" ================
    # "QVBoxLayout" inicia uma janela vertical
    window = MainWindow() # módulo "main_window"

    # ============= Texto título "janela principal" ================
    texto_titulo = QLabel("Diário Oficial") # Texto título
    window.vertical_layout.addWidget(texto_titulo, alignment=Qt.AlignCenter) # adicionar "QLabel()" em "QVBoxLayout()"
    configTextoTitulo(texto_titulo)

    # ================== Módulo botoes ===================
    # "QGridLayout" inicia uma janela de grade (linha e coluna)
    botoeGrid = BotoesGrid()  # adiciona "Display()" na janela de grade (linha e coluna)
    window.vertical_layout.addLayout(botoeGrid) # adiciona "BotoesGrid()" na janela principal

     # ================== Módulo display ===================
    today = date.today() # data de hoje
    display = Display(today.strftime('%d/%m/%Y')) # campo de inserção de data (dd/mm/aaaa)
    window.addWidgetLayout(display) # método widgets (módulo "main_window")

    # ========== texto sobre botão executar widgets janela principal ==========
    texto_botao_executar = QLabel("Executar Pasta") # adicionar texto
    window.vertical_layout.addWidget(texto_botao_executar, alignment=Qt.AlignCenter)
    configTextoBotao(texto_botao_executar)

    # =================== botão executar widgets janela principal =====================
    botao_executar = QPushButton('Executar') # widget botão
    window.vertical_layout.addWidget(botao_executar, alignment=Qt.AlignCenter)
    configBotao(botao_executar)
    botao_executar.clicked.connect(botao_clicado)

    # == Gerenciamento "Barra de Status"  janela principal ==
    status_bar = window.statusBar() # usado para verificar status da janela principal (ação executada)
    status_bar.showMessage(conexao_internet) # ver mensagem (roda pé janela)

    # ======== Ajuste tamanho da janela principal ==========
    # métopo para ajuste tamanho da janela window (módulo "main_window")
    window.adjustFixedSize()
    # =================== Exibição e loop ==================
    window.show() # mostrar janela
    app.exec()  # O loop da aplicação
