import numpy as np

# vector
vector = np.array([1, 2, 3])
print(vector)
print(type(vector))

# matriz

matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)

# diferentes tipos de datos

# matriz = np.array[["hola", 2, {"clave": "valor"}], [4.5, True, 0]]
# print(matriz)

A = np.array([[2, 4], [5, -6]])
B = np.array([[8, 9], [-5, 46]])
# Acceder a los datos
print(A[0])
print(A[0][1])

# por columnas
print(A[:, 0])
# Operaciones


# suma
C = A + B
print(A + B)

# multiplicacion
C = A.dot(B)
print(C)

# Transpuesta
print(A.transpose())


# Matriz de ceros
ceros = np.zeros((5, 5))
print(ceros)
