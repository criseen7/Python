import numpy as np
from PIL import Image
import glob
import random
import matplotlib.pyplot as plt

# Configuración inicial de la red neuronal
input_size = 15 * 15  # 15x15 pixels
hidden_size = 10      # Tamaño de la capa oculta
num_outputs = 2       # Dos clases: 'A' y 'O'
bias = 1
alpha = random.uniform(0.01, 1)  # Tasa de aprendizaje aleatoria en rango (0, 1]
max_epochs = 100000  # Número máximo de épocas de entrenamiento

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide
def sigmoid_derivative(x):
    return x * (1 - x)

# Clase para el perceptrón multicapa
class MultiLayerPerceptron:
    def __init__(self, input_size, hidden_size, num_outputs, bias, alpha):
        # Inicialización de pesos de las capas
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)  # Pesos de la capa de entrada a la capa oculta
        self.weights_hidden_output = np.random.rand(hidden_size, num_outputs)  # Pesos de la capa oculta a la capa de salida
        self.bias_hidden = np.random.rand(hidden_size)  # Bias para la capa oculta
        self.bias_output = np.random.rand(num_outputs)  # Bias para la capa de salida
        self.alpha = alpha  # Tasa de aprendizaje

    def predict(self, inputs):
        # Propagación hacia adelante
        self.hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)  # Salida de la capa oculta
        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        return sigmoid(self.final_input)  # Salida final de la red

    def train(self, training_inputs, labels):
        mse_per_epoch = []  # Lista para almacenar el MSE de cada época
        for epoch in range(max_epochs):
            errors = 0  # Contador de errores en cada época
            mse = 0  # Error cuadrado promedio
            for inputs, label in zip(training_inputs, labels):
                # Propagación hacia adelante
                prediction = self.predict(inputs)
                
                # Calcular el error en la capa de salida
                error_output = label - prediction
                errors += np.sum(np.abs(error_output))  # Contar los errores

                # Cálculo del error cuadrado
                mse += np.mean(np.square(error_output))  # Sumar el error cuadrado para la predicción
                
                # Backpropagation
                # Calcular el gradiente de la capa de salida
                delta_output = error_output * sigmoid_derivative(prediction)
                
                # Calcular el gradiente de la capa oculta
                delta_hidden = delta_output.dot(self.weights_hidden_output.T) * sigmoid_derivative(self.hidden_output)

                # Actualizar los pesos y los biases
                self.weights_hidden_output += self.alpha * self.hidden_output.T.dot(delta_output)
                self.bias_output += self.alpha * np.sum(delta_output, axis=0)

                self.weights_input_hidden += self.alpha * inputs.T.dot(delta_hidden)
                self.bias_hidden += self.alpha * np.sum(delta_hidden, axis=0)

            # Promediar el error cuadrado de todos los ejemplos
            mse_per_epoch.append(mse / len(training_inputs))

            # Verificar si todos los ejemplos fueron clasificados correctamente
            if errors == 0:
                print(f"Entrenamiento completo en {epoch + 1} épocas.")
                break
        else:
            print(f"Entrenamiento completado en el máximo de {max_epochs} épocas.")
        
        # Graficar el error cuadrado promedio
        plt.plot(mse_per_epoch)
        plt.title('Error Cuadrado Promedio (MSE) por Época')
        plt.xlabel('Época')
        plt.ylabel('Error Cuadrado Promedio (MSE)')
        plt.show()

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

# Crear y entrenar la red neuronal
mlp = MultiLayerPerceptron(input_size, hidden_size, num_outputs, bias, alpha)
mlp.train(training_inputs, training_labels)

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
        result = mlp.predict(img_array)
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
