import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('seaborn-poster')
#%matplotlib inline
n= 10
L=1
h = (L-0) / n
#Matriz A
A = np.zeros((n+1, n+1))
A[0,0]=1
A[1,1]=-2
A[1,2]=1
A[n,n]= 1
for i in range(2, n):
    A[i , i-1] = 1
    A[i , i] = -2
    A[i , i+1] = 1
print (A)
#Matriz B
x=np.linspace(0, 1, n+1)
b=np.zeros(n+1)
for i in range(1, n+1):
    b[i] = -x[i]*h**2
print (b)
#Solucion del sistema lineal de ecuaciones
u = np.linalg.solve(A, b)
print(u)
xl = np.linspace(0,1,n+1)
#Creacion de grafica de solucion del sistema de ecuaciones
plt.figure(figsize=(10,8))
plt.plot(xl, u)
plt.plot(0, 0.1)
plt.title('Solucion Numerica')
plt.xlabel('X')
plt.ylabel('U')
plt.show()
#Solucion Analitica
y=np.linspace(0, 1, 10)
print("Solucion numerica")
print(u)
print('Solucion analitica')
u_x=(y/6)*(1-y**2)
print(u_x)
plt.figure(figsize=(10,8))
plt.plot(y, u_x)
plt.plot(0, 0.1)
plt.title('Solucion Analitica')
plt.xlabel('(x)')
plt.ylabel('u(x)')
plt.show()
