import numpy as np
import matplotlib.pyplot as plt

# Crear datos de ejemplo
x = np.linspace(0, 10, 100)  # Array de valores de x de 0 a 10
y = np.sin(x)  # Array de valores de y correspondientes a la función seno

# Crear el gráfico
plt.plot(x, y)

# Personalizar el gráfico
plt.title('Gráfico de la función seno')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Guardar grafico
plt.savefig('grafico.png')   