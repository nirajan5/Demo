
# Python program to Plot Rose curve with even number of petals
import numpy as np
import matplotlib
from matplotlib import pyplot as plt


theta = np.linspace(0, 2*np.pi, 1000)

r = 3* np.sin(8 * theta)

plt.polar(theta, r, 'r')

plt.show()
