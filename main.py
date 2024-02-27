import sys
from datetime import date

from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtCore import Qt

from main_botoes_download import BotoesDownloadGrid
from main_botoes_pasta import BotoesPastaGrid
from main_window import MainWindow
from main_display import Display

from main_config_auxiliar_css import configTextoTitulo, configTexto
from download_pdf import verifica_conexao_internet

from qt_material import apply_stylesheet

# verificar conexão da internet
conexao_internet = verifica_conexao_internet()

if __name__ == '__main__':
    # ============ Gerenciamento "aplicação" ==============
    app = QApplication(sys.argv) # gerencia a aplicação
    apply_stylesheet(app, theme='dark_teal.xml') # qt-material (tema escuro)

    # ============= Gerenciamento "janela principal" ================
    # "QVBoxLayout" inicia uma janela vertical
    window = MainWindow() # módulo "main_window"

    # ============= Texto título "janela principal" ================
    texto_titulo = QLabel("Diário Oficial") # Texto título
    window.vertical_layout.addWidget(texto_titulo, alignment=Qt.AlignCenter) # widget
    configTextoTitulo(texto_titulo) # estilo do "texto_titulo"

     # ========== texto sobre botão executar widgets janela principal ==========
    texto_definir_data = QLabel("Definir data download:") # adicionar texto
    window.vertical_layout.addWidget(texto_definir_data, alignment=Qt.AlignCenter) # widget
    configTexto(texto_definir_data) # estilo do "texto_definir_data"

    # ================== Módulo display ===================
    today = date.today() # data de hoje
    display = Display(today.strftime('%d/%m/%Y')) # campo de inserção de data (dd/mm/aaaa)
    window.vertical_layout.addWidget(display, alignment=Qt.AlignCenter) # widget

    # ================== Módulo para espaçamento ===================
    espaco_01 = QWidget()
    window.vertical_layout.addWidget(espaco_01) # widget
    espaco_01.setStyleSheet('min-height: 20px') # estilo

    # ================== Módulo botoes ===================
    # "QGridLayout" inicia uma janela de grade (linha e coluna)
    botoes_download = BotoesDownloadGrid(window, display)  # adiciona "Display()" na janela de grade (linha e coluna)
    window.vertical_layout.addLayout(botoes_download) # widget

    # ================== Módulo para espaçamento ===================
    espaco_02 = QWidget()
    window.vertical_layout.addWidget(espaco_02) # widget
    espaco_02.setStyleSheet('min-height: 20px') # estilo

    # ==== texto sobre botão executar widgets janela principal ====
    texto_botao_executar = QLabel("Pasta local:") # adicionar texto
    window.vertical_layout.addWidget(texto_botao_executar, alignment=Qt.AlignCenter) # widget
    configTexto(texto_botao_executar) # estilo do "texto_botao_executar"

    # ========== botão executar widgets janela principal ==========
    botoes_executar = BotoesPastaGrid(window) # widget botão
    window.vertical_layout.addLayout(botoes_executar) # widget

    # ==== Gerenciamento "Barra de Status"  janela principal ====
    status_bar = window.statusBar() # usado para verificar status da janela principal (ação executada)
    status_bar.showMessage(conexao_internet) # ver mensagem (roda pé janela)

    # ======== Estilo "janela principal" ==========
    window.adjustFixedSize() # ajuste tamanho da janela window

    # =================== Exibição e loop ==================
    window.show() # mostrar janela
    app.exec()  # O loop da aplicação
