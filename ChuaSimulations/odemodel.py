import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

## default parameters, model settings
a = 17                      # a & b dependant on component values
b = 28
R = -1.1                    # resistor value
C2 = -0.6                   # voltage across capacator 2 (see wikipedia diagram)
r0 = [0.1, 0, 0]            # initial xyz
dur = 400                   # model duration
dt = 1e-3                   # sampling rate

t = np.arange(0, dur, dt)   # create list of sampling times

# chua circuit model to be integrated by scipy odeint
def circ(r, t):
    x, y, z = r

    # response of nonlinear resistor
    f = C2 * x + 0.5 * (R - C2) * (abs(x + 1) - abs(x - 1))

    # ODEs
    dx = a * (y - x - f)
    dy = x - y + z
    dz = -b * y
    
    # ODE array to pass to odeint
    return [dx, dy, dz]

# integrate
data = odeint(circ, r0, t)

# plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot(data[:,0], data[:,1], data[:,2], linewidth=0.3)
plt.show()