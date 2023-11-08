#Importing variables x and y from ChuaCircuitModel.py and analysing them here
#Make sure ChuaCircuitModel.py is in the same directory as this file otherwise it won't work

import ChuaCircuitModel
import numpy as np
import matplotlib.pyplot as plt

new_x = ChuaCircuitModel.x
new_y = ChuaCircuitModel.y
new_z = ChuaCircuitModel.z_mA
new_t = ChuaCircuitModel.t_ms

# Plot data
params = {'axes.labelsize': 'x-large'}
plt.rcParams.update(params)

plt.plot(new_x, new_y, linewidth = 0.40)
plt.xlabel('$V_2$ (V)')
plt.ylabel('$V_1$ (V)')

fig1 = plt.figure()
ax = fig1.add_subplot(projection='3d')
# Hide grid lines
ax.grid(False)
# Hide axes ticks
#ax.set_xticks([])
#ax.set_yticks([])
#ax.set_zticks([])
#label axes
ax.set_xlabel('$V_1$ (V)')
ax.set_ylabel('$V_2$ (V)')
ax.set_zlabel('I (mA)')
ax.plot(new_y, new_x, new_z, linewidth=0.40)

fig2, axs = plt.subplots(3, sharex=True)
axs[0].plot(new_t, new_x)
axs[1].plot(new_t, new_y)
axs[2].plot(new_t, new_z)

axs[0].set(ylabel = '$V_1$ (V)')
axs[1].set(ylabel = '$V_2$ (V)')
axs[2].set(ylabel = 'I (mA)')

axs[2].set(xlabel = 't (ms)')
axs[2].set_xlim([0, 10])

plt.show()

#Change font size and think about aspect ratios of photos when they're in the report