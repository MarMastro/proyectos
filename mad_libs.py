#Concatenar cadenas de caracteres
#Supongamos que queremos crear una cadena que diga:
#Aprende a programar con_______.

organizacion = "freeCodeCamp"

#print ("Aprende a programar con " + organizacion) 
#print ("Aprende a programar con {}".format(organizacion))
#print(f"Aprende a programar con {organizacion} ")

adj = input("Ingresá un adjetivo: ")
verbo1 = input("Ingresá un verbo: ")
verbo2 = input("Ingresá otro verbo: ")
sustantivo_plural = input("Ingresá un sustantivo en plural: ")

madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y \nalcanza tus {sustantivo_plural}"

print(madlib)
