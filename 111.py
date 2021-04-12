%matplotlib inline

import os
import matplotlib.pyplot as plt
import numpy as np

y = lambda x: np.cos(x)
y_1 = lambda x: np.cos(x * 3)
fig = plt.subplots()
x = np.linspace(0, 10,100)
plt.plot(x, y(x))
plt.plot(x, y_1(x))
plt.show()