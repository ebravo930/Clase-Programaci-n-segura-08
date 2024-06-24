
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ejercicio02.csv')
ventas_stats = data.groupby('Product')['Sales'].agg(['sum', 'mean'])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ventas_stats.plot(kind='bar', y='sum', ax=ax1, title='Ventas Totales por Producto', legend=False)
ventas_stats.plot(kind='bar', y='mean', ax=ax2, title='Ventas Promedio por Producto', color='green', legend=False)
plt.show()
