from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import time
import datetime

class telaComanda( QMainWindow ):
    def __init__( self, parent = None, db = None ):
        QMainWindow.__init__( self, parent )
        self.db = db
        self.setWindowTitle( "Comanda" )
        self.resize( 600, 400 )


class telaPreComanda( QDialog ):
    def __init__( self, parent = None, db = None ):
        QDialog.__init__(self, parent)
        self.db = db
        self.setWindowTitle( "Comanda" )
        self.resize( 200, 220 )

        self.mesa_label = QLabel( "Mesa:", self )
        self.mesa_label.move( 20, 20 )
        self.mesa = QComboBox( self )
        query_mesas = db.exec_("SELECT NUMERO FROM MESA")
        while query_mesas.next():
            self.mesa.addItem( str( query_mesas.value(0) ) )
        self.mesa.move( 20, 40 )
        self.mesa.resize( 160, 20 )

        self.pessoas_label = QLabel( "Pessoas:", self )
        self.pessoas_label.move( 20, 80 )
        self.pessoas = QLineEdit( self )
        self.pessoas.move( 20, 100)
        self.pessoas.resize( 160, 20 )

        self.reserva_label = QLabel( "Reserva:", self )
        self.reserva_label.move( 20, 140 )
        self.reserva = QCheckBox( self )
        self.reserva.move( 160, 140 )

        self.open_btn = QPushButton("Abrir", self)
        self.open_btn.clicked.connect( self.open )
        self.open_btn.move(60, 180)
        self.open_btn.resize( 80, 20 )

        self.show()

    @pyqtSlot()
    def open( self ):
        query = self.db.exec_()
        query.prepare("INSERT INTO COMANDA( entrada, dia, mesa, pessoas, reserva) VALUES ( :hora, :dia, :mesa, :pessoas, :reserva)")
        print( time.strftime("%d-%b-%Y", time.localtime() ), time.strftime("%H:%M:%S", time.localtime() ) )
        query.bindValue(":hora", time.strftime("%H:%M:%S", time.localtime() ) )
        query.bindValue(":dia", time.strftime("%d-%b-%Y", time.localtime() ) )
        query.bindValue(":mesa", int( self.mesa.itemText(  self.mesa.currentIndex() ) ) )
        query.bindValue(":pessoas", int( self.pessoas.text() ) )
        query.bindValue(":reserva", self.reserva.isTristate() )
        if query.exec_():
            self.accept()
        else:
            print( query.lastError().databaseText() )
