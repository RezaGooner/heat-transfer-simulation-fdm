import numpy as np
import matplotlib.pyplot as plt

L = float(input("Rod length (meters): "))  
T = float(input("Simulation time (seconds): "))
nx = int(input("Number of spatial points: "))    
nt = int(input("Number of time steps: "))  
alpha = float(input("Thermal diffusivity (alpha): "))  

dx = L / (nx - 1)  
dt = T / nt   
r = alpha * dt / dx**2   

if r > 0.5:
    raise ValueError("Stability condition violated. Reduce dx or dt.")

u = np.zeros(nx)  
u[int(0.4 * nx):int(0.6 * nx)] = 100  
u_new = np.zeros_like(u)

for n in range(nt):
    for i in range(1, nx - 1):
        u_new[i] = u[i] + r * (u[i + 1] - 2 * u[i] + u[i - 1])
    u[:] = u_new  

    if n % 200 == 0:
        plt.plot(np.linspace(0, L, nx), u, label=f"t = {n * dt:.2f} s")

plt.title("Heat Equation Simulation")
plt.xlabel("Position (m)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid()
plt.show()
