import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandasgui import show
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Datos ficticios
n = 100  # muestras
# Generar valores para la cantidad de fertilizante (x) en un rango de 0 a 100 kg
np.random.seed(42)  # reproducibilidad
fertilizante = np.random.uniform(0, 100, n)
# Definir una relación lineal con ruido para la cantidad de papas
# Suponiendo que 1kg de fertilizante obtendremos 0.8 toneladas
# Y agregamos un poco de ruido normal para simular variedad
papas = 0.8 * fertilizante + np.random.normal(0, 5, n) + 8  # Intercepto en 8 toneladas

df = pd.DataFrame({
    'Fertilizante (Kg)': fertilizante,
    'Papas (Toneladas)': papas
})

x = df[['Fertilizante (Kg)']].values
y = df["Papas (Toneladas)"]

# Separar los datos de entrenamiento y de prueba
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Definir modelo y entrenarlo
regresor = LinearRegression()
regresor.fit(X_train, Y_train)

# Hacer la predicción
Y_pred = regresor.predict(X_test)

# Coeficientes
b1 = regresor.coef_[0]
b0 = regresor.intercept_

print(f"""
      b1: {b1}
      b0: {b0}
    """)

# Calcular el MSE, RMSE, R^2
mse = mean_squared_error(Y_test, Y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(Y_test, Y_pred)

print(f"""
        mse: {mse}
        rmse: {rmse}
        r2: {r2}
    """)

# Graficar datos de entrenamiento
plt.figure(figsize=(10, 6))
plt.scatter(X_train, Y_train, color='blue', label='Datos de Entrenamiento')
plt.title("Regresión Lineal: Fertilizante vs Producción de Papas")
plt.xlabel("Fertilizante (Kg)")
plt.ylabel("Papas (Toneladas)")
plt.legend()
plt.show()

# Graficar datos de prueba
plt.figure(figsize=(10, 6))
plt.scatter(X_test, Y_test, color='green', label='Datos de Prueba')
plt.title("Regresión Lineal: Fertilizante vs Producción de Papas")
plt.xlabel("Fertilizante (Kg)")
plt.ylabel("Papas (Toneladas)")
plt.legend()
plt.show()

# Mostrar la interfaz interactiva
show(df)
