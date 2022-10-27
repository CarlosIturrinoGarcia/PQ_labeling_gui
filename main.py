import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtChart import QChart
import scipy.io




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # create default constructor for QWidget
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Empty Window in PyQt')
        self.createMenu()
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
                                                   "", "HTML Files (*.html);;Text Files (*.txt)")
        if file_name:
         with open(file_name, 'r') as f:
          notepad_text = f.read()
          self.text_field.setText(notepad_text)
        else:
          QMessageBox.information(self, "Error",
          "Unable to open file.", QMessageBox.Ok)



# Run program


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
