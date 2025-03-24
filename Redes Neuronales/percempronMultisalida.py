import numpy as np
from PIL import Image
import glob
import random

# Configuración inicial del perceptrón
input_size = 15 * 15  # 15x15 pixels
num_outputs = 2       # Dos clases: 'A' y 'O'
bias = 1
alpha = random.uniform(0.01, 1)  # Tasa de aprendizaje aleatoria en rango (0, 1]
max_epochs = 1000  # Número máximo de épocas de entrenamiento

# Función de activación (paso escalonado)
def activation(x):
    return np.where(x >= 0, 1, 0)

# Clase del perceptrón multisalidas
class MultiOutputPerceptron:
    def __init__(self, input_size, num_outputs, bias, alpha):
        self.weights = np.random.rand(input_size, num_outputs)  # Matriz de pesos aleatoria
        self.bias = np.random.rand(num_outputs)  # Bias aleatorio para cada salida
        self.alpha = alpha

    def predict(self, inputs):
        # Calcula las salidas de todas las neuronas
        total_input = np.dot(inputs, self.weights) + self.bias
        return activation(total_input)  # Activación para cada salida

    def train(self, training_inputs, labels):
        for epoch in range(max_epochs):
            errors = 0  # Contador de errores en cada época
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                if np.any(error != 0):
                    errors += 1
                    # Ajustar pesos y bias para cada salida
                    self.weights += self.alpha * np.outer(inputs, error)
                    self.bias += self.alpha * error
            
            # Verificar si todos los ejemplos fueron clasificados correctamente
            if errors == 0:
                print(f"Entrenamiento completo en {epoch + 1} épocas.")
                break
        else:
            print(f"Entrenamiento completado en el máximo de {max_epochs} épocas.")

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
train_images_a, train_labels_a = load_images("ImagenesAO", "A_*.png", [1, 0])  # Clase A: [1, 0]
train_images_o, train_labels_o = load_images("ImagenesAO", "O_*.png", [0, 1])  # Clase O: [0, 1]

# Unir imágenes y etiquetas de entrenamiento
training_inputs = np.array(train_images_a + train_images_o)
training_labels = np.array(train_labels_a + train_labels_o)

# Crear y entrenar el perceptrón
perceptron = MultiOutputPerceptron(input_size, num_outputs, bias, alpha)
perceptron.train(training_inputs, training_labels)

# Imprimir información del entrenamiento
print(f"Alpha (tasa de aprendizaje): {alpha}")
print(f"Bias inicial: {bias}")
print("Matriz de entrenamiento (entradas):")
print(training_inputs)
print("Matriz de entrenamiento (etiquetas):")
print(training_labels)

# Función para probar con una imagen nueva
def test_perceptron():
    while True:
        # Pedir al usuario una imagen de prueba
        filename = input("Ingresa el nombre del archivo de la imagen de prueba (ej: prueba.png): ")
        img = Image.open(filename).convert('L')
        img = img.resize((15, 15))
        img_array = np.array(img).flatten() / 255

        # Realizar predicción
        result = perceptron.predict(img_array)
        print(f"Vector de salida predicho: {result}")
        if np.array_equal(result, [1, 0]):
            print("La imagen ingresada es una 'A'")
        elif np.array_equal(result, [0, 1]):
            print("La imagen ingresada es una 'O'")
        else:
            print("La imagen no se clasifica correctamente.")

        # Preguntar si quiere realizar otra prueba
        another_test = input("¿Deseas ingresar otra imagen de prueba? (s/n): ").strip().lower()
        if another_test == 'n':
            print("Fin del programa.")
            break

# Ejecutar la prueba
test_perceptron()
