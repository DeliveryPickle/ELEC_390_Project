import sys

from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QInputDialog, QLineEdit, QFileDialog, \
    QDesktopWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
import pyqtgraph as pg
import pandas as pd
import classifier
import fillDataFrame as fd
import data_split
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'ELEC 390 Application'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 380
        self.initUI()

    def initUI(self):
        #Window Setup
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setStyleSheet("background-color: grey;")
        self.setStyleSheet("background-image : url(image2.png);")
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle = self.frameGeometry()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        #Button and Text Setup
        title = QLabel("ELEC 390 Application")
        title.setAlignment(Qt.AlignCenter)
        button = QPushButton('Open a CSV file', self)
        button.setToolTip('This opens a CSV file')
        button.clicked.connect(self.on_click)
        button.setStyleSheet("background-color: white;")

        #Layout Setup
        self.layout = QVBoxLayout()
        self.layout.addWidget(title)
        self.layout.addWidget(button)
        self.setLayout(self.layout)
        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        QFileDialog.setStyleSheet(self,"")
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "CSV (*.csv);;All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        return fileName

    def saveFileDialog(self, file):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        QFileDialog.setStyleSheet(self, "")
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","CSV (*.csv);;All Files (*)", options=options)
        if fileName:
            f = open(fileName, 'w')
            text = file.to_csv()
            f.write(text)
            f.close()

    @pyqtSlot()
    def on_click(self):
        fileName = self.openFileNameDialog()
        df = pd.read_csv(fileName)
        df = classifier.classify_input(df)
        df = fd.fillFrame(df)
        df = df.reset_index(drop=True)
        df = df.drop('maximum', axis = 1)
        df = df.drop('minimum', axis = 1)
        df = df.drop('standard deviation', axis = 1)
        df = df.drop('kurtosis', axis = 1)
        df = df.drop('variance', axis = 1)
        df = df.drop('skewness', axis = 1)
        df = df.drop('range', axis=1)
        df = df.drop('median', axis=1)
        df = df.drop('mean', axis=1)
        # df = df.loc[:,'type'].map(str)
        # df.loc['type'].replace('1','Jumping')
        # df.loc['type'].replace('0', 'Walking')
        print(df)
        #Graph Values
        time = df.loc[:,'Time (s)']
        #data = df.iloc[:,4]
        type = df.loc[:,'type']
        #Graph Setup
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('w')
        pen1 = pg.mkPen(color=(0, 0, 0))
        pen2 = pg.mkPen(color = (255, 0,0))
        # plot data: x, y values
        #self.graphWidget.plot(time, data, pen = pen1)
        self.graphWidget.plot(time, type, pen=pen2)
        self.layout.addWidget(self.graphWidget)
        self.saveFileDialog(df)

    def on_click_me(self):
        self.saveFileDialog()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    #QMainWindow().show()
    sys.exit(app.exec_())


