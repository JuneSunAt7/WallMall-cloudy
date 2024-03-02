from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QHBoxLayout
from PyQt5.QtCore import QThread, QTimer, pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap
import cv2
import face_des

class FaceRecognitionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = face_des.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.back_clicked)
        self.ui.pushButton_3.clicked.connect(self.save_and_back_clicked)
        self.ui.pushButton_2.clicked.connect(self.continue_clicked)

        self.video = cv2.VideoCapture(0)
        # загружаем веса для распознавания лиц
        faceProto = "D:/programming/Python/WallMall-cloudy/WallMall-cloudy/security/opencv_face_detector.pbtxt"
        # и конфигурацию самой нейросети — слои и связи нейронов
        faceModel = "D:/programming/Python/WallMall-cloudy/WallMall-cloudy/security/opencv_face_detector_uint8.pb"
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

                cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/150)), 8)
                faceBoxes.append([x1, y1, x2, y2])

        return frameOpencvDnn, faceBoxes

    def back_clicked(self):
        print("Back button clicked")

    def save_and_back_clicked(self):
        print("Save and back button clicked")

    def continue_clicked(self):
        print("Continue button clicked")


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    gui = FaceRecognitionApp()
    gui.show()
    sys.exit(app.exec_())
