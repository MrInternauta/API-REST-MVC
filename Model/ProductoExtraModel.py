# -*- coding: utf-8 -*-
from BaseModel import BaseModel as BM 

class ProductoExtraModel(BM):
    def __init__(self ):
      self.tableName = 'ExtrasProductos'
      self.idName = 'idExtras'
      self.Base = BM(self.tableName, self.idName)
      self.rows = {}

    def setDataModel(self, idProducto, idExtras):
        self.rows['idProducto'] = idProducto
        self.rows['idExtras'] = idExtras
        self.Base.setRows(self.rows)

    def getAll(self):
        return self.Base.getAll()

    def getOneById(self, id):
        return self.Base.getOneById(id)

    def Create(self):
        return self.Base.Create()
    
    def Update(self, id):
        self.Base.Update(id)




# usuarioModel = UsuarioModel("Usuario", "idUsuario")
# usuarioModel.setDataModel(None, "Felipe2", "Ramirez2", "feldjesus2", "1234", None)
# usuarioModel.Update(4)
# usuarioModel.Create()
# usuarioModel.getOneById(4)
#usuarioModel.getAll()
