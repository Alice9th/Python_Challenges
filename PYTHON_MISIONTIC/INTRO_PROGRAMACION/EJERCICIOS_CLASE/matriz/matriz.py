"""
Python no tiene un tipo de dato incorporado 
para trabajar con matrices, 
sin embargo podemos tratar la matriz como una 
lista de listas, por ejemplo:"""

A = [[1, 4, 5], [-5, 8, 9]]

"""Para acceder a los datos de la matriz"""
print(A)
print(A[0])  # primera fila
print(A[0][0])  # primer elemento de la primer fila
print(A[0][-1])

print(str(A[0]) + "\n" + str(A[1]))  # otra forma de imprimirlo


# """ Todo tipo de datos """

A = ["hola", "mundo", "!"]
B = [True, False, None]
C = [{"clave": "valor"}, {"Pokemon": "Pikachu"}, {"estudiante": "Miguel"}]
matriz = [A, B, C]
print(matriz)
print(matriz[2][2])
print(type(matriz))
