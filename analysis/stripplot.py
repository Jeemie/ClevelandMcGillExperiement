import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


error = pd.read_csv("compiledData.csv")
sb.set(style="darkgrid")
sb.stripplot(x="type", y="logError", data=error)
sb.pointplot("type", y="logError", data=error, color="black")
plt.show()