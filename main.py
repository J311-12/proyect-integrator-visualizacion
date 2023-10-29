import matplotlib.pyplot as plt
import pandas as pd

# Cargando los datos
df = pd.read_csv("datos_limpios.csv")

# Graficando la distribución de edades con un histograma
plt.hist(df["age"], bins=100)
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.title("Distribución de edades")
plt.show()

# Graficando histogramas agrupado por hombre y mujer:
# cantidad de anémicos
plt.bar(["Hombre", "Mujer"], df.groupby(["sex", "anemia"]).size(), width=0.4, align="edge",
        alpha=0.6)
plt.xlabel("Sexo")
plt.ylabel("Frecuencia")
plt.title("Cantidad de anémicos")
plt.show()

# cantidad de diabéticos
plt.bar(["Hombre", "Mujer"], df.groupby(["sex", "diabetes"]).size(), width=0.4, align="edge",
        alpha=0.6)
plt.xlabel("Sexo")
plt.ylabel("Frecuencia")
plt.title("Cantidad de diabéticos")
plt.show()

# cantidad de fumadores
plt.bar(["Hombre", "Mujer"], df.groupby(["sex", "smoking"]).size(), width=0.4, align="edge",
        alpha=0.6)
plt.xlabel("Sexo")
plt.ylabel("Frecuencia")
plt.title("Cantidad de fumadores")
plt.show()

# cantidad de muertos
plt.bar(["Hombre", "Mujer"], df.groupby(["sex", "is_dead"]).size(), width=0.4, align="edge",
        alpha=0.6)
plt.xlabel("Sexo")
plt.ylabel("Frecuencia")
plt.title("Cantidad de muertos")
plt.show()
