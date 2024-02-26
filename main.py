import sys
from datetime import date

from PySide6.QtWidgets import QApplication, QLabel, QWidget
from qt_material import apply_stylesheet
from PySide6.QtCore import Qt

from main_window import MainWindow
from main_display import Display
from main_botoes_download import BotoesDownloadGrid
from main_botoes_pasta import BotoesPastaGrid

from download_pdf import verifica_conexao_internet
from main_config_auxiliar_css import configTextoTitulo, configTextoBotao

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

     # ========== texto sobre botão executar widgets janela principal ==========
    texto_definir_data = QLabel("Definir data download:") # adicionar texto
    window.vertical_layout.addWidget(texto_definir_data, alignment=Qt.AlignCenter)
    configTextoBotao(texto_definir_data)

    # ================== Módulo display ===================
    today = date.today() # data de hoje
    display = Display(today.strftime('%d/%m/%Y')) # campo de inserção de data (dd/mm/aaaa)
    window.vertical_layout.addWidget(display, alignment=Qt.AlignCenter) # adicionar "QLabel()" em "QVBoxLayout()"

    # ================== Módulo espaçamento ===================
    widget = QWidget()
    window.vertical_layout.addWidget(widget)
    widget.setStyleSheet('min-height: 20px')

    # ================== Módulo botoes ===================
    # "QGridLayout" inicia uma janela de grade (linha e coluna)
    botoes_download = BotoesDownloadGrid(window, display)  # adiciona "Display()" na janela de grade (linha e coluna)
    window.vertical_layout.addLayout(botoes_download) # adiciona "BotoesDownloadGrid()" na janela principal

    # ================== Módulo espaçamento ===================
    widget = QWidget()
    window.vertical_layout.addWidget(widget)
    widget.setStyleSheet('min-height: 20px')

    # ========== texto sobre botão executar widgets janela principal ==========
    texto_botao_executar = QLabel("Pastas") # adicionar texto
    window.vertical_layout.addWidget(texto_botao_executar, alignment=Qt.AlignCenter)
    configTextoBotao(texto_botao_executar)

    # =================== botão executar widgets janela principal =====================
    botoes_executar = BotoesPastaGrid(window) # widget botão
    window.vertical_layout.addLayout(botoes_executar) # adiciona "BotoesDownloadGrid()" na janela principal

    # # == Gerenciamento "Barra de Status"  janela principal ==
    status_bar = window.statusBar() # usado para verificar status da janela principal (ação executada)
    status_bar.showMessage(conexao_internet) # ver mensagem (roda pé janela)

    # ======== Ajuste tamanho da janela principal ==========
    # métopo para ajuste tamanho da janela window (módulo "main_window")
    window.adjustFixedSize()
    # =================== Exibição e loop ==================
    window.show() # mostrar janela
    app.exec()  # O loop da aplicação
