import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QCheckBox,\
    QProgressBar, QLabel, QComboBox, QStyleFactory, QFontDialog,\
    QColorDialog, QCalendarWidget, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QAction
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import *


class Window(QMainWindow):
    """a normal window"""

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("PyQt5")

        extractAction = QAction("Exit", self)
        extractAction.setShortcut("Ctrl+X")
        extractAction.setStatusTip("Leave the App")
        extractAction.triggered.connect(self.close_application)

        editor = QAction("Edit", self)
        editor.setShortcut("Ctrl+E")
        editor.setStatusTip("Start editing")
        editor.triggered.connect(self.edit)

        openFile = QAction("Open", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("Open the file")
        openFile.triggered.connect(self.file_open)

        saveFile = QAction("Save", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip("Save the file")
        saveFile.triggered.connect(self.file_save)

        self.statusBar()

        mainMenu = self.menuBar()
        # show the menubar on MacOS looks like on Windows
        mainMenu.setNativeMenuBar(False)

        fileMenu = mainMenu.addMenu("File")
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)

        editMenu = mainMenu.addMenu("Edit")
        editMenu.addAction(editor)

        self.home()

    def home(self):
        btn = QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())  # automatically set the button size
        btn.move(100, 100)

        extractAction = QAction("Flee the Screen", self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        fontChoice = QAction("Font", self)
        fontChoice.triggered.connect(self.font_choice)
        #self.toolBar = self.addToolBar("Font")
        self.toolBar.addAction(fontChoice)

        fontColor = QAction("Font bg Color", self)
        fontColor.triggered.connect(self.color_choice)
        self.toolBar.addAction(fontColor)

        cal = QCalendarWidget(self)
        cal.move(300, 300)
        cal.resize(cal.sizeHint())

        checkBox = QCheckBox("Enlarge Window", self)
        checkBox.move(0, 40)
        checkBox.stateChanged.connect(self.enlarge_window)
        checkBox.toggle()

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 100, 250, 20)

        self.btn = QPushButton("Download", self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)

        # create a text label that tells us which theme we currently use
        self.styleChoice = QLabel("MacOS", self)
        self.styleChoice.move(50, 150)

        # make the drop down
        comboBox = QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.move(50, 250)

        # the combo box will take the string version of the choice, and run self.style_choice method
        comboBox.activated[str].connect(self.style_choice)

        self.show()

    def color_choice(self):
        color = QColorDialog.getColor()
        self.styleChoice.setStyleSheet(
            "QWidget {background-color:%s}" % color.name())

    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def style_choice(self, text):
        # changes our label text to say the current style choice
        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def download(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += .01
            self.progress.setValue(self.completed)

    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(100, 100, 800, 800)
        else:
            self.setGeometry(100, 100, 400, 400)

    def edit(self):
        self.textEditor = QTextEdit("A custom editor", self)
        self.setCentralWidget(self.textEditor)

    def file_open(self):
        name, _ = QFileDialog.getOpenFileName(
            self, "Open File", options=QFileDialog.DontUseNativeDialog)
        file = open(name, "r")
        # call the text editor to come up
        self.edit()
        # care about the with method
        with file:
            text = file.read()
            self.textEditor.setText(text)

    def file_save(self):
        name, _ = QFileDialog.getSaveFileName(
            self, "Save File", options=QFileDialog.DontUseNativeDialog)
        file = open(name, "w")
        text = self.textEditor.toPlainText()
        file.write(text)
        file.close()

    def close_application(self):
        choice = QMessageBox.question(
            self, "Extract!", "Quit???", QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("quit application")
            sys.exit()
        else:
            pass


if __name__ == "__main__":

    def run():
        app = QApplication(sys.argv)
        GUI = Window()
        sys.exit(app.exec_())


run()
