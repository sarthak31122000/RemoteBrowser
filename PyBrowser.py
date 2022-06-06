import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QToolBar,QPushButton,QLineEdit
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QSize,QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEnginePage

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Browser')
        self.setWindowIcon(QIcon('assets/python.png'))
        self.setGeometry(200,200,900,600)

        toolBar=QToolBar()
        self.addToolBar(toolBar)

        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon('assets/arrow.png'))
        self.backButton.setIconSize(QSize(36,36))
        self.backButton.clicked.connect(self.backBtn)
        toolBar.addWidget(self.backButton)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon('assets/reload.png'))
        self.reloadButton.setIconSize(QSize(36,36))
        self.reloadButton.clicked.connect(self.reloadBtn)
        toolBar.addWidget(self.reloadButton)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon('assets/right-arrows.png'))
        self.forwardButton.setIconSize(QSize(36,36))
        self.forwardButton.clicked.connect(self.forwardBtn)
        toolBar.addWidget(self.forwardButton)

        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon('assets/home.png'))
        self.homeButton.setIconSize(QSize(36,36))
        self.homeButton.clicked.connect(self.homeBtn)
        toolBar.addWidget(self.homeButton)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont('Sans-Serif',18))
        self.addressLineEdit.returnPressed.connect(self.searchBtn)
        toolBar.addWidget(self.addressLineEdit)

        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon('assets/magnifier.png'))
        self.searchButton.setIconSize(QSize(36,36))
        self.searchButton.clicked.connect(self.searchBtn)
        toolBar.addWidget(self.searchButton)

        self.webEngineView=QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initial_Url='http://google.com'
        self.addressLineEdit.setText(initial_Url)
        self.webEngineView.load(QUrl(initial_Url))

    def searchBtn(self):
        myUrl=self.addressLineEdit.text()
        self.webEngineView.load(QUrl(myUrl))
    
    def backBtn(self):
        self.webEngineView.back()
    
    def forwardBtn(self):
        self.webEngineView.forward()

    def reloadBtn(self):
        self.webEngineView.reload()
    
    def homeBtn(self):
        self.webEngineView.load(QUrl('http://google.com'))


app=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())