from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante
r=Restaurante("Restaurante Sabor Andino")
for p in [Producto("Hamburguesa","Comida",6.5,True),Producto("Pizza","Comida",12.99,True),Producto("Jugo","Bebida",2.5,True),Producto("Café","Bebida",1.75,False)]: r.agregar_producto(p)
for c in [Cliente("Juan Pérez",25,"0991234567",True),Cliente("María Gómez",30,"0987654321",False)]: r.agregar_cliente(c)
print(r); r.mostrar_productos(); r.mostrar_clientes()
