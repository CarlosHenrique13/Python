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

#RENDERIZAR PAGINAS DO NAVEGADOR
web = QWebEngineView(mainWindow)
web.setGeometry(0,30,1350,690)
web.setStyleSheet("background-color: rgb(255,255,255);")
web.load(QUrl(home_url))

#Linha de Entrada da Url
go_line = QLineEdit(mainWindow)
go_line.setGeometry(350,5,500,20)
go_line.setStyleSheet("background-color: rgb(255,255,255);")


#Butão Home
home_button = QToolButton(mainWindow)
home_button.setGeometry(10,3,20,20)
home_button_icon = QIcon()
home_button_icon.addPixmap(QPixmap("img/home.png"))
home_button.setIcon(home_button_icon)
home_button.setStyleSheet("background-color: transparent")

#Butão Reload
reload_button = QToolButton(mainWindow)
reload_button.setGeometry(60,3,20,20)
reload_button_icon = QIcon()
reload_button_icon.addPixmap(QPixmap("img/reciclar.png"))
reload_button.setIcon(reload_button_icon)
reload_button.setStyleSheet("background-color: transparent")

#Butão Voutar
back_button = QToolButton(mainWindow)
back_button.setGeometry(140,3,20,20)
back_button_icon = QIcon()
back_button_icon.addPixmap(QPixmap("img/retorna.png"))
back_button.setIcon(back_button_icon)
back_button.setStyleSheet("background-color: transparent")

#Butão Para Frente
forward_button = QToolButton(mainWindow)
forward_button.setGeometry(180,5,20,20)
forward_button_icon = QIcon()
forward_button_icon.addPixmap(QPixmap("img/frente.png"))
forward_button.setIcon(forward_button_icon)
forward_button.setStyleSheet("background-color: transparent")
forward_button.setIconSize(QSize(50,50))

#Butão de Psguisa
go_button = QToolButton(mainWindow)
go_button.setGeometry(880,3,30,30)
go_button_icon = QIcon()
go_button_icon.addPixmap(QPixmap("img/procurar.png"))
go_button.setIcon(go_button_icon)
go_button.setStyleSheet("background-color: transparent")

#Butão de Facebook
facebook_button = QToolButton(mainWindow)
facebook_button.setGeometry(1200,1,30,30)
facebook_button_icon = QIcon()
facebook_button_icon.addPixmap(QPixmap("img/facebook.png"))
facebook_button.setStyleSheet("background-color: transparent")
facebook_button.setIcon(facebook_button_icon)

#Butão de Youtube
youtube_button = QToolButton(mainWindow)
youtube_button.setGeometry(1250,1,30,30)
youtube_button_icon = QIcon()
youtube_button_icon.addPixmap(QPixmap("img/youtube.png"))
youtube_button.setStyleSheet("background-color: transparent")
youtube_button.setIcon(youtube_button_icon)
youtube_button.setIconSize(QSize(20,20))

#Butão de Twiter
twiter_button = QToolButton(mainWindow)
twiter_button.setGeometry(1300,1,30,30)
twiter_button_icon = QIcon()
twiter_button_icon.addPixmap(QPixmap("img/twitter.png"))
twiter_button.setStyleSheet("background-color: transparent")
twiter_button.setIcon(twiter_button_icon)


def home(mainWindow):
    web.load(QUrl(home_url))

def reload(mainWindow):
    web.reload()

def back(mainWindow):
    web.back()

def forward(mainWindow):
    web.forward()

def go(mainWindow):
    go_url = go_line.text()
    web.load(QUrl(go_url))

def facebook(mainWindow):
    web.load(QUrl(facebook_url))

def twitter(mainWindow):
    web.load(QUrl(twitter_url))

def youtube(mainWindow):
    web.load(QUrl(youtube_url))

def Downloads(item):
    item.accept()
    msg = QMessageBox()
    msg.setWindowTitle("Dowloads")
    msg.setText("O seu download foi iniciado")
    msg.setIcon(QMessageBox.Warning)
    msg.exec_()


mainWindow.show()
application.exec_()
