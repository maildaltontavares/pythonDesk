from PyQt5.QtSql import QSqlQuery
from DataBase.ConexaoSQL import ConexaoSQL

class ItemDAO:
    def CadastrarItem(Item):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        query = QSqlQuery()
        query.prepare("INSERT INTO Itens(codigo,nome, classe, um) "
                      "VALUES (?, ?, ?,?)")
        query.addBindValue(Item.Codigo)
        query.addBindValue(Item.Nome)
        query.addBindValue(Item.Classe)
        query.addBindValue(Item.Um)

        query.exec_()
        db.commit()

    def AtualizarItem(codigoIt, Item):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        query = QSqlQuery()
        query.prepare("UPDATE Itens SET nome = '"+Item.Nome
                      +"', classe = '"+Item.Classe
                      +"', codigo = '"+Item.Codigo
                      +"', um =     '"+Item.Um
                      +"' WHERE roll = "+codigoIt)
        query.exec_()
        db.commit()

    def ExcluirItem(codigoIt):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        query = QSqlQuery()
        query.prepare("DELETE FROM Itens WHERE roll=:codigoIt")
        query.bindValue(":codigoIt", codigoIt)
        query.exec_()
        db.commit()

    def PesquisarTodosItems():
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        sql = "SELECT roll,codigo,nome,um,classe FROM Itens"
        #sql = "SELECT * FROM Itens"
        query = QSqlQuery(sql)

        return query

    def PesquisarItem(valor, tipo):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        if tipo=='Id':
            sql = "SELECT * FROM Itens where roll = " + valor
            query = QSqlQuery(sql)
        elif tipo=='Codigo':
            sql = "SELECT * FROM Itens where codigo = '"+valor+"'"
            query = QSqlQuery(sql)
        elif tipo=='Nome':
            sql = "SELECT * FROM Itens where nome = '" + valor+"'"
            query = QSqlQuery(sql)

        return query




