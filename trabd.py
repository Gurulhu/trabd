import sys
import cx_Oracle
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

class r1View( QWidget ):
    def __init__( self, parent = None ):
        QWidget.__init__( self, parent )
        self.welcome = QLabel( "Aqui ficará o relatório 1", self )
        self.welcome.move( parent.width()/2, parent.height()/2 )

class r2View( QWidget ):
    def __init__( self, parent = None ):
        QWidget.__init__( self, parent )
        self.welcome = QLabel( "Aqui ficará o relatório 2", self )
        self.welcome.move( parent.width()/2, parent.height()/2 )

class r3View( QWidget ):
    def __init__( self, parent = None ):
        QWidget.__init__( self, parent )
        self.welcome = QLabel( "Aqui ficará o relatório 3", self )
        self.welcome.move( parent.width()/2, parent.height()/2 )



class mainWindow( QMainWindow ):
    def __init__( self, parent = None, usr = None, pwd = None, conn = None ):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle( "Trabd" )
        self.resize( 800, 600 )
        self.usr = usr
        self.pwd = pwd
        self.db = conn

        menuBar = QMenuBar( self )
        menuBar.setNativeMenuBar( True )
        mainMenu = menuBar.addMenu("Menu")
        db_btn = QAction("Base de Dados", self)
        db_btn.triggered.connect(self.callDbView)

        report_btn = QMenu("Relatórios", self)
        rep1_btn = QAction( "Atletas por Modalidade, Treinador e Médico", self )
        rep1_btn.triggered.connect(self.callR1View)
        rep2_btn = QAction( "Médicos por Quantidade de Pacientes e Nação", self )
        rep2_btn.triggered.connect(self.callR2View)
        rep3_btn = QAction( "Atletas irregulares por Treinadores", self )
        rep3_btn.triggered.connect(self.callR3View)
        report_btn.addAction(rep1_btn)
        report_btn.addAction(rep2_btn)
        report_btn.addAction(rep3_btn)

        exit_btn = QAction("Sair", self)
        exit_btn.triggered.connect( self.exitCall )
        mainMenu.addAction(db_btn)
        mainMenu.addMenu(report_btn)
        mainMenu.addAction(exit_btn)

        self.setMenuBar( menuBar )

        self.setCentralWidget( greetingView( self ) )

    def getUser():
        return self.usr

    def exitCall( self, flag ):
        try:
            self.db.close()
            self.close()
        except:
            print( "Ops" )

    def callDbView( self, flag ):
        self.setCentralWidget( dbView( self ) )

    def callR1View( self, flag ):
        self.setCentralWidget( r1View( self ) )

    def callR2View( self, flag ):
        self.setCentralWidget( r2View( self ) )

    def callR3View( self, flag ):
        self.setCentralWidget( r3View( self ) )


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
        ip = sys.argv[1]
        port = sys.argv[2]
        sid = sys.argv[3]
        conn = cx_Oracle.makedsn(ip, port, sid)

        try:
            self.db = cx_Oracle.connect( str( self.usr.text() ), str( self.pwd.text() ), conn )
            self.accept()
        except Exception as e:
            print( e )
            self.reject()


if __name__ == "__main__":
    app = QApplication( sys.argv )
    login = loginScreen()
    if login.exec_() == QDialog.Accepted:
        main = mainWindow( usr = login.usr.text(), pwd = login.pwd.text(), conn = login.db )
        login.close()
        main.show()
        sys.exit( app.exec_() )

    sys.exit( 1 )
