from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *

from Controller.ItemCTR import ItemCTR

#try:
#    _fromUtf8 = QString.fromUtf8
#except AttributeError:
def _fromUtf8(s):
    return s

#try:
#    _encoding = QApplication.UnicodeUTF8
#    def _translate(context, text, disambig):
#        return QApplication.translate(context, text, disambig, _encoding)
#except AttributeError:
def _translate(context, text, disambig):
    return QApplication.translate(context, text, disambig)

class Ui_FrmInsereItem(object):
    #PREENCHER OS CAMPOS PARA ALTERAÇÃO
    def PreencherAlterar(self,  id,codigo, nome, classe,um):
        self.edtCodigo.setText(codigo)
        self.edtNome.setText(nome)
        self.edtClasse.setText(classe)
        self.edtUm.setText(um)


    #CLICK BTN_SALVAR
    def btnSalvar_Click(self, estado, codigoIt):

        if self.edtCodigo.text() != "" and self.edtNome.text() != "":
            codigo = self.edtCodigo.text()
            nome   = self.edtNome.text()
            classe = self.edtClasse.text()
            um     = self.edtUm.text()


            #VERIFICA O ESTADO INSERIR/ALTERAR PARA CHAMAR A FUNÇAO APROPRIADA
            if estado=='inserir':
                InsereItem = ItemCTR
                InsereItem.CadastrarItem(nome, codigo,classe, um)

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Item inserido com sucesso!")
                msg.setWindowTitle("Inserir Item")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

                self.edtCodigo.setText('')
                self.edtNome.setText('')
                self.edtClasse.setText('')
                self.edtUm.setText('')

            if estado=='alterar':
                InsereItem = ItemCTR
                InsereItem.AtualizarItem(codigoIt,nome, codigo,classe, um)

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Item alterado com sucesso!")
                msg.setWindowTitle("Alterar Item")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

            

        else:

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            if self.edtCodigo.text() == "":
                msg.setText("Codigo nao informado!")
            elif self.edtNome.text() == "":
                msg.setText("Nome nao informado!")
            # msg.setInformativeText("This is additional information")
            msg.setWindowTitle("Atencao")
            # msg.setDetailedText("The details are as follows:")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

 

    def setupUi(self, frmInsereItem, estado  , codigoIt):
        frmInsereItem.setObjectName(_fromUtf8("frmInsereItem"))

        #DESABILITAR REDIMENCIONAMENTO DA JANELA
        frmInsereItem.setFixedSize(532, 269)
        icon = QIcon()
        icon.addPixmap(QPixmap(_fromUtf8("Imagens/produto.png")), QIcon.Normal, QIcon.Off)
        frmInsereItem.setWindowIcon(icon)
        self.groupBox = QGroupBox(frmInsereItem)
        self.groupBox.setGeometry(QRect(10, 10, 511, 161))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        
        self.lbCodigo = QLabel(self.groupBox)
        self.lbCodigo.setGeometry(QRect(10, 10, 46, 13))
        self.lbCodigo.setObjectName(_fromUtf8("lbCodigo"))
        
        self.lbNome = QLabel(self.groupBox)
        self.lbNome.setGeometry(QRect(340, 10, 46, 13))
        self.lbNome.setObjectName(_fromUtf8("lbNome"))
        
        self.lbUm = QLabel(self.groupBox)
        self.lbUm.setGeometry(QRect(340, 60, 46, 13))
        self.lbUm.setObjectName(_fromUtf8("lbUm"))

        self.lbClasse = QLabel(self.groupBox)
        self.lbClasse.setGeometry(QRect(10, 60, 46, 13))
        self.lbClasse.setObjectName(_fromUtf8("lbClasse"))

        self.edtCodigo = QLineEdit(self.groupBox)
        self.edtCodigo.setGeometry(QRect(10, 30, 321, 20))
        self.edtCodigo.setObjectName(_fromUtf8("edtCodigo"))

        self.edtNome = QLineEdit(self.groupBox)
        self.edtNome.setGeometry(QRect(340, 30, 161, 20))
        self.edtNome.setObjectName(_fromUtf8("edtNome"))

        self.edtClasse = QLineEdit(self.groupBox)
        self.edtClasse.setGeometry(QRect(10, 80, 321, 20))
        self.edtClasse.setObjectName(_fromUtf8("edtClasse"))

        self.edtUm = QLineEdit(self.groupBox)
        self.edtUm.setGeometry(QRect(340, 80, 161, 20))
        self.edtUm.setObjectName(_fromUtf8("edtUm"))
        
        self.groupBox_2 = QGroupBox(frmInsereItem)
        self.groupBox_2.setGeometry(QRect(10, 180, 511, 81))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        
        self.btnSalvar = QPushButton(self.groupBox_2)
        self.btnSalvar.setGeometry(QRect(400, 10, 101, 61))
        self.btnSalvar.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(_fromUtf8("Imagens/save.png")), QIcon.Normal, QIcon.Off)
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setIconSize(QSize(35, 35))
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))
        #CLICK BOTAO SALVAR
        self.btnSalvar.clicked.connect(lambda: self.btnSalvar_Click(estado, codigoIt))


        frmInsereItem.setWindowTitle("Cadastro de Item")
        self.lbCodigo.setText("Codigo")
        self.lbNome.setText("Nome")
        self.lbClasse.setText("Classe")
        self.lbUm.setText("UM")

        self.btnSalvar.setText("Salvar")


        #self.retranslateUi(frmInsereItem)
        QMetaObject.connectSlotsByName(frmInsereItem)

    # def retranslateUi(self, frmInsereItem):
    #     frmInsereItem.setWindowTitle("Cadastro de Item")
    #     self.codigo.setText("Nome")
    #     self.nome.setText("CPF")
    #     self.lbClasse.setText("Endereço")
    #     self.lbUm.setText("EMail")
    #     self.codigo_5.setText("Telefone")
    #     self.btnSalvar.setText("Salvar")


if __name__ == "__main__":
    pass 
#    import sys
#    app = QApplication(sys.argv)
#    frmInsereItem = QWidget()
#    ui = Ui_frmInsereItem()
#    ui.setupUi(frmInsereItem)
#    frmInsereItem.show()
#    sys.exit(app.exec_())

