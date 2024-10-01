def obtener_numero_natural():
    while True:
        try:
            # Solicitamos al usuario ingresar un número
            numero = int(input("Ingrese un número natural: "))
            if numero < 1:
                raise ValueError("El número debe ser mayor que 0.")
            return numero
        except ValueError as e:
            print(f"Error: {e}. Por favor, intente de nuevo.")

def calcular_divisores(numero):
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores

# Programa principal
if __name__ == "__main__":
    numero = obtener_numero_natural()
    divisores = calcular_divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")
