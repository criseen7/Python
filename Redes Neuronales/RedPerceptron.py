import numpy as np

def perceptron_simple():
    # Paso 1: Solicitar datos al usuario
    bias = float(input("Ingresa el valor del bias: "))
    
    print("\nIngresa el vector de entrada 1 (4 valores separados por espacio): ")
    entrada1 = np.array(list(map(float, input().split()))).reshape(1, 4)
    
    print("Ingresa el vector de entrada 2 (4 valores separados por espacio): ")
    entrada2 = np.array(list(map(float, input().split()))).reshape(1, 4)
    
    print("Ingresa el vector de salida ideal (4 valores separados por espacio): ")
    salida_ideal = np.array(list(map(float, input().split()))).reshape(1, 4)
    
    alfa = float(input("Ingresa el valor de alfa (0 < alfa <= 1): "))
    
    print("\nIngresa la matriz de pesos inicial de tamaño [3][1] (3 valores separados por espacio): ")
    matriz_pesos = np.array(list(map(float, input().split()))).reshape(3, 1)
    
    # Paso 2: Imprimir los datos en formato de tabla
    print("\nTabla de entradas y salidas ideales:")
    print(f"{'Bias':^10}{'Entrada 1':^15}{'Entrada 2':^15}{'Salida Ideal':^15}")
    for i in range(4):
        print(f"{bias:^10}{entrada1[0][i]:^15}{entrada2[0][i]:^15}{salida_ideal[0][i]:^15}")
    
    # Crear el vector de entradas incluyendo el bias
    entradas = np.vstack(([bias] * 4, entrada1, entrada2)).T

        # Paso 3: Calcular salida, error y ajustar matriz de pesos
    errores_totales = 0
    band=-1
    i=0
    while i<=3:
        error = 1  # Inicializar el error para entrar en el bucle
        j=1
        if i==band :
             i+=1
             if i>3:
                 break
        while error != 0:  # Recalcular mientras haya error
            # Calcular la salida Yi como la suma de los productos W * Xi
            Xi = entradas[i].reshape(3, 1)
            suma = np.dot(matriz_pesos.T, Xi)[0, 0]  # Producto punto de W y Xi
            Yi = 1 if suma >= 0 else -1  # Función de transferencia escalón

            # Imprimir salida calculada Yi
            print(f"\nPara Patron {i+1}:")
            print(f"Iteracion {j}: ")
            print(f"   Vector de entrada (bias + entradas): {Xi.T}")
            print(f"   Producto punto W·X: {suma}")
            print(f"   Salida calculada Yi: {Yi}")
                    
            # Calcular error e = salida ideal - salida calculada
            error = salida_ideal[0][i] - Yi
            print(f"   Salida ideal: {salida_ideal[0][i]}")
            print(f"   Error calculado: {error}")
                    
            # Si el error no es cero, ajustar matriz de pesos
            if error != 0:
                ajuste = alfa * error * Xi
                print(f"   Ajuste en pesos = alfa * error * Xi = {alfa} * {error} * {Xi.T}")
                matriz_pesos = matriz_pesos + ajuste
                print(f"   Nueva matriz de pesos después del ajuste:\n{matriz_pesos}")
                errores_totales += 1  # Contar este error
                band=i
                if band!=0:
                    i=-1
            j+=1
        i+=1    

    print("\nLa matriz de pesos final con todos los errores en cero es:")
    print(matriz_pesos)

# Ejecutar el programa
if __name__ == "__main__":
    perceptron_simple()