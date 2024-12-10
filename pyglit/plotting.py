from si_colors import *
print(denims)

import matplotlib.pyplot as plt

# Example chart using denims_palette
plt.bar(range(len(denims)), [1] * len(denims), color=denims)
plt.title("Denims Color Palette")
plt.show()