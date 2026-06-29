class Cliente:
    def __init__(self,nombre:str,edad:int,telefono:str,cliente_frecuente:bool):
        self.nombre=nombre; self.edad=edad; self.telefono=telefono; self.cliente_frecuente=cliente_frecuente
    def __str__(self):
        return f"Cliente: {self.nombre} | Edad: {self.edad} | Teléfono: {self.telefono} | {'Cliente frecuente' if self.cliente_frecuente else 'Cliente nuevo'}"
