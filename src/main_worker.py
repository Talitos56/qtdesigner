import sys

from PySide6.QtWidgets import QApplication, QWidget

from worker import Ui_myWidget


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
