import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generar datos aleatorios
np.random.seed(0)
data = np.random.randn(100)

# Visualizar los datos utilizando Seaborn
sns.set(style="whitegrid")
sns.histplot(data, kde=True)
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Histograma de datos aleatorios")
plt.savefig("histograma.png")
