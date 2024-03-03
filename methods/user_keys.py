import sys
from PyQt5.QtWidgets import QApplication, QWidget
from methods.keyinterface import Ui_FormKeys

class Keys(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FormKeys()
        self.ui.setupUi(self)

        self.ui.radioButton.toggled.connect(self.set_passwd)
        self.ui.radioButton_2.toggled.connect(self.set_elkey)

        self.ui.radioButton.setChecked(True)

    def set_passwd(self):
        if self.ui.radioButton.isChecked():
            self.ui.label.setText("Пароль:")
            self.ui.label_2.setText("Пароль еще раз:")

    def set_elkey(self):
        if self.ui.radioButton_2.isChecked():
            self.ui.label.setText("ProductID:")
            self.ui.label_2.setText("VendorID")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Keys()
    window.show()
    sys.exit(app.exec_())
