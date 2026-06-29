from modelos.producto import Producto
from modelos.cliente import Cliente
class Restaurante:
    def __init__(self,nombre:str):
        self.nombre=nombre
        self.productos:list[Producto]=[]
        self.clientes:list[Cliente]=[]
    def agregar_producto(self,p): self.productos.append(p)
    def agregar_cliente(self,c): self.clientes.append(c)
    def mostrar_productos(self):
        print("\n=== PRODUCTOS ===")
        [print(p) for p in self.productos]
    def mostrar_clientes(self):
        print("\n=== CLIENTES ===")
        [print(c) for c in self.clientes]
    def __str__(self):
        return f"Restaurante: {self.nombre}\nProductos: {len(self.productos)}\nClientes: {len(self.clientes)}"
