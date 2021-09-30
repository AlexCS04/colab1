
def dec2bin(numero_decimal, numero_bits):
    numero_binario = bin(numero_decimal)
    numero_binario = numero_binario[2:len(numero_binario)]  # quita el "0b" del principio
    
    while len(numero_binario) < numero_bits:      # añade 0's a la izquierda si hace falta
        numero_binario = "0" + numero_binario
    return numero_binario

# ----------------------------------------
# MAIN
# ----------------------------------------
if __name__ == "__main__":

    numero_decimal = int(input("Escribe el número en decimal que quieres convertir: "))
    numero_bits = int(input("Cuantos bits tendrá el número binario: "))

    numero_binario = dec2bin(numero_decimal, numero_bits)

    print("El numero " + str(numero_decimal) + " es " + numero_binario + " en binario con " + str(numero_bits) + " bits.")
