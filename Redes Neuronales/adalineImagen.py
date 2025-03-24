import numpy as np
from PIL import Image
import glob
import random

# Configuración inicial de la red de Adaline
input_size = 15 * 15  # 15x15 píxeles
bias = 1
alpha = random.uniform(0.01, 1)  # Tasa de aprendizaje aleatoria en rango (0, 1]
max_iteracions = 100  # Número máximo de épocas de entrenamiento

# Función de activación (lineal)
def activation(x):
    return x  # Sin función de activación, salida directa

# Clase Adaline
class Adaline:
    def __init__(self, input_size, bias, alpha):
        self.weights = np.random.rand(input_size)  # Pesos iniciales aleatorios
        self.bias = bias
        self.alpha = alpha

    def predict(self, inputs):
        # Calcula la salida (sin función de activación, solo suma ponderada)
        total_input = np.dot(inputs, self.weights) + self.bias
        return total_input

    def train(self, training_inputs, labels):
        for iteracion in range(max_iteracions):
            total_error = 0  # Contador de errores en cada época
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                total_error += error ** 2  # Error cuadrático

                # Ajuste de pesos y bias con el gradiente descendente
                self.weights += self.alpha * error * inputs
                self.bias += self.alpha * error  # Ajuste de bias

            # Verificar si el error total es suficientemente pequeño
            if total_error == 0:
                print(f"Entrenamiento completo en {iteracion + 1} épocas.")
                break
        else:
            print(f"Entrenamiento completado en el máximo de {max_iteracions} épocas.")

# Cargar las imágenes de entrenamiento y convertirlas a vectores
def load_images(folder, pattern, label, size=(15, 15)):
    images = []
    labels = []
    for filename in glob.glob(f"{folder}/{pattern}"):
        img = Image.open(filename).convert('L')
        img = img.resize(size)
        img_array = np.array(img).flatten() / 255  # Escala los valores a 0 y 1
        images.append(img_array)
        labels.append(label)
    return images, labels

# Cargar imágenes de la letra A y O
train_images_a, train_labels_a = load_images("ImagenesAO", "A_*.png", 1)
train_images_o, train_labels_o = load_images("ImagenesAO", "O_*.png", 0)

# Unir imágenes y etiquetas de entrenamiento
training_inputs = np.array(train_images_a + train_images_o)
training_labels = np.array(train_labels_a + train_labels_o)

# Crear y entrenar el modelo Adaline
adaline = Adaline(input_size, bias, alpha)
adaline.train(training_inputs, training_labels)

# Imprimir el alfa, el bias, y las matrices de entrenamiento
print(f"Alpha (tasa de aprendizaje): {alpha}")
print(f"Bias: {bias}")
print("Matriz de entrenamiento (entradas):")
print(training_inputs)
print("Matriz de entrenamiento (etiquetas):")
print(training_labels)

# Función para probar con una imagen nueva
def test_adaline():
    while True:
        # Pedir al usuario una imagen de prueba
        filename = input("Ingresa el nombre del archivo de la imagen de prueba (ej: prueba.png): ")
        img = Image.open(filename).convert('L')
        img = img.resize((15, 15))
        img_array = np.array(img).flatten() / 255

        # Imprimir la matriz de prueba
        print("Matriz de prueba:")
        print(img_array)

        # Realizar predicción
        result = adaline.predict(img_array)
        if result >= 0.5:
            print("La imagen ingresada es una 'A'")
        else:
            print("La imagen ingresada es una 'O'")

        # Preguntar si quiere realizar otra prueba
        another_test = input("¿Deseas ingresar otra imagen de prueba? (s/n): ").strip().lower()
        if another_test == 'n':
            print("Fin del programa.")
            break

# Ejecutar la prueba
test_adaline()