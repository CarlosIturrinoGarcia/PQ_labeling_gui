import sys
from PyQt5.QtWidgets import QApplication, QAction, QMainWindow, QFileDialog, QMessageBox
import scipy.io
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from matplotlib.widgets import SpanSelector
from PyQt5 import QtWidgets

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=500, height=400, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes1 = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() # create default constructor for QWidget
        self.setGeometry(50, 50, 1500, 700)
        self.setWindowTitle("Smart Energy Lab")
        self.dataPlot1 = []
        self.windowSize = 1922
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

    def actions(self):
        self.openAction1 = QtWidgets.QAction("Open Phase1", self)
        self.openAction1.triggered.connect(self.file_open1)

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
                self.dataPlot1 = sig['Data1_V1i']
                self.signal_size = len(self.dataPlot1)
                self.sc.toolbar.clear()
                self.setupPlotter(self.dataPlot1)

            else:
                with open(file_name, 'r') as f:
                    sig = f.read()
                    self.text_field.setText(sig)
        else:
            QMessageBox.information(self, "Error",
                                    "Unable to open file.", QMessageBox.Ok)



    def setupPlotter(self, data):
        self.dataPlot1 = np.array(self.dataPlot1)
        self.count = []
        self.region_x = []
        self.sc = MplCanvas(self, width=500, height=400, dpi=100)
        if self.dataPlot1.any():
            self.dataPlot1.shape = (self.signal_size,)
            self.dataPlot1 = np.array(self.dataPlot1)
            #sc.axes1.set_title(self.name1[0])
            self.sc.axes1.plot(self.dataPlot1)

        else:
            self.sc.axes1.plot([])
        self.tool = self.addToolBar(NavigationToolbar2QT(self.sc, self))
        self.setCentralWidget(self.sc)
        self.span1 = SpanSelector(self.sc.axes1, self.onselect1, 'horizontal', useblit=True,  rectprops=dict(alpha=0.5, facecolor='blue'))

    def onselect1(self, xmin, xmax):
        if self.count:
           self.count = self.count+1
           leng = len(range(int(xmin),int(xmax)))
           if leng < self.windowSize:
               print("Non Sufficient Data Points")
           remainder = leng % self.windowSize
           is_divisible = remainder == 0
           c = 0
           while (not is_divisible):
               c = c + 1
               leng = leng - 1
               remainder = leng % self.windowSize
               is_divisible = remainder == 0
           self.region_x1 = np.append(self.region_x1, self.dataPlot1[int(xmin):(int(xmax)-c)])
           print(np.shape(self.region_x1))
           print(self.count)

        else:
           self.count = 1
           leng = len(range(int(xmin), int(xmax)))
           remainder = leng % self.windowSize
           is_divisible = remainder == 0
           c = 0
           while (not is_divisible):
               c = c + 1
               leng = leng - 1
               remainder = leng % self.windowSize
               is_divisible = remainder == 0
           self.region_x1 = self.dataPlot1[int(xmin):(int(xmax)-c)]
           print(np.shape(self.region_x1))
           print(self.count)
        print(self.region_x1)



# Run program


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
