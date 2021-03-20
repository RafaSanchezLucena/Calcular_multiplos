# Calcula múltiplos de un número
# Autor: Rafa Sánchez
# Fecha: 05/03/2021
# Versión: 1.4


numero = int(input("Dame un número: "))

while numero != 0:
      contador = 0
      for i in range(2, numero):

            if numero % i == 0 and numero != i:
                  contador = 1
                  print("El numero", numero, "es múltiplo de", i)
            if i > numero / 2:      # Fin a la mitad del numero
                  break

      if contador == 0:  # No ha habido ningún resultado exacto
            print("El numero", numero, "es primo.")

      numero = int(input("Dame un número: "))

print("Fin del programa")
