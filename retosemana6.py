print("¡¡ Bienvenido comenzemos... ")

print("Para acceder tu contraseña debe comenzar con un numero y tener minimo 6 caracteres...")
# Definir el número máximo de intentos permitidos
max_intentos = 3

# Inicializar el contador de intentos
intentos = 0

# Bucle principal para solicitar la contraseña
while intentos < max_intentos:
    # 1. Solicita una contraseña que inicie con un número y tenga al menos 6 dígitos
    contraseña1 = input("Ingrese una contraseña: ")

    # Validar que la contraseña tenga al menos 6 caracteres y comience con un número
    if len(contraseña1) < 6 or not contraseña1[0].isdigit():
        print("La contraseña debe comenzar con un número y tener al menos 6 caracteres.")
        intentos += 1
        # Si se exceden los intentos, se sale del bucle
        if intentos == max_intentos:
            print("Fin del programa.")
            break
        # Volver al inicio del bucle para pedir de nuevo la contraseña
        continue

    # 2. Pide ingresar nuevamente la contraseña y verificar que coincida
    contraseña2 = input("Ingrese la contraseña nuevamente: ")

    # Verificar si las contraseñas coinciden
    if contraseña1 == contraseña2:
        print("Contraseña correcta")
        print("Fin del programa")
        # Si la contraseña es correcta, se sale del bucle
        break
    else:
        print("Las contraseñas no coinciden")
        intentos += 1
        # Si se exceden los intentos, se sale del bucle
        if intentos == max_intentos:
            print("Fin del programa.")
            break