from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
from PyQt5.QtSql import QSqlDatabase
 
from Controller.ItemCTR import ItemCTR
from View.FrmInsereItem import Ui_FrmInsereItem

import sqlite3

def _fromUtf8(s):
    return s

class Ui_FrmItens(object):

    def FrmInsereItem_Click(self):
        self.frmInsereitens = QMainWindow()
        self.frmInsereitens.setWindowModality(Qt.ApplicationModal)
        self.ui = Ui_FrmInsereItem()
        self.ui.setupUi(self.frmInsereitens, 'inserir', 0)
        self.frmInsereitens.show()

        self.PesquisarTodosItens()

    def FrmAlteraItem_Click(self):

        linha = self.gridItem.currentItem().row()

        codigoId = self.gridItem.item(linha, 0).text()
        codigoIt = self.gridItem.item(linha, 1).text()
        nome     = self.gridItem.item(linha, 2).text()
        classe   = self.gridItem.item(linha, 3).text()
        um       = self.gridItem.item(linha, 4).text()

        self.frmInsereitens = QMainWindow()
        self.frmInsereitens.setWindowModality(Qt.ApplicationModal)
        self.ui = Ui_FrmInsereItem()
        self.ui.setupUi(self.frmInsereitens, 'alterar',codigoId )
        self.ui.PreencherAlterar(codigoId,codigoIt,nome,classe,um)

        self.frmInsereitens.show()

        self.PesquisarTodosItens()

	#BTNItem.CLICK
    def PesquisarItem(self, valor, tipo):
        if valor == '':
            self.PesquisarTodosItens()
        else:
            Item = ItemCTR
            query = Item.PesquisarItem(valor, tipo)

            while (self.gridItem.rowCount() > 0):
                self.gridItem.removeRow(0)

            row = 0
            while query.next():

                self.gridItem.insertRow(row)
                codId = QTableWidgetItem(str(query.value(0)))
                codIt = QTableWidgetItem(str(query.value(1)))
                nomeIt = QTableWidgetItem(str(query.value(2)))
                umIt = QTableWidgetItem(str(query.value(3)))
                classeIt = QTableWidgetItem(str(query.value(4)))

                self.gridItem.setItem(row, 0, codId)
                self.gridItem.setItem(row, 1, codIt)
                self.gridItem.setItem(row, 2, nomeIt)
                self.gridItem.setItem(row, 3, umIt)
                self.gridItem.setItem(row, 4, classeIt)


                row = row + 1

        self.EdtPesqItem.setText('')

    def ExcluirItem_Click(self):

        linha = self.gridItem.currentItem().row()
        codigoIt = self.gridItem.item(linha, 0).text()

        #self.gridItem.removeRow(linha)
        Item = ItemCTR
        Item.ExcluirItem(codigoIt)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Item Excluído!")
        # msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Excluir Item")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        self.PesquisarTodosItens()

    def setupUi(self, FrmMainWindowItens):

        FrmMainWindowItens.setObjectName(_fromUtf8("FrmMainWindowItens"))
        #FrmMainWindowItens.setWindowModality(Qt.NonModal)

        FrmMainWindowItens.setWindowTitle("Cadastro de Itens")

        self.conn = sqlite3.connect("database.db")
        # self.c = self.conn.cursor()
        # self.c.execute(
        #     "CREATE TABLE IF NOT EXISTS  students(roll INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,branch TEXT,sem integer,mobile INTEGER,address TEXT)")
        # self.c.close()

        self.c = self.conn.cursor()
        self.c.execute(
            "CREATE TABLE IF NOT EXISTS  itens(roll INTEGER PRIMARY KEY AUTOINCREMENT, codigo TEXT,classe TEXT,nome TEXT,um TEXT)")
        self.c.close()



        FrmMainWindowItens.tableWidget = QTableWidget()
        FrmMainWindowItens.setCentralWidget(FrmMainWindowItens.tableWidget)

        #DESABILITAR REDIMENCIONAMENTO DA JANELA
        #FrmMainWindowItens.setFixedSize(803, 422)
        FrmMainWindowItens.setFixedSize(803, 550)
        icon = QIcon()
        icon.addPixmap(QPixmap(_fromUtf8("Imagens/FrmIcon_Car.png")), QIcon.Normal, QIcon.Off)
        FrmMainWindowItens.setWindowIcon(icon)
        FrmMainWindowItens.setAutoFillBackground(True)
        FrmMainWindowItens.setIconSize(QSize(40, 40))

        self.toolbar =  QToolBar(FrmMainWindowItens)
        self.toolbar.setMovable(False)
        FrmMainWindowItens.addToolBar(self.toolbar)

        self.btn_ac_add = QAction(QIcon("Imagens/add.png"),"Inserir Item",FrmMainWindowItens)
        self.btn_ac_add.triggered.connect(self.FrmInsereItem_Click)
        self.btn_ac_add.setStatusTip("Inserir Item")
        self.toolbar.addAction(self.btn_ac_add)

        self.btn_ac_refresh = QAction(QIcon("Imagens/edit.png"),"Atualizar dados do item",FrmMainWindowItens)
        self.btn_ac_refresh.setStatusTip("Atualizar")
        self.btn_ac_refresh.triggered.connect(self.FrmAlteraItem_Click)
        self.toolbar.addAction(self.btn_ac_refresh)

        self.btn_ac_search = QAction(QIcon("Imagens/pesquisar.png"),"Pesquisar dados do item",FrmMainWindowItens)
        self.btn_ac_search.setStatusTip("Pesquisar")
        self.btn_ac_search.triggered.connect(self.PesquisarTodosItens)
        self.toolbar.addAction(self.btn_ac_search)

        self.btn_ac_delete = QAction(QIcon("Imagens/delete.png"),"Deletar item",FrmMainWindowItens)
        self.btn_ac_delete.setStatusTip("Deletar")
        #self.btn_ac_delete.triggered.connect(self.delete)
        self.btn_ac_delete.triggered.connect(self.ExcluirItem_Click)
        self.toolbar.addAction(self.btn_ac_delete)

        self.btn_ac_sair = QAction(QIcon("Imagens/sair.png"), "Sair", FrmMainWindowItens)
        self.btn_ac_sair.setStatusTip("Sair")
        #btn_ac_sair.triggered.connect(self.sair)
        self.toolbar.addAction(self.btn_ac_sair)

        self.groupBox_2 = QGroupBox(FrmMainWindowItens)
        self.groupBox_2.setGeometry(QRect(3, 53, 798, 501))   #(3, 53, 798, 171))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setGeometry(QRect(10, 20, 81, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.cbPesqItem = QComboBox(self.groupBox_2)
        self.cbPesqItem.setGeometry(QRect(10, 40, 111, 22))
        self.cbPesqItem.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbPesqItem.setObjectName(_fromUtf8("cbPesqItem"))
        self.cbPesqItem.addItem(_fromUtf8(""))
        self.cbPesqItem.addItem(_fromUtf8(""))
        self.cbPesqItem.addItem(_fromUtf8(""))

        self.EdtPesqItem = QLineEdit(self.groupBox_2)
        self.EdtPesqItem.setGeometry(QRect(130, 40, 261, 20))
        self.EdtPesqItem.setObjectName(_fromUtf8("EdtPesqItem"))

        # BTN PESQ Item
        self.btnPesqItem = QPushButton(self.groupBox_2)
        self.btnPesqItem.setGeometry(QRect(400, 30, 91, 31))
        self.btnPesqItem.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(_fromUtf8("Imagens/lupa.png")), QIcon.Normal, QIcon.Off)
        self.btnPesqItem.setIcon(icon1)
        self.btnPesqItem.setIconSize(QSize(30, 30))
        self.btnPesqItem.setObjectName(_fromUtf8("btnPesqItem"))
        # BTN PESQ Item CLICK
        self.btnPesqItem.clicked.connect(lambda: self.PesquisarItem(self.EdtPesqItem.text(), self.cbPesqItem.currentText()))

        # GRID Item
        self.gridItem = QTableWidget(self.groupBox_2)
        self.gridItem.setGeometry(QRect(1, 70, 795, 400))  #(QRect(1, 70, 795, 170))
        self.gridItem.setObjectName(_fromUtf8("gridItem"))
        self.gridItem.setColumnCount(5)
        self.gridItem.setRowCount(0)
        item = QTableWidgetItem()
        self.gridItem.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.gridItem.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.gridItem.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.gridItem.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.gridItem.setHorizontalHeaderItem(4, item)

        # AJUSTANDO MODO DE SELEÇÃO - Uma linha por vez, desalitar editar
        self.gridItem.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.gridItem.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.gridItem.setSelectionMode(QAbstractItemView.SingleSelection)

        item = self.gridItem.horizontalHeaderItem(0)
        item.setText("ID")
        item = self.gridItem.horizontalHeaderItem(1)
        item.setText("Codigo")
        item = self.gridItem.horizontalHeaderItem(2)
        item.setText("Nome")
        item = self.gridItem.horizontalHeaderItem(3)
        item.setText("Classe")
        item = self.gridItem.horizontalHeaderItem(4)
        item.setText("UM")

        
        self.cbPesqItem.setItemText(0,"Id")
        self.cbPesqItem.setItemText(1, "Codigo")
        self.cbPesqItem.setItemText(2, "Nome")



        self.PesquisarTodosItens()

    # def sair(self):
    #     self.destroy

    # def delete(self):
    #     dlg = DeleteDialog()
    #     dlg.exec_()
    #
    # def search(self):
    #     dlg = SearchDialog()
    #     dlg.exec_()
    #
    # def insert(self):
    #     dlg = InsertDialog()
    #     dlg.exec_()

    def PesquisarTodosItens(self):

        Item = ItemCTR
        query = Item.PesquisarTodosItems()  
    
        while (self.gridItem.rowCount() > 0):
            self.gridItem.removeRow(0)

        row = 0
        while query.next():

            self.gridItem.insertRow(row)
            codId =    QTableWidgetItem(str(query.value(0)))
            codIt    = QTableWidgetItem(str(query.value(1)))
            nomeIt   = QTableWidgetItem(str(query.value(2)))
            classeIt     = QTableWidgetItem(str(query.value(3)))
            umIt = QTableWidgetItem(str(query.value(4)))


            self.gridItem.setItem(row, 0, codId)
            self.gridItem.setItem(row, 1, codIt)
            self.gridItem.setItem(row, 2, nomeIt)
            self.gridItem.setItem(row, 3, umIt)
            self.gridItem.setItem(row, 4, classeIt)
