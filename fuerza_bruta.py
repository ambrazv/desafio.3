from string import ascii_lowercase

password = input("Ingrese la contraseña a adivinar (oculta): ") # Se solicita introducir al usuario la contraseña en consola

password = password.lower()  # Convertimos la contraseña a minúsculas

intentos = 0  # Inicializamos el contador de intentos

# Iteramos sobre cada carácter de la contraseña
for i, char in enumerate(password):
    # Iteramos sobre cada letra del abecedario en minúsculas
    for guess in ascii_lowercase:
        intentos += 1  # Incrementamos el contador de intentos
        if guess == char:  # Si la letra adivinada coincide con la letra de la contraseña
                break  # Salimos del bucle interno y pasamos a la siguiente letra de la contraseña
    
print(f"La contraseña se adivinó en {intentos} intentos.")  # Se imprime resultado en consola

