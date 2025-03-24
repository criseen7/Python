import numpy as np
from PIL import Image

def imagen_a_vector(image_path):
    # Cargar imagen y convertirla a escala de grises
    imagen = Image.open(image_path).convert('L')
    
    # Convertir la imagen a binaria usando un umbral (0 o 255)
    imagen_binaria = imagen.point(lambda p: 255 if p > 128 else 0)
    
    # Convertir la imagen en un array de numpy
    imagen_array = np.array(imagen_binaria)
    
    # Convertir los píxeles 255 en 1 y los 0 en -1
    vector = np.where(imagen_array == 255, 1, -1)
    
    # Aplanar la imagen (de 2D a 1D)
    vector = vector.flatten()
    
    return vector

def vector_a_imagen(vector, width, height):
    # Convertir los valores -1 a 0 y 1 a 255
    imagen_array = np.where(vector == 1, 255, 0)
    
    # Convertir el vector de nuevo a la forma de la imagen original
    imagen_array = imagen_array.reshape((height, width))
    
    # Crear una imagen de PIL a partir del array
    imagen_recuperada = Image.fromarray(np.uint8(imagen_array))
    
    return imagen_recuperada

# Función para entrenar la red de Hopfield
def entrenar_hopfield(vectores):
    n = len(vectores[0])  # El número de neuronas (longitud de los vectores)
    m = len(vectores)  # El número de patrones (imágenes)

    W = np.zeros((n, n))  # Inicializar la matriz de pesos en ceros
    
    # Recorrer todas las neuronas
    for i in range(n):
        for j in range(n):
            if i != j:  # Evitar auto-conexiones
                producto = 1
                for vector in vectores:
                    producto *= vector[i] * vector[j]  # Multiplicar todos los vectores
                W[i, j] = producto / n  # Normalizar por el número de neuronas
    
    return W

# Función de activación (función signo)
def activacion(x):
    return np.where(x >= 0, 1, -1)

# Función para recuperar un patrón a partir de un patrón ruidoso
def recuperar_hopfield(W, vector, iteraciones=10):
    vector_anterior = vector.copy()  # Copia del vector inicial para comparación
    for i in range(iteraciones):
        vector = activacion(np.dot(W, vector))  # Actualizar el vector de acuerdo a la matriz de pesos
        print(f"Iteración {i+1}: {vector}")  # Imprimir el vector en cada iteración
        if np.array_equal(vector, vector_anterior):  # Comparar con el patrón de la iteración anterior
            print(f"Patrón converge en la iteración {i+1}.")
            break  # Terminar la iteración si el patrón no cambia
        vector_anterior = vector.copy()  # Actualizar el patrón anterior para la siguiente iteración
    return vector

# Función para calcular la distancia de Hamming entre dos vectores
def distancia_hamming(vector1, vector2):
    return np.sum(vector1 != vector2)

# Nueva función para asociar la imagen recuperada con la de menor distancia de Hamming
def asociar_imagen_menor_distancia(vector_ruidoso, vectores_entrenamiento, nombres_imagenes):
    distancias = [distancia_hamming(vector_ruidoso, vector) for vector in vectores_entrenamiento]
    indice_menor_distancia = np.argmin(distancias)  # Índice del vector con menor distancia
    return nombres_imagenes[indice_menor_distancia], distancias[indice_menor_distancia]  # Devuelve el nombre y la distancia

def main():
    # Pedir al usuario las imágenes de entrenamiento
    num_imagenes = int(input("Introduce el número de imágenes a almacenar: "))
    
    vectores_entrenamiento = []
    nombres_imagenes = []  # Lista para almacenar los nombres de las imágenes
    dimensiones_imagen = None
    
    for i in range(num_imagenes):
        image_path = input(f"Introduce la ruta de la imagen {i+1}: ")
        vector_imagen = imagen_a_vector(image_path)
        
        # Guardar las dimensiones de la primera imagen para reconstrucción
        if dimensiones_imagen is None:
            dimensiones_imagen = Image.open(image_path).size
        
        vectores_entrenamiento.append(vector_imagen)
        nombres_imagenes.append(image_path)  # Guardar el nombre de la imagen
    
    # Entrenar la red de Hopfield con los vectores dados
    W = entrenar_hopfield(vectores_entrenamiento)
    
    # Imprimir la matriz de pesos
    print("\nMatriz de pesos W:")
    print(W)

    continuar = 's'
    while continuar == 's':
        # Pedir al usuario una imagen ruidosa/incompleta para recuperar
        image_path_ruido = input("Introduce la ruta de la imagen ruidosa/incompleta: ")
        vector_ruidoso = imagen_a_vector(image_path_ruido)
        
        # Calcular la distancia de Hamming entre el vector ruidoso y cada vector de entrada
        for i, vector_entrenamiento in enumerate(vectores_entrenamiento):
            distancia = distancia_hamming(vector_ruidoso, vector_entrenamiento)
        
        # Recuperar el patrón original, imprimiendo cada iteración
        patron_recuperado = recuperar_hopfield(W, vector_ruidoso)
        
        # Convertir el vector recuperado en una imagen y mostrarla
        imagen_recuperada = vector_a_imagen(patron_recuperado, *dimensiones_imagen)
        imagen_recuperada.show()  # Mostrar la imagen recuperada

        # Asociar la imagen recuperada con la de menor distancia de Hamming
        imagen_asociada, distancia = asociar_imagen_menor_distancia(vector_ruidoso, vectores_entrenamiento, nombres_imagenes)
        
        print(f"La imagen ruidosa '{image_path_ruido}' se asocia con la imagen '{imagen_asociada}'.\n") 
        for i, vector_entrenamiento in enumerate(vectores_entrenamiento):
            distancia = distancia_hamming(vector_ruidoso, vector_entrenamiento)
            print(f"Distancia de Hamming entre la imagen ruidosa y la imagen {nombres_imagenes[i]}: {distancia}")

    continuar = input("\n¿Quieres ingresar otra imagen ruidosa? (s/n): ").lower()

if __name__ == "__main__":
    main()
