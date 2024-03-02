import sys
from PyQt5.QtWidgets import QApplication, QWidget
from methods.keyinterface import Ui_FormKeys

class Keys(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FormKeys()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Keys()
    window.show()
    sys.exit(app.exec_())
