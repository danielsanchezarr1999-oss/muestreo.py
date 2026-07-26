from abc import ABC, abstractmethod

# 1. Interfaz (en Python se simula mediante Clases Abstractas con métodos abstractos)
class Garantizable(ABC):
    @abstractmethod
    def mostrar_garantia(self):
        pass

# 2. Clase Abstracta Producto
class Producto(ABC):
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int):
        self._id = id_producto         # Encapsulamiento (atributo protegido)
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    # Métodos abstractos que obligatoriamente deben implementar las subclases (Polimorfismo)
    @abstractmethod
    def mostrar_detalles(self):
        pass

    @abstractmethod
    def calcular_precio_con_descuento(self) -> float:
        pass

    # Getters y Setters
    def get_id(self): return self._id
    def set_id(self, id_producto): self._id = id_producto

    def get_nombre(self): return self._nombre
    def set_nombre(self, nombre): self._nombre = nombre

    def get_precio(self): return self._precio
    def set_precio(self, precio): self._precio = precio

    def get_stock(self): return self._stock
    def set_stock(self, stock): self._stock = stock

# 3. Subclase Electronico (Hereda de Producto e implementa Garantizable)
class Electronico(Producto, Garantizable):
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, meses_garantia: int):
        super().__init__(id_producto, nombre, precio, stock)
        self.meses_garantia = meses_garantia

    def mostrar_detalles(self):
        print(f"[Electrónico] ID: {self.get_id()} | Nombre: {self.get_nombre()} | "
              f"Precio: ${self.get_precio():.2f} | Stock: {self.get_stock()} | "
              f"Garantía: {self.meses_garantia} meses")

    def calcular_precio_con_descuento(self) -> float:
        # 10% de descuento para electrónicos
        return self.get_precio() * 0.90

    def mostrar_garantia(self):
        print(f"Este producto electrónico cuenta con soporte y {self.meses_garantia} meses de garantía directa.")

# 4. Subclase Alimento (Hereda de Producto)
class Alimento(Producto):
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, fecha_caducidad: str):
        super().__init__(id_producto, nombre, precio, stock)
        self.fecha_caducidad = fecha_caducidad

    def mostrar_detalles(self):
        print(f"[Alimento] ID: {self.get_id()} | Nombre: {self.get_nombre()} | "
              f"Precio: ${self.get_precio():.2f} | Stock: {self.get_stock()} | "
              f"Caducidad: {self.fecha_caducidad}")

    def calcular_precio_con_descuento(self) -> float:
        # 15% de descuento por liquidación próxima
        return self.get_precio() * 0.85

# 5. Subclase Ropa (Hereda de Producto)
class Ropa(Producto):
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, talla: str, material: str):
        super().__init__(id_producto, nombre, precio, stock)
        self.talla = talla
        self.material = material

    def mostrar_detalles(self):
        print(f"[Ropa] ID: {self.get_id()} | Nombre: {self.get_nombre()} | "
              f"Precio: ${self.get_precio():.2f} | Stock: {self.get_stock()} | "
              f"Talla: {self.talla} | Material: {self.material}")

    def calcular_precio_con_descuento(self) -> float:
        # 20% de descuento para ropa
        return self.get_precio() * 0.80

# 6. Código Principal (Demostración de Polimorfismo)
if __name__ == "__main__":
    print("=== SISTEMA DE GESTIÓN DE INVENTARIOS (POO en Python) ===")
    print("Alumno: Jesus Daniel Sanchez Arredondo - Matrícula: 101886\n")

    # Lista polimórfica que almacena diferentes tipos de productos
    inventario = [
        Electronico("E001", "Laptop Gamer", 18500.0, 5, 12),
        Alimento("A001", "Caja de Leche", 28.50, 50, "15/10/2026"),
        Ropa("R001", "Camisa Casual", 450.0, 20, "M", "Algodón")
    ]

    print("--- DETALLES DEL INVENTARIO Y POLIMORFISMO ---")
    for producto in inventario:
        # Se invoca el método de forma dinámica según la clase del objeto
        producto.mostrar_detalles()
        print(f"Precio con descuento aplicado: ${producto.calcular_precio_con_descuento():.2f}")
        
        # Verificamos si el objeto implementa la interfaz Garantizable
        if isinstance(producto, Garantizable):
            producto.mostrar_garantia()
            
        print("-" * 65)