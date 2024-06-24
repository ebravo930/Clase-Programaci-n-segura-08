import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv('ejercicio01.csv')
    while True:
        print("\nMenú:")
        print("1. Ver análisis de temperatura por ciudad")
        print("2. Ver gráfico de temperatura semanal por ciudad")
        print("0. Salir")
        opcion = int(input("Ingrese su opción: "))
        
        if opcion == 0:
            break
        elif opcion == 1:
            ciudad = input("Ingrese el nombre de la ciudad (New York, London, Tokyo, Santiago): ")
            mostrar_analisis(data, ciudad)
        elif opcion == 2:
            ciudad = input("Ingrese el nombre de la ciudad para graficar: ")
            graficar_temperaturas(data, ciudad)
        else:
            print("Opción no válida, intente de nuevo.")

def mostrar_analisis(data, ciudad):
    ciudad_data = data[data['City'] == ciudad]
    print(f"\nAnálisis de Temperaturas para {ciudad}:")
    print("Temperatura Promedio:", ciudad_data['Temperature'].mean())
    print("Temperatura Mínima:", ciudad_data['Temperature'].min())
    print("Temperatura Máxima:", ciudad_data['Temperature'].max())
    print("Últimos 3 días de Temperaturas Registradas:")
    print(ciudad_data.tail(3))
    x = input("Pulse una tecla para continuar.....")

def graficar_temperaturas(data, ciudad):
    ciudad_data = data[data['City'] == ciudad]
    plt.figure()
    plt.plot(ciudad_data['Date'], ciudad_data['Temperature'], marker='o', linestyle='-')
    plt.title(f'Temperatura Semanal en {ciudad}')
    plt.xlabel('Fecha')
    plt.ylabel('Temperatura (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

