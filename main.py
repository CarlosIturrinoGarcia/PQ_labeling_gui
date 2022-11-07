import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QMainWindow, QFileDialog, QMessageBox, QVBoxLayout, QGraphicsView
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import Qt
import pyqtgraph as pg
import scipy.io
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # create default constructor for QWidget
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """

        figure = Figure(figsize=(6, 5))
        self.chart_canvas = FigureCanvasQTAgg(figure)

        self.x = np.random.normal(size=1000)
        self.setGeometry(200, 100, 800, 600)
        self.setWindowTitle('Empty Window in PyQt')
        self.createMenu()
        self.setupPlotter(self.x)
        self.show()

    def createMenu(self):
        """
        Create skeleton with menu bar
        """
        # Exit Command
        exit_act = QAction('&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)

        # Open file Command
        open_act = QAction('&Open', self)
        open_act.setShortcut('Ctrl+O')
        open_act.triggered.connect(self.openFile)

        # Create menubar

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add actions
        file_menu = menu_bar.addMenu('File')
        tools_menu = menu_bar.addMenu('Tools')
        file_menu.addAction(open_act)
        file_menu.addAction(exit_act)

    def openFile(self):
        """
        Open a text or html file and display its contents in
        the text edit field.
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File",
                                                   "", "Mat Files (*.mat);;HTML Files (*.html);;Text Files (*.txt)")
        if file_name:
            if file_name[-4:] == '.mat':
                sig = scipy.io.loadmat(file_name)
                x = sig['Data1_V1i']
                self.updatePlotter(x)
            else:
                with open(file_name, 'r') as f:
                    sig = f.read()
                    self.text_field.setText(sig)
        else:
            QMessageBox.information(self, "Error",
                                    "Unable to open file.", QMessageBox.Ok)



    def setupPlotter(self, data):
        t = range(0, np.size(data))
        self.figure = Figure(figsize=(6,5))
        self.chart_canvas = FigureCanvasQTAgg(self.figure)
        self.axes = self.figure.add_subplot(111)
        self.PlotData(data)

    def updatePlotter(self,data):
        self.figure.clear()
        self.figure = Figure(figsize=(6, 5))
        self.chart_canvas = FigureCanvasQTAgg(self.figure)
        self.axes = self.figure.add_subplot(111)
        self.PlotData(data)


    def PlotData(self,data):
        self.axes.plot(data)
        self.tool = self.addToolBar(NavigationToolbar2QT(self.chart_canvas, self))
        self.setCentralWidget(self.chart_canvas)

# Run program


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
