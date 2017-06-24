import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class greetingView( QWidget ):
    def __init__( self, parent = None ):
        QWidget.__init__( self, parent )
        self.welcome = QLabel( "Olá " + parent.usr + "!", self )
        self.welcome.move( parent.width()/2, parent.height()/2 )

class dbView( QWidget ):
    def __init__( self, parent = None ):
        QWidget.__init__( self, parent )
        self.welcome = QLabel( "Esta é a Base de Dados", self )
        self.welcome.move( parent.width()/2, parent.height()/2 )

class reportView( QWidget ):
    def __init__( self, parent = None ):
        QWidget.__init__( self, parent )
        self.welcome = QLabel( "Aqui ficaram os relatórios", self )
        self.welcome.move( parent.width()/2, parent.height()/2 )


class mainWindow( QMainWindow ):
    def __init__( self, parent = None, usr = None, pwd = None ):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle( "Trabd" )
        self.resize( 800, 600 )
        self.usr = usr
        self.pwd = pwd

        menuBar = QMenuBar( self )
        menuBar.setNativeMenuBar( True )
        mainMenu = menuBar.addMenu("Menu")
        db_btn = QAction("Base de Dados", self)
        db_btn.triggered.connect(self.callDbView)
        report_btn = QAction("Relatórios", self)
        report_btn.triggered.connect(self.callReportView)
        exit_btn = QAction("Sair", self)
        exit_btn.triggered.connect( self.close )
        mainMenu.addAction(db_btn)
        mainMenu.addAction(report_btn)
        mainMenu.addAction(exit_btn)

        self.setMenuBar( menuBar )

        self.setCentralWidget( greetingView( self ) )

    def getUser():
        return self.usr

    def callDbView( self, flag ):
        self.setCentralWidget( dbView( self ) )

    def callReportView( self, flag ):
        self.setCentralWidget( reportView( self ) )

class loginScreen( QDialog ):
    def __init__( self, parent = None ):
        QDialog.__init__(self, parent)
        self.setWindowTitle( "Login" )
        self.resize( 280, 180 )

        self.usr_label = QLabel( "Usuário:", self )
        self.usr_label.move( 20, 20 )
        self.usr = QLineEdit( self )
        self.usr.move( 20, 40 )
        self.usr.resize( 240, 20 )

        self.pwd_label = QLabel( "Senha:", self )
        self.pwd_label.move( 20, 80 )
        self.pwd = QLineEdit( self )
        self.pwd.setEchoMode( QLineEdit.Password )
        self.pwd.move( 20, 100)
        self.pwd.resize( 240, 20 )

        self.login_btn = QPushButton("Login", self)
        self.login_btn.clicked.connect( self.login )
        self.login_btn.move(100, 140)
        self.login_btn.resize( 80, 20 )

        self.show()

    @pyqtSlot()
    def login( self ):
        self.accept()



if __name__ == "__main__":
    app = QApplication( sys.argv )
    login = loginScreen()
    if login.exec_() == QDialog.Accepted:
        main = mainWindow( usr = login.usr.text(), pwd = login.pwd.text() )
        login.close()
        main.show()

    sys.exit( app.exec_() )
