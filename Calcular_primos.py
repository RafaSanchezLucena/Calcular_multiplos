# Calcula los números primos de una serie
# Autor: Rafa Sánchez
# Fecha: 06/03/2021
# Versión: 1.0
# Git

rango = int(input("¿Hasta qué número quieres calcular los primos?: "))
lista = []

for numero in range(2, rango + 1):
      contador = 0      # Si se mantiene a cero es un número primo.
      for i in range(2, rango + 1):
            if numero % i == 0 and numero != i:
                  contador = 1
                  break       # Cuando detecta un divisor, sale del bucle.
      if contador == 0:
            lista.append(numero)


print("El rango contiene los siguientes números primos: ")
print(lista)
print("Fin del programa")
