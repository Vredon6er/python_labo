import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv('Capstone Data.csv', sep=';', header=0) # hier het pad naar je file zetten
print(dataframe)

############### meerdere run's in een csv file: zet hier je run nr. anders is dit 1
run = 1 # als je meerdere run's in een file hebt
run_i = dataframe.iloc[:, run*3-3:run*3] # doe hier *2 en -2 als je alleen maar positie en intensiteit hebt en niet de tijd.
run_i = run_i.dropna()
print(run_i)

data = run_i.to_numpy(copy=True)
data = np.transpose(data)
array1 = data[0]  #deze waarde is 0,1 of 2 (afhankelijk van hoe de data file er uit ziet)
array2 = data[1]  #deze waarde is 0,1 of 2 (afhankelijk van hoe de data file er uit ziet)
plt.scatter(array1,array2,marker=".")
plt.show()


