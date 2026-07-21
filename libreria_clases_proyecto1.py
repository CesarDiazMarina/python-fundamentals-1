"""
libreria_clases_proyecto1.py
-----------------------------
Librería externa con clases que implementan operaciones CRUD
(Crear, Leer, Actualizar, Eliminar). El estudiante debe elegir
UNA clase, conectar sus atributos/métodos con widgets en Streamlit
y hacerla funcionar dentro de la app (Ejercicio 4).

Cada clase mantiene sus registros en una lista interna de
diccionarios para facilitar su conversión a DataFrame en Streamlit.
"""


class GestorProductos:
    """
    Área: Inventario / Retail
    Administra un catálogo simple de productos.
    """

    def __init__(self):
        self.registros = []
        self._siguiente_id = 1

    def crear(self, nombre: str, categoria: str, precio: float, stock: int):
        registro = {
            "id": self._siguiente_id,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "stock": stock,
        }
        self.registros.append(registro)
        self._siguiente_id += 1
        return registro

    def leer(self):
        return self.registros

    def actualizar(self, id_registro: int, **campos):
        for r in self.registros:
            if r["id"] == id_registro:
                r.update(campos)
                return r
        return None

    def eliminar(self, id_registro: int):
        self.registros = [r for r in self.registros if r["id"] != id_registro]


class GestorClientes:
    """
    Área: Ventas / CRM
    Administra una lista simple de clientes.
    """

    def __init__(self):
        self.registros = []
        self._siguiente_id = 1

    def crear(self, nombre: str, correo: str, telefono: str):
        registro = {
            "id": self._siguiente_id,
            "nombre": nombre,
            "correo": correo,
            "telefono": telefono,
        }
        self.registros.append(registro)
        self._siguiente_id += 1
        return registro

    def leer(self):
        return self.registros

    def actualizar(self, id_registro: int, **campos):
        for r in self.registros:
            if r["id"] == id_registro:
                r.update(campos)
                return r
        return None

    def eliminar(self, id_registro: int):
        self.registros = [r for r in self.registros if r["id"] != id_registro]


class GestorTareas:
    """
    Área: Gestión de proyectos / Productividad
    Administra una lista simple de tareas con su estado.
    """

    def __init__(self):
        self.registros = []
        self._siguiente_id = 1

    def crear(self, titulo: str, prioridad: str, estado: str = "Pendiente"):
        registro = {
            "id": self._siguiente_id,
            "titulo": titulo,
            "prioridad": prioridad,
            "estado": estado,
        }
        self.registros.append(registro)
        self._siguiente_id += 1
        return registro

    def leer(self):
        return self.registros

    def actualizar(self, id_registro: int, **campos):
        for r in self.registros:
            if r["id"] == id_registro:
                r.update(campos)
                return r
        return None

    def eliminar(self, id_registro: int):
        self.registros = [r for r in self.registros if r["id"] != id_registro]
