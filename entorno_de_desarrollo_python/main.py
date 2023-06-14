import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,100)
y=np.sin(x)

plt.plot(x,y)

plt.title('Grafico de la funcion seno')
plt.xlabel('x')
plt.xlabel('y')
plt.grid(True)

plt.savefig('Grafico png')