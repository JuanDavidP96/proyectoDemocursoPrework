"""
Created on Sun Dec 19 19:44:17 2021

@author: Juan David
"""

import numpy as np
import matplotlib.pyplot as plt

#parametros

rho_a = 1.184 #[Kg/m^3]
m = 0.3552 #[Kg]
c_p = 1007 #[j/(Kg*K)]
I = 2 #[A]
Vol_punto = 0.5/60 #[m^3/s]
Vol_incu = 0.3 #[m^3]
m_punto = Vol_punto*rho_a #[Kg/min]
k_u = I/(m_punto*c_p)
Tao = m/m_punto #[min]
d = 298.15 #[K]

#Condiciones iniciales y finales
t_0 = 0
T_0 = 298.15 #[k]
V_0 = 50
t_f = 700
dt = 0.01
y_sp = 310.15 #[K]
K_p = (1/k_u)

Iteraciones = round(t_f/dt)

t = np.linspace(t_0,t_f, (Iteraciones+1))
errorc = np.zeros(Iteraciones+1)
ysp = np.zeros(Iteraciones+1)
Uc_euler = np.zeros(Iteraciones+1)
d_dif=np.zeros(Iteraciones+1)
V = 0
u = V
#Ecuación del método de euler

X_dif = np.zeros(Iteraciones+1)
X = T_0

for i in range(0,Iteraciones+1):
 
    X_dif[i] = X
    dXdt = (-X+(k_u*u)+d)/Tao
    X = X + dXdt*dt
    ec = (y_sp - X)*100/20
    errorc[i]= ec
    ysp[i]= y_sp
    uc = K_p * ec
    if uc > 100:
        uc = 100
    Uc_euler[i] = uc
    u = 120*uc/100+0
    d_dif[i] = d
   
#Gráfica
plt.figure(1) 
plt.subplot(411)
plt.plot(t,X_dif, 'b-', label = 'Temperatura')
plt.plot(t,ysp, 'r--', label = 'Y_sp')
plt.title("Modelo incubadora")
plt.ylabel("Temperatura [T]")
plt.grid(True) #divisiones en la grafica
plt.subplot(412)
plt.plot(t,Uc_euler, 'g-', label = 'Voltaje')
plt.xlabel("Tiempo [s]")
plt.ylabel("Voltaje")
plt.grid(True)
plt.subplot(413)
plt.plot(t,errorc, 'c-', label = 'Error')
plt.ylabel('Error')
plt.xlabel('Tiempo[s]')
plt.grid(True)
plt.subplot(414)
plt.plot(t,d_dif, 'y-', label = 'Perturbacion')
plt.ylabel('perturbacion')
plt.xlabel('Tiempo[s]')
plt.grid(True)