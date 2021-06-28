import sys
from View.FormPrincipalEstk import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    FrmPrincipal = QMainWindow()
    ui = Ui_FrmPrincipalEstk()
    ui.setupUi(FrmPrincipal)
    FrmPrincipal.show()
    sys.exit(app.exec_())