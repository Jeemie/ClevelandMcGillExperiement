import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


error = pd.read_csv("compiledData.csv")
sb.set(style="darkgrid")
sb.pointplot("logError", y="type", data=error, join=False, capsize=.2, hue="type")
plt.show()