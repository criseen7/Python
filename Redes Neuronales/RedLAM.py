import numpy as np

def CalculaW(vectores_entrada, vectores_salida):
    """
    Función para entrenar una red LAM con los pares de vectores de entrada y salida.
    vectores_entrada: lista de vectores de entrada
    vectores_salida: lista de vectores de salida
    Devuelve la matriz de pesos W.
    """
    num_neuronas_entrada = len(vectores_entrada[0])  # Número de neuronas de entrada
    num_neuronas_salida = len(vectores_salida[0])  # Número de neuronas de salida
    
    W = np.zeros((num_neuronas_entrada, num_neuronas_salida))  # Inicializamos la matriz de pesos en ceros
    
    # Iterar sobre los pares de vectores de entrada y salida
    for a, b in zip(vectores_entrada, vectores_salida):
        # Convertir los vectores de entrada y salida usando la fórmula (2a - 1)(2b - 1)
        a_transformado = 2 * np.array(a) - 1
        b_transformado = 2 * np.array(b) - 1
        
        # Actualizar la matriz de pesos usando el producto externo de los vectores transformados
        W += np.outer(a_transformado, b_transformado)

    return W

def CalculrBias(W, num_neuronas_entrada, num_neuronas_salida):
    """
    Función para calcular el vector de bias O.
    W: matriz de pesos
    num_neuronas_entrada: número de neuronas en el vector de entrada
    num_neuronas_salida: número de neuronas en el vector de salida
    Devuelve el vector de bias O.
    """
    if num_neuronas_entrada == num_neuronas_salida:
        # Vectores de entrada y salida del mismo tamaño
        O = -0.5 * np.sum(W, axis=1)  # Suma a lo largo de las columnas
    else:
        # Vectores de entrada y salida de diferente tamaño
        O = -0.5 * np.sum(W.T, axis=1)  # Suma a lo largo de las filas de W transpuesta
    
    return O

def es_binario_o_bipolar(vector):
    """
    Determina si el vector es binario (1 y 0) o bipolar (1 y -1).
    """
    if all(x in [0, 1] for x in vector):
        return "binario"
    elif all(x in [-1, 1] for x in vector):
        return "bipolar"
    else:
        raise ValueError("El vector contiene valores no válidos. Debe contener solo 1s y 0s o 1s y -1s.")

def recuperarLAM(W, vector_entrada, O, num_neuronas_entrada, num_neuronas_salida):
    """
    Función para recuperar el vector de salida a partir de un vector de entrada y la matriz de pesos.
    W: matriz de pesos entrenada
    vector_entrada: vector de entrada para recuperación
    O: vector de bias
    Devuelve el vector de salida asociado.
    """
    tipo_entrada = es_binario_o_bipolar(vector_entrada)
    
    # Convertir el vector de entrada usando la fórmula 2a - 1
    if tipo_entrada == "binario":
        vector_entrada_transformado = 2 * np.array(vector_entrada) - 1  # Transformar 0s en -1s para cálculo
    else:
        vector_entrada_transformado = np.array(vector_entrada)
    
    if num_neuronas_entrada == num_neuronas_salida:
        # Si los vectores de entrada y salida son del mismo tamaño:
        Y = np.dot(W, vector_entrada_transformado) + O  # WX^T + O
    else:
        # Si los vectores de entrada y salida tienen diferentes tamaños:
        Y = np.dot(W.T, vector_entrada_transformado) + O  # W^TX^T + O
    
    if tipo_entrada == "binario":
        Y = np.where(Y >= 0, 1, 0)  # Función de transferencia para vectores binarios (1 y 0)
    else:
        Y = np.where(Y >= 0, 1, -1)  # Función de transferencia para vectores bipolares (1 y -1)
    
    return Y

def main():
    num_pares = int(input("Introduce el número de pares de vectores de entrada y salida: "))
    
    vectores_entrada = []
    vectores_salida = []
    
    # Ingresar los vectores de entrada y salida
    for i in range(num_pares):
        print(f"\nVector de entrada {i+1}:")
        vector_entrada = list(map(int, input("Introduce los valores del vector de entrada separados por espacios (1 o 0, o 1 o -1): ").split()))
        print(f"Vector de salida {i+1}:")
        vector_salida = list(map(int, input("Introduce los valores del vector de salida separados por espacios (1 o 0, o 1 o -1): ").split()))
        
        vectores_entrada.append(vector_entrada)
        vectores_salida.append(vector_salida)
    
    # Entrenar la red LAM con los vectores ingresados
    W = CalculaW(vectores_entrada, vectores_salida)
    
    # Imprimir la matriz de pesos
    print("\nMatriz de pesos W:")
    print(W)
    
    # Calcular el vector de bias
    num_neuronas_entrada = len(vectores_entrada[0])
    num_neuronas_salida = len(vectores_salida[0])
    O = CalculrBias(W, num_neuronas_entrada, num_neuronas_salida)
    
    # Imprimir el vector de bias
    print("\nVector de bias O:")
    print(O)
    
    # Recuperar los vectores de salida para cada uno de los vectores de entrada ingresados y comprobar asociación
    for i, (vector_entrada, vector_salida_original) in enumerate(zip(vectores_entrada, vectores_salida)):
        vector_salida_recuperado = recuperarLAM(W, vector_entrada, O, num_neuronas_entrada, num_neuronas_salida)
        
        print(f"\nVector de entrada {i+1}: {vector_entrada}")
        print(f"Vector de salida recuperado {i+1}: {vector_salida_recuperado}")
        print(f"Vector de salida original {i+1}: {vector_salida_original}")
        
        # Comparar si el vector de salida recuperado es igual al vector de salida original
        if np.array_equal(vector_salida_recuperado, vector_salida_original):
            print(f"El vector X{i+1} asocia con su vector de salida Y{i+1}")
        else:
            print(f"El vector X{i+1} NO asocia con su vector de salida Y{i+1}")

if __name__ == "__main__":
    main()