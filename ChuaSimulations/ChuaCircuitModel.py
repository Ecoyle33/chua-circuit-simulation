# ------Model of Lorentz attractor based off real values drawn from the Chua Circuit setup shown on chuacircuits.com---------

# Packages - scipy used to solve the ode
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def chua(r, t):

    x = r[0]   # Starting voltage across C1
    y = r[1]   # Starting Voltage across C2
    z = r[2]   # Starting current through Inductor

    # --------------Component Values--------------
    C1 = 10 * (1e-9)  # 10nF Capacitor
    C2 = 100 * (1e-9)  # 100nF Capacitor
    R = 1800  # 1.8k Ohms
    G = 1/R

    # ---------------Chua Diode-------------------
    # Resistor Values
    R1 = 220
    R2 = 220
    R3 = 2200
    R4 = 22000
    R5 = 22000
    R6 = 3300

    V0 = 9  # 9V input from batteries
    V1 = R3/(R2 + R3) * V0  # Potential difference across one Op amp
    V2 = R6/(R5 + R6) * V0  # Potential difference across the other Op amp

    # Gyrator values
    """
    R7 = 100
    R8 = 1000
    R9 = 1000
    R10 = 1800
    C = 100 * (1e-9)
    L = R7 * R9 * R10 * C/R8  # Equivalent to an inductance of 18mH; the equation here could be replaced with 18e-3 and it would give the same result
    """
    L = 18e-3
    # End Gyrator

    # Gradients in the I-V characteristic of the Chua Diode
    m01 = 1/R1
    m02 = 1/R4
    m11 = - 1/R3
    m12 = - 1/R6

    m1 = m12+m11

    if V1 > V2:
        m0 = m11 + m02

    else:
        m0 = m12 + m01

    mm1 = m01 + m02
    Vmax = max(V1, V2)
    Vmin = min(V1, V2)

    if abs(x) < Vmin:
        g = x * m1

    elif abs(x) < Vmax:
        g = x * m0

        if x > 0:
            g = g + Vmin * (m1 - m0)
        else:
            g = g + Vmin * (m0 - m1)

    elif abs(x) >= Vmax:
        g = x * mm1

        if x > 0:
            g = g + (Vmax * (m0 - mm1)) + (Vmin * (m1 - m0))
        else:
            g = g + (Vmax * (mm1 - m0)) + (Vmin * (m0 - m1))

    # Chua's Circuit Equations
    dV1_dt = (1/C1) * (G * (y - x) - g)
    dV2_dt = (1/C2) * (G * (x - y) + z)
    # Parasitic resistance term is removed as inductor gyrator has no parasitic resistance
    dI_dt = - (1/L) * y

    return [dV1_dt, dV2_dt, dI_dt]
# --------------End Chua Diode----------------

# Integrate to solve ODE

# Starting values
r0 = [-2.0, 0, 0]    # x = -0.5, y = -0.2, z = 0
len = 0.02                   # model duration
dt = 1e-7                   # sampling rate
t = np.arange(0, len, dt)   # create list of sampling times
t_ms = t*1000

ode = odeint(chua, r0, t)
x = ode[:, 0] #V1
y = ode[:, 1] #V2
z = ode[:, 2] #I
z_mA= z*1000 #Current in mA