import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import beamforming_ui
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = beamforming_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())