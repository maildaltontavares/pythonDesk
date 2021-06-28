from Model.DTO.ItemDTO import ItemDTO
from Model.DAO.ItemDAO import ItemDAO

class ItemCTR:
    def CadastrarItem(nome, codigo,classe, um):
        itemDTO = ItemDTO
        itemDTO.Codigo = codigo
        itemDTO.Nome = nome
        itemDTO.Classe = classe
        itemDTO.Um = um


        itemDAO = ItemDAO
        itemDAO.CadastrarItem(itemDTO)

    def AtualizarItem(codigoIt, nome, codigo,classe, um):
        itemDTO = ItemDTO
        itemDTO.Codigo = codigo
        itemDTO.Nome = nome
        itemDTO.Classe = classe
        itemDTO.Um = um


        itemDAO = ItemDAO
        itemDAO.AtualizarItem(codigoIt, itemDTO)

    def PesquisarTodosItems():
        itemDAO = ItemDAO
        query = itemDAO.PesquisarTodosItems()

        return query

    def PesquisarItem(valor, tipo):
        itemDAO = ItemDAO
        query = itemDAO.PesquisarItem(valor, tipo)

        return query

    def ExcluirItem(codigoIt):
        itemDAO = ItemDAO
        itemDAO.ExcluirItem(codigoIt)


