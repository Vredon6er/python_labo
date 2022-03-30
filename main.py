import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv('Capstone Data.csv', sep=';', header=0) # hier het pad naar je file zetten
print(dataframe)

############### meerdere run's in een csv file: zet hier je run nr. anders is dit 1
run = 7
run_i = dataframe.iloc[:, run*3-3:run*3]
run_i = run_i.dropna()
print(run_i)

data = run_i.to_numpy(copy=True)
data = np.transpose(data)
array1 = data[1]
array2 = data[2]
plt.scatter(array1,array2,marker=".")
plt.show()


