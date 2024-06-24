import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ejercicio01.csv')
stats = data.groupby('City')['Temperature'].agg(['mean', 'min', 'max'])

fig, ax = plt.subplots()
stats.plot(kind='bar', y='mean', color='blue', ax=ax)
stats.plot(kind='line', y=['min', 'max'], marker='o', ax=ax)
plt.title('Análisis de Temperatura por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Temperatura')
plt.show()
