import numpy as np

np.random.seed(0)

x_data = [1, 2, 3, 4]
y_data = [147.8095238, 173.4126984, 146.8835979, 156.0352734]

import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data)