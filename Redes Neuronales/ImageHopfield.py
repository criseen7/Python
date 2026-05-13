import numpy as np
from PIL import Image
import os

def imagen_a_vector(imagen):
    # Abrir imagen en modo blanco y negro (L)
    img = Image.open(imagen).convert('L')
    # Obtener el tamaño de la imagen (ancho x alto)
    ancho, alto = img.size
    # Convertir la imagen en una matriz numpy
    array = np.array(img)
    # Umbral para convertir a binario (1 para blanco, -1 para negro)
    array = np.where(array > 128, 1, -1)  # Pixel blanco será 1, negro será -1
    return array.flatten(), ancho * alto  # Convertir la matriz a un vector unidimensional y retornar tamaño

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
    return indice_menor_distancia, distancias  # Retorna el índice del vector con menor distancia y las distancias

def distanciaHamming(vector1, vector2):
    return np.sum(vector1 != vector2)

def main():
    num_vectores = int(input("Introduce el número de imágenes de entrenamiento: "))
    
    vectores = []
    nombres_imagenes = []  # Para almacenar los nombres de las imágenes
    tamaño_imagen = None   # Variable para almacenar el tamaño de las imágenes (ancho * alto)

    # Leer las imágenes de entrenamiento
    for i in range(num_vectores):
        ruta_imagen = input(f"Introduce la ruta de la imagen {i+1}: ")
        if not os.path.exists(ruta_imagen):
            print(f"La imagen {ruta_imagen} no existe. Intenta de nuevo.")
            exit()
        vector, tamaño = imagen_a_vector(ruta_imagen)  # Convertir la imagen a un vector y obtener el tamaño
        vectores.append(vector)  # Aceptamos el vector convertido
        nombres_imagenes.append(ruta_imagen)  # Guardar el nombre de la imagen

        # Si es la primera imagen, establecer el tamaño
        if tamaño_imagen == None:
            tamaño_imagen = tamaño
        elif tamaño != tamaño_imagen:
            print(f"Las imágenes deben tener el mismo tamaño. {ruta_imagen} tiene un tamaño diferente.")
            exit()

    num_neuronas = tamaño_imagen  # Las neuronas son el total de píxeles en la imagen
    
    # Entrenar la red de Hopfield con los vectores dados
    W = calcularW(vectores, num_neuronas)

    # Imprimir la matriz de pesos
    print("\nMatriz de pesos W:")
    print(W)

    # Bucle para probar múltiples imágenes ruidosas
    continuar = 's'
    while continuar.lower() == 's':
        # Pedir al usuario una imagen ruidosa/incompleta para recuperar
        ruta_imagen_prueba = input("Introduce la ruta de la imagen de prueba: ")
        if not os.path.exists(ruta_imagen_prueba):
            print(f"La imagen {ruta_imagen_prueba} no existe. Intenta de nuevo.")
            exit()

        patron_ruidoso, tamaño_prueba = imagen_a_vector(ruta_imagen_prueba)  # Convertimos la imagen a un vector
        
        # Verificar si la imagen de prueba tiene el mismo tamaño que las imágenes de entrenamiento
        if tamaño_prueba != tamaño_imagen:
            print(f"La imagen de prueba debe tener el mismo tamaño que las imágenes de entrenamiento ({tamaño_imagen} píxeles).")
            exit()
        
        # Recuperar el patrón original, imprimiendo cada iteración
        patron_recuperado = recuperarHopfield(W, patron_ruidoso)

        # Si el patrón no converge, no se asocia a ningún vector
        if patron_recuperado is None:
            print("El patrón no converge y no se puede asociar a ningún vector de entrada.")
        else:
            # Asociar el patrón recuperado con los vectores entrenados
            indice_asociado, distancias = asociarVector(patron_recuperado, vectores)
            imagen_asociada = nombres_imagenes[indice_asociado]
            
            print(f"La imagen ruidosa '{ruta_imagen_prueba}' se asocia con la imagen '{imagen_asociada}'.\n")
            
            # Imprimir la distancia de Hamming entre la imagen ruidosa y cada imagen de entrenamiento
            print("Distancias de Hamming entre la imagen ruidosa y las imágenes de entrenamiento:")
            for i, vector_entrenado in enumerate(vectores):
                distancia_hamming = distanciaHamming(patron_ruidoso, vector_entrenado)
                print(f"Distancia con '{nombres_imagenes[i]}': {distancia_hamming}")

        continuar = input("¿Quieres ingresar otra imagen de prueba? (s/n): ").lower()

if __name__ == "__main__":
    main()
