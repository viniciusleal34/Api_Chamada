
from Reconhecimento.app.database import db
class Registro:
    def __init__(self,codigo, date, hour, minute):
        self.codigo = codigo
        self.date = date
        self.hour = hour
        self.minute = minute

    def salvar(self):

        registro = db.registro
        registro.insert_one({
            'codigo': self.codigo,
            'date': str(self.date),
            'hour': int(self.hour),
            'minute': int(self.minute),
        })