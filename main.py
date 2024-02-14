import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel
from display import Display
from botoes import BotoesGrid

from qt_material import apply_stylesheet

if __name__ == '__main__':
    # ============ Gerenciamento "aplicação" ==============
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml') # qt-material (tema escuro)

    # ============= Gerenciamento "janela principal " ================
    # "QVBoxLayout" inicia uma janela vertical
    window = MainWindow() # módulo "main_window"

    # ================== Módulo botoes ===================
    # "QGridLayout" inicia uma janela de grade (linha e coluna)
    botoeGrid = BotoesGrid()  # adiciona "Display()" na janela de grade (linha e coluna)
    window.vertical_layout.addLayout(botoeGrid) # adiciona "BotoesGrid()" na janela principal

    # informacao_display = Info() # exibir informacao_display acima do display
    # window.addWidgetLayout(botoeGrid) # método widgets (módulo "main_window")

     # ================== Módulo display ===================
    display = Display() # campo de inserção de data (dd/mm/aaaa)
    window.addWidgetLayout(display) # método widgets (módulo "main_window")

    # ======== Ajuste tamanho da janela principal =========
    # métopo para ajuste tamanho da janela window (módulo "main_window")
    window.adjustFixedSize()
    # =================== Exibição e loop =================
    window.show() # mostrar janela
    app.exec()  # O loop da aplicação
