# retosemana6contrase-a
se pide al usuario ingresar una contraseña de 6 caracteres iniciando con numero

Manejo de intentos: Se define una constante max_intentos para establecer el límite en 3.
Se usa una variable intentos que se incrementa cada vez que el usuario comete un error, 
ya sea si no empieza con un numero o no coincidir las contraseñas.

Validación de la contraseña:

El bucle while se ejecuta mientras el número de intentos sea menor que el límite.

La primera validación if not contraseña1[0].isdigit(): comprueba si el primer caracter de la contraseña no es un dígito. 
Si no lo es, se informa al usuario, se incrementa el contador de intentos y se usa continue para saltar el resto del código del bucle y volver a pedir la contraseña.

Verificación de coincidencia:

Si la primera contraseña pasa la validación, el programa pide la segunda contraseña.

El código if contraseña1 == contraseña2: compara ambas contraseñas. 
Si son iguales, el programa imprime "Contraseña correcta" y "Fin del programa", y se usa break para salir del bucle.

Si no coinciden, se informa al usuario, se incrementa el contador de intentos, y el bucle continúa para el próximo intento.

Cierre del programa: Dentro de ambos bloques if de error, se verifica si el número de intentos ha llegado al máximo. 
Si es así, se imprime "Fin del programa" y se usa break para terminar el bucle, cumpliendo así con el requisito de cerrar el programa tras 3 errores.
#Ingreso un mensaje de bienvenida imprimiendolo
print("¡¡ Bienvenido comenzemos... ")
#Imprimo un mensaje sobre infrmacion de los datos a ingresar
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
