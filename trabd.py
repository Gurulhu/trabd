import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import loginView
import comandaView

class dialog( QDialog ):
    def __init__( self, parent = None, opts = None ):
        QDialog.__init__( self, parent )
        self.combo = QComboBox()
        self.combo.resize( 100, 40 )
        self.combo.move( 20, 20 )
        print( opts )
        for i in range( len( opts ) ):
            self.combo.addItem( str( opts[i][0] ) )
        self.combo.activated.connect( self.changed )

    def changed( int ):
        self.accept()

class greetingView( QWidget ):
    def __init__( self, parent = None ):
        QWidget.__init__( self, parent )
        self.welcome = QLabel( "Olá " + parent.usr + "!", self )
        self.welcome.move( parent.width()/2, parent.height()/2 )

class dbView( QTableWidget ):
    def __init__( self, parent = None ):
        QTableWidget.__init__( self, parent )
        self.resize( parent.width(), parent.height() )
        self.db = parent.db
        cursor = self.db.cursor()
        cursor.execute( "SELECT * FROM METODO_DE_TRATAMENTO" )
        result = cursor.fetchall()
        self.setRowCount( len(result) + 1 )
        self.setColumnCount( len( result[0] ) + 1 )
        for i in range( len( result ) ):
            for j in range( len( result[i] ) ):
                try:
                    self.setItem( i, j, QTableWidgetItem( str( result[i][j] ) ) )
                except Exception as e:
                    self.setItem( i, j, QTableWidgetItem( str( result[i][j].read() ) ) )
            self.setItem( i, len( result[i] ), QTableWidgetItem( "Deletar" ) )
        self.cellClicked.connect( self.callCellClicked )
        self.cellChanged.connect( self.callCellChanged )
        self.setItem( len( result ), len( result[i] ), QTableWidgetItem( "Inserir" ) )
        cursor.close()

    def callCellChanged( self, i, j ):
        if i != self.rowCount() -1:
            self.item( i, 4 ).setData( 2, "Alterar" )

    def callCellClicked( self, i, j ):
        print( i, j, self.rowCount(), self.columnCount() )
        if j == self.columnCount() - 1:
            cursor = self.db.cursor()
            if i == self.rowCount() - 1:
                statement = "INSERT INTO METODO_DE_TRATAMENTO VALUES ( :q, :w, :e, :r )"
                values = { "q": self.item( i, 0 ).data(2), "w": self.item( i, 1 ).data(2), "e": self.item( i, 2 ).data(2).encode("UTF-8"), "r": self.item( i, 3 ).data(2) }
            elif self.item( i, j ).data(2) == "Deletar":
                statement = "DELETE FROM METODO_DE_TRATAMENTO WHERE id = :q"
                values = { "q": self.item( i, 0 ).data(2) }
            else:
                statement = "UPDATE METODO_DE_TRATAMENTO SET id = :q, diagnostico = :w, descricao = :e, efetividade = :r WHERE id = :q"
                values = { "q": self.item( i, 0 ).data(2), "w": self.item( i, 1 ).data(2), "e": self.item( i, 2 ).data(2).encode("UTF-8"), "r": self.item( i, 3 ).data(2) }
            print( statement, values )
            cursor.execute( statement, values )
            self.db.commit()
            cursor.close()
        elif j == 1:
            cursor = self.db.cursor()
            cursor.execute( "SELECT ID FROM DIAGNOSTICO" )
            opts = cursor.fetchall()
            cursor.close()
            d = dialog( opts = opts )
            d.exec_()
            self.item( i, j).setData( 2, str( d.combo.currentIndex() ) )
            d.close()




class r1View( QWidget ):
    def __init__( self, parent = None ):
        QWidget.__init__( self, parent )
        self.usr_label = QLabel( "Modalidade:", self )
        self.usr_label.move( 20, 60 )
        self.usr = QLineEdit( self )
        self.usr.move( 180, 60 )
        self.usr.resize( 150, 20 )

        self.usr_label = QLabel( "Médico:", self )
        self.usr_label.move( 20, 130 )
        self.usr = QLineEdit( self )
        self.usr.move( 180, 130 )
        self.usr.resize( 150, 20 )

        self.usr_label = QLabel( "Treinador:", self )
        self.usr_label.move( 20, 200 )
        self.usr = QLineEdit( self )
        self.usr.move( 180, 200 )
        self.usr.resize( 150, 20 )

        self.gerar_btn = QPushButton("Gerar", self)
        self.gerar_btn.clicked.connect( self.generate )
        self.gerar_btn.move(100, 270)
        self.gerar_btn.resize( 80, 20 )

    def generate( self, flag ):
        pass

class r2View( QWidget ):
    def __init__( self, parent = None ):
        QWidget.__init__( self, parent )
        self.usr_label = QLabel( "Numero de Atletas:", self )
        self.usr_label.move( 20, 60 )
        self.usr = QLineEdit( self )
        self.usr.move( 180, 60 )
        self.usr.resize( 150, 20 )

        self.usr_label = QLabel( "Nação:", self )
        self.usr_label.move( 20, 130 )
        self.usr = QLineEdit( self )
        self.usr.move( 180, 130 )
        self.usr.resize( 150, 20 )

        self.gerar_btn = QPushButton("Gerar", self)
        self.gerar_btn.clicked.connect( self.generate )
        self.gerar_btn.move(100, 200)
        self.gerar_btn.resize( 80, 20 )

    def generate( self, flag ):
        pass


class r3View( QWidget ):
    def __init__( self, parent = None ):
        QWidget.__init__( self, parent )
        self.usr_label = QLabel( "Numero de Treinadores:", self )
        self.usr_label.move( 20, 60 )
        self.usr = QLineEdit( self )
        self.usr.move( 180, 60 )
        self.usr.resize( 150, 20 )

        self.gerar_btn = QPushButton("Gerar", self)
        self.gerar_btn.clicked.connect( self.generate )
        self.gerar_btn.move(100, 130)
        self.gerar_btn.resize( 80, 20 )

    def generate( self, flag ):
        pass


class mainWindow( QMainWindow ):
    def __init__( self, parent = None, usr = None, pwd = None, conn = None ):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle( "Trabd" )
        self.resize( 600, 600 )
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



if __name__ == "__main__":
    app = QApplication( sys.argv )
    login = loginView.telaLogin()
    if login.exec_() == QDialog.Accepted:
        #main = mainWindow( usr = login.usr.text(), pwd = login.pwd.text(), conn = login.db )
        precomanda = comandaView.telaPreComanda( db = login.db )
        login.close()
        if precomanda.exec_() == QDialog.Accepted:
            comanda = comandaView.telaComanda( db = precomanda.db )
            comanda.show()
        #main.show()
        sys.exit( app.exec_() )

    sys.exit( 1 )
