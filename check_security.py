import winreg
import sys
from PyQt5 import QtWidgets
from sec_ui import Ui_Form
from main import Client
from methods.face_detect import FaceRecognitionApp

key_path = r"Software\WallMall"


class Security(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        if self.check_registry_key(key_path, "face") and self.check_registry_key(key_path, "passwd"):
            self.face_recognition_app = FaceRecognitionApp()
            self.face_recognition_app.show()
            self.ui.label_2.setVisible(False)
            self.ui.label_3.setVisible(False)
            self.ui.progressBar.setVisible(False)
            print("Ключ Software\WallMall существует под именем face и под именем passwd с тем же значением")

        elif self.check_registry_key(key_path, "face") and self.check_registry_key(key_path, "phykey"):
            self.face_recognition_app = FaceRecognitionApp()
            self.face_recognition_app.show()
            self.ui.label.setVisible(False)
            self.ui.lineEdit.setVisible(False)
            self.ui.label_3.setVisible(False)
            self.ui.progressBar.setVisible(False)
            print("Ключ Software\WallMall существует под именем face и под именем phykey с тем же значением")

        else:
            self.myapp = Client()
            self.myapp.show()

            self.ui.frame.setVisible(False)

    def check_registry_key(self, key, value):
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key)
            registry_value, _ = winreg.QueryValueEx(registry_key, value)
            return registry_value == "1"
        except FileNotFoundError:
            return False
        except Exception as e:
            print("An error occurred while checking registry key:", e)
            return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Security()
    myapp.show()
    sys.exit(app.exec_())
