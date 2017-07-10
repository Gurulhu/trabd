from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

class telaItem( QMainWindow ):
    def __init__( self, parent = None, db = None ):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle( "Inventário" )
        self.resize( 600, 600 )

        menuBar = QMenuBar( self )
        menuBar.setNativeMenuBar( True )
        mainMenu = menuBar.addMenu("Menu")
        db_btn = QAction("Listar", self)
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

        exit_btn = QAction("Voltar", self)
        #exit_btn.triggered.connect( self.exitCall )
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
        #self.setCentralWidget( dbView( self ) )

    def callR1View( self, flag ):
        #self.setCentralWidget( r1View( self ) )

    def callR2View( self, flag ):
        #self.setCentralWidget( r2View( self ) )

    def callR3View( self, flag ):
        #self.setCentralWidget( r3View( self ) )
