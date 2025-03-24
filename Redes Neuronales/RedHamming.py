import numpy as np

# Función de transferencia fh
def funcion_transferencia(x):
    if x > 1:
        return 1
    elif 0 <= x <= 1:
        return x
    else:
        return 0

# Aplicar la función de transferencia a un vector
def aplicar_transferencia(vector):
    return np.array([funcion_transferencia(v) for v in vector])

class HammingNetwork:
    def __init__(self, patrones):
        self.patrones = np.array(patrones)  # Convertimos los patrones de entrada en un array de numpy
        self.num_patrones = len(patrones)  # Número de patrones
        self.num_neuronas = len(patrones[0])  # Tamaño de cada vector de entrada
        
        # Matriz de pesos W según la fórmula W_ij = C_i / 2
        self.W = self.patrones / 2

        # Bias O_j = N / 2, donde N es el tamaño del vector de entrada
        self.O = np.full(self.num_patrones, self.num_neuronas / 2)

        # Factor epsilon
        self.epsilon = 1 / (self.num_neuronas - 1)
        
        print("\nMatriz de pesos W:")
        print(self.W)
        print("\nBias O:")
        print(self.O)

    def coincidencia(self, entrada):
        # Capa de coincidencia: calcular las coincidencias entre la entrada y los patrones
        coincidencias = np.dot(self.W, entrada) + self.O
        
        # Aplicamos la función de transferencia fh
        coincidencias_normalizadas = coincidencias / self.num_neuronas
        coincidencias_transferidas = aplicar_transferencia(coincidencias_normalizadas)

        return coincidencias_transferidas

    def competencia(self, coincidencias):
        # Capa de competencia: determinar el ganador (neuronas con mayor coincidencia)
        max_value = np.max(coincidencias)
        ganadoras = coincidencias == max_value  # Ver cuál tiene el máximo valor
        return ganadoras

    def actualizar_activaciones(self, activaciones):
        # Actualizar las activaciones de Yi con la fórmula Y(i+1) = fh(Uk(i) - e * sum Ui(t)), excluyendo Uk(i)
        nuevas_activaciones = activaciones.copy()
        
        for k in range(len(activaciones)):
            suma_excluyendo_k = np.sum([activaciones[j] for j in range(len(activaciones)) if j != k])
            nuevas_activaciones[k] = activaciones[k] - self.epsilon * suma_excluyendo_k
            print(f"Y{k} = {activaciones[k]} - {self.epsilon} * {suma_excluyendo_k} = {nuevas_activaciones[k]}")
        
        return aplicar_transferencia(nuevas_activaciones)

    def reconocer(self, entrada):
        # Reconocer el patrón más cercano al de entrada
        activaciones = self.coincidencia(entrada)
        
        # Iterar sobre las activaciones y actualizar hasta convergencia
        for i in range(10):
            print(f"\nY({i}) = {activaciones}")  # Imprimir el vector Y en cada iteración
            
            nuevas_activaciones = self.actualizar_activaciones(activaciones)
            activaciones_positivas = nuevas_activaciones[nuevas_activaciones > 0]
            
            if len(activaciones_positivas) == 0:
                print("No quedan activaciones positivas. No converge.")
                return None  # No converge y no asocia a ningún patrón
            elif len(activaciones_positivas) == 1:
                print(f"\nConverge en la iteración {i+1} con un solo valor positivo.")
                print(f"Y({i+1}) = {nuevas_activaciones}")
                break  # Convergencia exitosa
            
            activaciones = nuevas_activaciones
        
        ganadoras = self.competencia(activaciones)
        return ganadoras

def main():
    # Pedir el número de patrones de entrenamiento
    num_patrones = int(input("Introduce el número de patrones de entrenamiento: "))
    
    # Leer los patrones de entrada
    patrones = []
    for i in range(num_patrones):
        print(f"Introduce el patrón {i+1} (solo -1 y 1 separados por espacio):")
        patron = list(map(int, input().split()))
        patrones.append(np.array(patron))
    
    # Crear la red de Hamming
    red_hamming = HammingNetwork(patrones)
    
    continuar = 's'
    while continuar.lower() == 's':
        # Pedir un vector de prueba
        print("\nIntroduce el vector de prueba (solo -1 y 1 separados por espacio):")
        vector_prueba = list(map(int, input().split()))
        
        # Reconocer el patrón más cercano
        ganadoras = red_hamming.reconocer(np.array(vector_prueba))
        
        # Mostrar el resultado
        if ganadoras is None:
            print("El vector de prueba no se asocia con ningún patrón.\n")
        else:
            indices_ganadores = np.where(ganadoras)[0] + 1
            if len(indices_ganadores) == 1:
                print(f"\nEl vector de prueba se asocia con el patrón {indices_ganadores[0]}.\n")
            else:
                print("\nEl vector de prueba no se asocia con ningún patrón.")

        continuar = input("¿Quieres ingresar otro vector de prueba? (s/n): ").lower()

if __name__ == "__main__":
    main()
