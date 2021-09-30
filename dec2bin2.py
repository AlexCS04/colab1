# ------------------------------------------------------
# Convierte un número decimal positivo a binario usando un 
#   determinado número de bits.
# El binario resultante es un string e.g. "101"
# Se usa la función bin() que transforma e.g. 3 en "0b11".
# En esta función se quita el "0b" para dejar el "11"
# ------------------------------------------------------
def dec2bin(numero_decimal, numero_bits):
    n_b = bin(numero_decimal)
    n_b = n_b[2:len(n_b)]  # quita el "0b" del principio
    
    while len(n_b) < numero_bits:      # añade 0's a la izquierda si hace falta
         n_b = "0" + n_b
    return n_b

# ----------------------------------------
# MAIN
# ----------------------------------------
if __name__ == "__main__":
    # Pide al usuario el número a convertir y el número de bits 
    # Como el resultado de input es de tipo string, se convierte a entero usando int()
    numero_decimal = int(input("Escribe el número en decimal que quieres convertir: "))
    numero_bits = int(input("Cuantos bits tendrá el número binario: "))

    # se llama a la función dec2bin() para hacer la conversión
    n_b = dec2bin(numero_decimal, numero_bits)

    # Muestra por pantalla el resultado.
    # Para imprimir un entero es necesario convertirlo a string con str()
    print("El numero " + str(numero_decimal) + " es " + n_b + " en binario con " + str(numero_bits) + " bits.")
