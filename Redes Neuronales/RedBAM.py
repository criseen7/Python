import numpy as np

class BAM:
    def __init__(self, input_size, output_size):
        self.W = np.zeros((input_size, output_size))  # Matriz de pesos inicializada en ceros

    def entrenar(self, patrones_X, patrones_Y):
        # Sumar los productos externos de los patrones de entrenamiento
        for X, Y in zip(patrones_X, patrones_Y):
            self.W += np.outer(X, Y)  # Producto externo entre los patrones
        print("Matriz de pesos W después del entrenamiento:")
        print(self.W)

    def imprimir_matriz_transpuesta(self):
        # Verificar si la matriz es cuadrada
        if self.W.shape[0] == self.W.shape[1]:
            print("La matriz de pesos es cuadrada, no se necesita calcular la transpuesta.")
        else:
            # Imprimir la matriz de pesos transpuesta si no es cuadrada
            W_transpuesta = self.W.T
            print("Matriz de pesos transpuesta W^T:")
            print(W_transpuesta)

    def asociar_direccion_X_a_Y(self, X):
        # Propagar de X a Y
        Y_calculado = np.dot(X, self.W)  # Producto de X con la matriz de pesos
        return np.where(Y_calculado >= 0, 1, -1)  # Aplicar función de transferencia (-1, 1)

    def asociar_direccion_Y_a_X(self, Y):
        # Propagar de Y a X
        X_calculado = np.dot(self.W, Y)  # Producto de Y con la matriz de pesos
        return np.where(X_calculado >= 0, 1, -1)  # Aplicar función de transferencia (-1, 1)

def main():
    # Pedir el número de pares de patrones
    num_pares = int(input("Introduce el número de pares de patrones: "))
    
    # Inicializar listas para los patrones
    patrones_X = []
    patrones_Y = []
    
    # Para cada par de patrones, pedir los patrones de entrada y salida
    for i in range(num_pares):
        print(f"\nIntroduce el patrón de entrada X{i+1} (solo -1 y 1 separados por espacio):")
        X = list(map(int, input().split()))
        patrones_X.append(np.array(X))
        
        print(f"Introduce el patrón de salida Y{i+1} (solo -1 y 1 separados por espacio):")
        Y = list(map(int, input().split()))
        patrones_Y.append(np.array(Y))
    
    # Crear la red BAM
    input_size = len(patrones_X[0])
    output_size = len(patrones_Y[0])
    bam = BAM(input_size=input_size, output_size=output_size)

    # Entrenar la red BAM con los patrones ingresados
    bam.entrenar(patrones_X, patrones_Y)

    # Imprimir la matriz transpuesta (si es necesario)
    bam.imprimir_matriz_transpuesta()

    # Probar la asociación desde X a Y
    print("\nAsociación desde X a Y:")
    for i, X in enumerate(patrones_X):
        Y_recuperado = bam.asociar_direccion_X_a_Y(X)
        print(f"Patrón X{i+1}: {X} -> Y recuperado: {Y_recuperado}")
        print(f"Por lo tanto X{i+1} asocia con su salida Y{i+1}.\n")

    # Probar la asociación desde Y a X
    print("\nAsociación desde Y a X:")
    for i, Y in enumerate(patrones_Y):
        X_recuperado = bam.asociar_direccion_Y_a_X(Y)
        print(f"Patrón Y{i+1}: {Y} -> X recuperado: {X_recuperado}")
        print(f"Por lo tanto Y{i+1} asocia con su entrada X{i+1}.\n")

if __name__ == "__main__":
    main()
