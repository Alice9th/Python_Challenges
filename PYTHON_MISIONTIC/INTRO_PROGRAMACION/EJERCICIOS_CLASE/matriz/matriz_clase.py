class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.ceros = [0] * (columnas + 1)
        self.matriz = [] * (filas + 1)
        for i in range(filas + 1):
            self.matriz.append(self.ceros)


matriz = Matriz(4, 4)
print(matriz.matriz)
