import numpy as np

def calcularW(vectores, n):
    W = np.zeros((n, n))  # Inicializar la matriz de pesos en ceros
    for vector in vectores:
        W += np.outer(vector, vector)  
    np.fill_diagonal(W, 0) 
    return W / len(vectores)  # Normalizar por el número de vectores

def funcionTransferencia(x):
    return np.where(x >= 0, 1, -1)

def recuperarHopfield(W, vector, iteraciones=10):
    vector_anterior = vector.copy()  # Copia del vector inicial para comparación
    for i in range(iteraciones):
        vector = funcionTransferencia(np.dot(W, vector))  # Actualizar el vector de acuerdo a la matriz de pesos
        print(f"Iteración {i+1}: {vector}")  # Imprimir el vector en cada iteración
        if np.array_equal(vector, vector_anterior):  # Comparar con el patrón de la iteración anterior
            print(f"Y({i}) == Y({i-1}) Por lo tanto Converge.")
            return vector  # Si converge, retornar el patrón recuperado
        else:
            print(f"Y({i}) != Y({i-1}) Por lo tanto No converge")
        vector_anterior = vector.copy()  # Actualizar el patrón anterior para la siguiente iteración
    return None  # Si no converge, retornar None

def asociarVector(patron_recuperado, vectores_entrenados):
    distancias = [np.sum(np.abs(patron_recuperado - vector)) for vector in vectores_entrenados]
    menor_distancia = min(distancias)
    indice_menor_distancia = distancias.index(menor_distancia)
    return indice_menor_distancia + 1  # Retorna el índice del vector con menor distancia

def main():
    num_vectores = int(input("Introduce el número de vectores: "))
    num_neuronas = int(input("Introduce el número de neuronas: "))

    # Leer los vectores de entrada
    vectores = []
    for i in range(num_vectores):
        print(f"Introduce los valores del vector {i+1} (solo -1 y 1 separados por espacio):")
        vector = list(map(int, input().split()))
        if len(vector) != num_neuronas or not all(v in [-1, 1] for v in vector):
            print("El vector debe tener la longitud correcta y solo valores -1 y 1. Intenta de nuevo.")
            exit()
        vectores.append(np.array(vector))  # Aceptamos el vector tal como es (-1 y 1)

    # Entrenar la red de Hopfield con los vectores dados
    W = calcularW(vectores, num_neuronas)

    # Imprimir la matriz de pesos
    print("\nMatriz de pesos W:")
    print(W)

    # Bucle para probar múltiples vectores ruidosos
    continuar = 's'
    while continuar.lower() == 's':
        # Pedir al usuario un patrón ruidoso/incompleto para recuperar
        print("Introduce el vector de prueba (solo -1 y 1):")
        patron_ruidoso = list(map(int, input().split()))
        if len(patron_ruidoso) != num_neuronas or not all(v in [-1, 1] for v in patron_ruidoso):
            print("El patrón debe tener la longitud correcta y solo valores -1 y 1. Intenta de nuevo.")
            exit()
        
        patron_ruidoso = np.array(patron_ruidoso)  # Convertimos el patrón a un array de numpy
        
        # Recuperar el patrón original, imprimiendo cada iteración
        patron_recuperado = recuperarHopfield(W, patron_ruidoso)

        # Si el patrón no converge, no se asocia a ningún vector
        if patron_recuperado is None:
            print("El patrón no converge y no se puede asociar a ningún vector de entrada.")
        else:
            # Asociar el patrón recuperado con los vectores entrenados
            vector_asociado = asociarVector(patron_recuperado, vectores)
            
            if vector_asociado is not None:
                print(f"El patrón recuperado se asocia con el vector {vector_asociado}.")
            else:
                print("El patrón recuperado no se asocia exactamente con ningún vector.")

        continuar = input("¿Quieres ingresar otro vector de prueba? (s/n): ").lower()

if __name__ == "__main__":
    main()
