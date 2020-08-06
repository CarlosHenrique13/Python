from PyQt5.QtWidgets import QApplication, QMainWindow, QToolButton, QLineEdit, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon, QPixmap

#Variaveis
home_url     = "https://www.google.com"
facebook_url = "https://www.facebook.com"
twitter_url  = "https://www.twitter.com"
youtube_url  = "https://www.youtube.com"


application = QApplication([])

#INTERFACE
mainWindow = QMainWindow()
mainWindow.setGeometry(0,0,1350,690)
mainWindow.setMinimumHeight(690)
mainWindow.setMaximumHeight(690)
mainWindow.setMinimumWidth(1350)
mainWindow.setMaximumWidth(1350)
mainWindow.setWindowTitle("NAVEGADOR")
mainWindow.setStyleSheet("background-color: rgb(0,0,0);")



mainWindow.show()
application.exec_()
