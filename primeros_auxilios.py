# Preguntas para evaluar si una persona necesita asistencia medica.
print("Hay Alguien Herido?")
print("Por favor, responde exactamente 'si' o 'no' a las preguntas para recibir instrucciones.")

respuesta = input("¿Responde a estímulos? (si/no): ")

if respuesta == "si":
    print("Evalua si existe la necesidad de llevarlo al hospital más cercano.")
else:
    print("Abrir la vía aérea.")
    respuesta = input("¿Respira? (si/no): ")
    if respuesta == "si":
        print("Permitirle posición de suficiente ventilación.")
    else:
        print("Administrar 5 ventilaciones y llamar a ambulancia.")
        respuesta = input("¿Hay signos de vida? (si/no): ")
        if respuesta == "si":
            respuesta = input("¿Llegó la ambulancia? (si/no): ")
            if respuesta == "si":
                print("Reevaluar a la espera de la ambulancia.")
            else:
                print("Reevaluar a la espera de la ambulancia.")
        else:
            print("Administrar compresiones torácicas hasta que llegue la ambulancia.")


#fin