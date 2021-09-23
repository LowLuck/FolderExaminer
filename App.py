import sys
from PyQt5.QtWidgets import QApplication, QWidget
from Design.design import Ui_BigFolderFounder
from main import size_in_folder
import os


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

        self.ui.pushButton.clicked.connect(self.input_button)

    def initUI(self):
        self.ui = Ui_BigFolderFounder()
        self.ui.setupUi(self)

    def input_button(self):
        try:
            inp = self.ui.lineEdit.text()
            if os.path.isdir(inp):
                strin = 'Size in GB'
                for j in size_in_folder(inp):
                    strin += f'\n{j}'
                self.ui.textBrowser.setText(strin)
            else:
                self.ui.textBrowser.setText('Directory not found')
        except Exception:
            self.ui.textBrowser.setText('Error')


if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
