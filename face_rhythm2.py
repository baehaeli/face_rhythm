import sys
import cv2
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "App"
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 800
        self.InitUI()

    def InitUI(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.label = QLabel(self)
        self.label.resize(400,100)
        self.label.move(100,100)
        movie =QMovie("/Users/baehaeli/Desktop/logo.gif")
        self.label.setMovie(movie)
        movie.start()
        self.label.setLayout(QHBoxLayout())


        btn1 = QPushButton('Game Start', self)
        btn1.move(200, 400)
        btn1.clicked.connect(self.btn1_onClick)

        btn2 = QPushButton('Setting', self)
        btn2.move(200, 500)
        btn2.clicked.connect(self.btn2_onClick)

        btn3 = QPushButton('Rank', self)
        btn3.move(200, 600)
        btn3.clicked.connect(self.btn3_onClick)

        self.show()

    @pyqtSlot()
    def btn1_onClick(self):
        self.statusBar().showMessage("Switched to window 1")
        self.cams = Window1()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def btn2_onClick(self):
        self.statusBar().showMessage("Switched to window 2")
        self.cams = Window2()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def btn3_onClick(self):
        self.statusBar().showMessage("Switched to window 2")
        self.cams = Window3()
        self.cams.show()
        self.close()


class Window1(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Game Start Window')
        self.setGeometry(100, 100, 500, 800)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        self.button.setIconSize(QSize(200, 200))

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Click me!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)
        self.game_screen()

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()

    def game_screen(self):
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
        while True:
            ret, frame = cap.read()
            frame = cv2.flip(frame,1)
            cv2.imshow("VideoFrame", frame)
            if cv2.waitKey(1) > 0: break

        cap.release()
        cv2.destroyAllWindows()



class Window2(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Setting')
        self.setGeometry(100, 100, 500, 800)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        self.button.setIconSize(QSize(200, 200))

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Click me!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()

class Window3(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Rank')
        self.setGeometry(100, 100, 500, 800)

        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        self.button.setIconSize(QSize(200, 200))

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Click me!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Window()
    sys.exit(app.exec_())