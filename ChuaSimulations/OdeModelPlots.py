import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

## default parameters, model settings
a = 15.6                      # a & b dependant on component values
b = 26.05
R = -(10/7)                    # resistor value
C2 = -(5/7)                   # voltage across capacator 2 (see wikipedia diagram)
r0 = [-1, 0, 0]            # initial xyz
dur = 80                # model duration
dt = 1e-3                   # sampling rate

t = np.arange(0, dur, dt)   # create list of sampling times

# chua circuit model to be integrated by scipy odeint
def circ(r, t):
    x, y, z = r

    # response of nonlinear resistor
    f = C2 * x + 0.5 * (R - C2) * (abs(x + 1) - abs(x - 1))

    # ODEs
    dx = a * (y - x - f)
    dy = (1/C2*R) * (x - y + z)
    dz = -b * y
    
    # ODE array to pass to odeint
    return [dx, dy, dz]

# integrate
data = odeint(circ, r0, t)

x = data[:, 0] #V1
y = data[:, 1] #V2
z = data[:, 2] #I

plt.plot(x, y, color="black", linewidth = 0.40)
plt.xlabel('x')
plt.ylabel('y')

"""
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot(x, y, z, linewidth=0.3)
"""

fig2, axs = plt.subplots(2, sharex=True)
#fig2.suptitle('x, y and z against t')
axs[0].plot(t, x)
axs[1].plot(t, y)
#axs[2].plot(t, z)

axs[0].set(ylabel = 'x')
axs[1].set(ylabel = 'y')
#axs[2].set(ylabel = 'z')

axs[1].set(xlabel = 't')

#axs[0].set_ylim(-2, 2)
#axs[1].set_ylim(-0.3, 0.3)
#axs[2].set_ylim(-3, 3)

plt.xticks(np.arange(min(t), max(t)+1, 10))
plt.show()