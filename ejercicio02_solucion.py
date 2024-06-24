import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv('ejercicio02.csv')
    while True:
        print("\nMenú:")
        print("1. Ver análisis de ventas por producto")
        print("2. Ver gráfico de ventas por producto")
        print("0. Salir")
        opcion = int(input("Ingrese su opción: "))
        
        if opcion == 0:
            break
        elif opcion == 1:
            producto = input("Ingrese el nombre del producto (Product A, Product B): ")
            mostrar_analisis(data, producto)
        elif opcion == 2:
            graficar_ventas(data)
        else:
            print("Opción no válida, intente de nuevo.")

def mostrar_analisis(data, producto):
    producto_data = data[data['Product'] == producto]
    print(f"\nAnálisis de Ventas para {producto}:")
    print("Ventas Totales:", producto_data['Sales'].sum())
    print("Ventas Promedio:", producto_data['Sales'].mean())
    print("Ventas Mínimas:", producto_data['Sales'].min())
    print("Ventas Máximas:", producto_data['Sales'].max())

def graficar_ventas(data):
    ventas_totales = data.groupby('Product')['Sales'].sum()
    ventas_totales.plot(kind='bar')
    plt.title('Ventas Totales por Producto')
    plt.xlabel('Producto')
    plt.ylabel('Ventas Totales')
    plt.xticks(rotation=0)
    plt.show()

if __name__ == "__main__":
    main()
