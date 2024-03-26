import sys
import hashlib
import configparser
import winreg
from PyQt5.QtWidgets import QApplication, QWidget
from methods.keyinterface import Ui_FormKeys

class Keys(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FormKeys()
        self.ui.setupUi(self)
        self.hash_value = None

        self.ui.radioButton.toggled.connect(self.set_passwd)
        self.ui.radioButton_2.toggled.connect(self.set_elkey)
        self.ui.pushButton.clicked.connect(self.close_win)
        self.ui.pushButton_2.clicked.connect(self.save_params)

        self.ui.radioButton.setChecked(True)

    def set_passwd(self):
        if self.ui.radioButton.isChecked():
            self.ui.label.setText("Пароль:")
            self.ui.label_2.setText("Пароль еще раз:")

    def set_elkey(self):
        if self.ui.radioButton_2.isChecked():
            self.ui.label.setText("ProductID:")
            self.ui.label_2.setText("VendorID")

    def close_win(self):
        self.close()
    def save_params(self):
        if self.ui.radioButton.isChecked():
            hash_object = hashlib.sha256(self.ui.lineEdit.text().encode('utf-8'))
            self.hash_value = hash_object.hexdigest()

            config = configparser.ConfigParser()
            config['SETTINGS'] = {'hash_value': self.hash_value}

            with open('pwd.ini', 'w') as configfile:
                config.write(configfile)

            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\WallMall")  # открываем или создаем ключ
            winreg.SetValueEx(key, "passwd", 0, winreg.REG_SZ, "1")  # записываем значение

            winreg.CloseKey(key)  # закрываем ключ
        elif self.ui.radioButton_2.isChecked():
            config = configparser.ConfigParser()

            # Загружаем существующий файл настроек, если он есть
            config.read('settings.ini')

            # Получаем значения из QLineEdit и QLineEdit_2
            hash_value = self.ui.lineEdit.text()
            hash_value_2 = self.ui.lineEdit_2.text()

            # Записываем хеши в файл настроек
            config['Hashes'] = {
                'prod': hash_value,
                'vend': hash_value_2
            }

            # Сохраняем изменения в файл
            with open('settings.ini', 'w') as configfile:
                config.write(configfile)
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\WallMall")  # открываем или создаем ключ
            winreg.SetValueEx(key, "phykey", 0, winreg.REG_SZ, "1")  # записываем значение

            winreg.CloseKey(key)  # закрываем ключ



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Keys()
    window.show()
    sys.exit(app.exec_())
