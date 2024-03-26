import cv2
import dlib
import winreg
import os
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from methods.face_des import Ui_FormFace
from methods.user_keys import Keys

class FaceRecognitionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FormFace()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.back_clicked)
        self.ui.pushButton_3.clicked.connect(self.save_and_back_clicked)
        self.ui.pushButton_2.clicked.connect(self.continue_clicked)

        self.video = cv2.VideoCapture(0)
        # загружаем веса для распознавания лиц
        faceProto = "D:\programming\Python\WallMall-cloudy\WallMall-cloudy\methods\opencv_face_detector.pbtxt"
        # и конфигурацию самой нейросети — слои и связи нейронов
        faceModel = "D:\programming\Python\WallMall-cloudy\WallMall-cloudy\methods\opencv_face_detector_uint8.pb"
        self.faceNet = cv2.dnn.readNet(faceModel, faceProto)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        hasFrame, frame = self.video.read()
        if not hasFrame:
            return

        resultImg, faceBoxes = self.highlightFace(self.faceNet, frame)
        frameRGB = cv2.cvtColor(resultImg, cv2.COLOR_BGR2RGB)
        image = QImage(frameRGB.data, frameRGB.shape[1], frameRGB.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
        self.ui.frame.setPixmap(pixmap)

    def highlightFace(self, net, frame, conf_threshold=0.7):
        frameOpencvDnn = frame.copy()
        frameHeight = frameOpencvDnn.shape[0]
        frameWidth = frameOpencvDnn.shape[1]

        blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)
        net.setInput(blob)
        detections = net.forward()

        faceBoxes = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                x1 = int(detections[0, 0, i, 3] * frameWidth)
                y1 = int(detections[0, 0, i, 4] * frameHeight)
                x2 = int(detections[0, 0, i, 5] * frameWidth)
                y2 = int(detections[0, 0, i, 6] * frameHeight)

                cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 150)), 8)
                faceBoxes.append([x1, y1, x2, y2])

                # Извлечение лица из кадра
                face = frame[y1:y2, x1:x2]

                # Сохранение изображения лица
                self.save_face(face)
                # self.continue_clicked()


        return frameOpencvDnn, faceBoxes

    def back_clicked(self):
        print("Back button clicked")
        self.hide()

    def save_and_back_clicked(self):
        print("Save and back button clicked")
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\WallMall")  # открываем или создаем ключ
        winreg.SetValueEx(key, "face", 0, winreg.REG_SZ, "1")  # записываем значение

        winreg.CloseKey(key)  # закрываем ключ
        self.hide()

    def continue_clicked(self):
        print("Continue button clicked")

        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\WallMall")  # открываем или создаем ключ
        winreg.SetValueEx(key, "face", 0, winreg.REG_SZ, "1")  # записываем значение

        winreg.CloseKey(key)  # закрываем ключ
        self.keys = Keys()
        self.keys.show()
        self.hide()

    def save_face(self, face):
        if os.path.exists('str.jpg'):
            print('Файл существует')
        else:
            cv2.imwrite('str.jpg', face)
            print("saved")
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\WallMall")  # открываем или создаем ключ
        winreg.SetValueEx(key, "face", 0, winreg.REG_SZ, "1")  # записываем значение

        winreg.CloseKey(key)  # закрываем ключ



