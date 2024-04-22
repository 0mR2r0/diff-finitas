"""
Ejemplo de diferencias finitas discretizando el espacio y el tiempo con animacion en el grafico
"""
import numpy as np
import matplotlib.pyplot as plt
#Datos
L=1
alpha=0.1
#discretizacion
N=5
x=np.linspace(0,L,N)
dx=L/(N-1)

#Condiciones iniciales
t=0
T_ini=1000
T=np.ones(N)*T_ini
#Condiciones de frontera
T_0=25
T[0]=T_0
T_L=100
T[-1]=T_L

#Solucion con el tiempo
dt=0.1
tfin=20
Tdt=T.copy()
Tsol=[T]
tsol=[t]

while t<tfin:
  #Se crea una matriz para colocar el sistema de ecuaciones de la forma Ax=b
  A=np.zeros((N,N))
  b=np.zeros(N)
  for i in range(N):
    if i==0:
      #Condiciones del nodo 0
      A[i][i]=1
      b[i]=T_0
    elif i==N-1:
      #Condiciones del ultimo nodo N-1
      A[i][i]=1
      b[i]=T_L
    else:
      #Se escriben las ecuaciones de las diagonales de la matriz
      #Matriz A
      A[i][i]=1+2*alpha*dt/dx**2
      A[i][i-1]=-alpha*dt/dx**2
      A[i][i+1]=-alpha*dt/dx**2
      #Matriz b
      b[i]=T[i]
  #Obtener la inversa de la matriz
  Ainv=np.linalg.inv(A)
  Tdt=np.dot(Ainv,b)

  T=Tdt.copy()
  t=t+dt
  Tsol.append(T)
  tsol.append(t)
#crear las grafica animada
import matplotlib.animation as animation
fig=plt.figure()
ax=plt.gca()

#Definir funcion que contendra los datos para la animacion
def actualizar(i):
  ax.clear()
  plt.plot(x, Tsol[i],'ro')
  plt.title(str(round(tsol[i],5)))
  #Definir limites del grafico
  plt.xlim(0,L)
  plt.ylim(0,1000)
ani=animation.FuncAnimation(fig, actualizar, range(len(tsol)))
plt.show()
