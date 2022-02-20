import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
from PyQt5.Qt import QPixmap
from predict_captcha2 import Captcha


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.path_2_captcha = str()
        self.solved_captcha = str()
        self.captha_pixmap = QPixmap()

        uic.loadUi('window.ui', self)
        self.pushButton.clicked.connect(self.browse)
        self.pushButton_2.clicked.connect(self.predict)

    def clear_text_browser(self):
        self.textBrowser.clear()

    def load_captcha_image(self):
        self.captha_pixmap.load(self.path_2_captcha)
        scaled = self.captha_pixmap.scaled(160, 50)
        self.label_2.setPixmap(scaled)

    def browse(self):
        self.clear_text_browser()
        path_name: str = QFileDialog.getOpenFileName(self, 'Open File', './')[0]
        self.path_2_captcha = path_name
        self.load_captcha_image()

    def predict(self):
        captcha = Captcha()
        captcha.crop_captcha(path_name=self.path_2_captcha)
        self.solved_captcha: str = captcha.run_predict()
        captcha.delete_croped_image()
        self.textBrowser.append(self.solved_captcha)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("plastique")

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
