import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv('/Users/joren/Downloads/run_7_data.csv', sep=';', header=0,decimal=',') # hier het pad naar je file zetten
print(dataframe)

############### meerdere run's in een csv file: zet hier je run nr. anders is dit 1

run_i = dataframe.iloc[:, :]
run_i = run_i.dropna()
print(run_i)

data = run_i.to_numpy(copy=True)
data = np.transpose(data)
array1 = data[0]
array2 = data[1]

fig, ax = plt.subplots()
ax.scatter(array1, array2, marker=".")
#ax.set( xticks=np.linspace(0, 350,10), yticks=np.linspace(0, 1.5,10))
plt.show()
