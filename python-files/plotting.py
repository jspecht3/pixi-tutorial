import matplotlib.pyplot as plt
import numpy as np
from parser import (theta, cos, sin)

# plotting
fig, ax1 = plt.subplots()

c1 = 'b'
c2 = 'r'

# title
ax1.set_title("Basic Trig Functions from [-2pi, 2pi)", fontsize = "small")

# cos
ax1.plot(theta, cos, color = c1)
ax1.set_xlabel("Theta [rad]", fontsize = "small")
ax1.set_ylabel("Cos", color = c1, fontsize = "small")
ax1.tick_params(axis = 'y', labelcolor = c1)

# sin
ax2 = ax1.twinx()
ax2.plot(theta, sin, color = c2)
ax2.set_ylabel("Sin", color = c2, fontsize = "small")
ax2.tick_params(axis = 'y', labelcolor = c2)

# pi vertical lines
[ax1.axvline(drop, color = 'k', lw = 2, ls = ((0, (5, 3)))) for drop in (np.pi * np.arange(-2,3))]

fig.savefig("trig.png", dpi = 600, bbox_inches = "tight")
