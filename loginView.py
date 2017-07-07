import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

class telaLogin( QDialog ):
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
        self.db = QSqlDatabase.addDatabase("QPSQL")
        self.db.setHostName( sys.argv[1] )
        self.db.setPort( int( sys.argv[2] ) )
        self.db.setDatabaseName( sys.argv[3] )

        self.db.setUserName( str( self.usr.text() ) )
        self.db.setPassword( str( self.pwd.text() ) )

        if self.db.open():
            self.accept()
        else:
            print( self.db.lastError().databaseText() )
            self.reject()
