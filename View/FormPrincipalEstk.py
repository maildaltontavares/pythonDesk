from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *

from View.FrmItens import Ui_FrmItens

def _fromUtf8(s):
    return s

from View.FrmInsereItem import Ui_FrmInsereItem
class Ui_FrmPrincipalEstk(object):
	#BTNCLIENTE.CLICK

    def FrmItens_Click(self):
        self.frmitens = QMainWindow()
        self.frmitens.setWindowModality(Qt.ApplicationModal)
        self.ui = Ui_FrmItens()
        self.ui.setupUi(self.frmitens)
        self.frmitens.show()

    def setupUi(self, frmMainWindow):
        frmMainWindow.setObjectName(_fromUtf8("frmMainWindow"))
        frmMainWindow.setWindowModality(Qt.NonModal)
        frmMainWindow.setWindowTitle("Sysup")

        #DESABILITAR REDIMENCIONAMENTO DA JANELA
        #frmMainWindow.setFixedSize(803, 422)
        frmMainWindow.setFixedSize(580, 450)
        icon = QIcon()
        icon.addPixmap(QPixmap(_fromUtf8("Imagens/produto.png")), QIcon.Normal, QIcon.Off)
        frmMainWindow.setWindowIcon(icon)
        frmMainWindow.setAutoFillBackground(True)
        frmMainWindow.setIconSize(QSize(40, 40))

        self.centralwidget = QWidget(frmMainWindow)

        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.columnView = QColumnView(self.centralwidget)
        self.columnView.setGeometry(QRect(0, 0, 581, 101))
        self.columnView.setObjectName(_fromUtf8("columnView"))


        #BTN ITEM ###################
        self.btnItem = QPushButton(self.centralwidget)
        self.btnItem.setGeometry(QRect(140, 10, 131, 81))
        self.btnItem.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(_fromUtf8("Imagens/produto.png")), QIcon.Normal, QIcon.Off)
        self.btnItem.setIcon(icon2)
        self.btnItem.setIconSize(QSize(30, 30))
        self.btnItem.setObjectName(_fromUtf8("btnItem"))
        ##  btnItem CLICK EVENT  ###
        self.btnItem.clicked.connect(self.FrmItens_Click)



        #BTN CLIENTE ###################
        self.btnFornecedor = QPushButton(self.centralwidget)
        #self.btnFornecedor.setGeometry(QRect(140, 10, 131, 81))
        self.btnFornecedor.setGeometry(QRect(10, 10, 131, 81))
        self.btnFornecedor.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(_fromUtf8("Imagens/btnCadCli.png")), QIcon.Normal, QIcon.Off)
        self.btnFornecedor.setIcon(icon2)
        self.btnFornecedor.setIconSize(QSize(30, 30))
        self.btnFornecedor.setObjectName(_fromUtf8("btnFornecedor"))
        ##  btnFornecedor CLICK EVENT  ###
        #self.btnFornecedor.clicked.connect(self.FrmItens_Click)  

        self.lbImg = QLabel(self.centralwidget)
        self.lbImg.setGeometry(QRect(10, 110, 561, 301))
        self.lbImg.setCursor(QCursor(Qt.PointingHandCursor))
        self.lbImg.setFrameShape(QFrame.WinPanel)
        self.lbImg.setText(_fromUtf8(""))
        self.lbImg.setPixmap(QPixmap(_fromUtf8("Imagens/suprimentos.png")))
        self.lbImg.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.lbImg.setObjectName(_fromUtf8("lbImg"))

        self.menubar = QMenuBar(frmMainWindow)

        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuCad = QMenu(self.menubar)
        self.menuCad.setObjectName("menuCad")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        frmMainWindow.setMenuBar(self.menubar)

        self.actionSobre = QAction(frmMainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.actionItem = QAction(frmMainWindow)
        self.actionItem.setObjectName("actionItem")
        self.actionForn = QAction(frmMainWindow)
        self.actionForn.setObjectName("actionForn")
        
        self.menuCad.addAction(self.actionForn)
        self.menuCad.addAction(self.actionItem)
        
        self.menuHelp.addAction(self.actionSobre)
       
        self.menubar.addAction(self.menuCad.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        iconF = QIcon()
        iconF.addPixmap(QPixmap(_fromUtf8("Imagens/btnCadCli.png")), QIcon.Normal, QIcon.Off)
        iconI = QIcon()
        iconI.addPixmap(QPixmap(_fromUtf8("Imagens/produto.png")), QIcon.Normal, QIcon.Off)

        self.menuCad.setTitle("&Cadastros")
        self.menuHelp.setTitle("&Help")

        self.actionSobre.setText("&Sobre")
        self.actionSobre.setShortcut("Ctrl+S")

        self.actionItem.setText("&Item")
        self.actionItem.setShortcut("Ctrl+I")
        self.actionItem.setIcon(iconI)
        self.actionItem.triggered.connect(self.FrmItens_Click)

        self.actionForn.setText("&Fornecedor")
        self.actionForn.setShortcut("Ctrl+F")
        self.actionForn.setIcon(iconF)

        frmMainWindow.setCentralWidget(self.centralwidget)

    def newCall(self):
        pass

    def newCallFornec(self):
        pass

        #help_menu = self.menuBar().addMenu("&Ajuda")