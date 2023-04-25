Nombre = "Sebastian"
Apellido="Oteiza"
Especialidad="Pesimista"

print(Nombre + Apellido)
#Pequeño alias en la cadena de texto con el %s, el contenido de la variable se inserta dentro de la primera cadena
print("Mi nombre es:  %s" %Nombre)

#concatenar dos contenidos de variable
print("Mi nombre es : %s y Mi apellido es %s: " %(Nombre, Apellido))

#Tercera forma de concatenar, se crea una especie de indice, parte en el 0 para ir adjudicando valores
print("Mi nombre es: {0} y mi especialidad es: {1}".format(Nombre, Especialidad))

#4ta forma de concatenación
print("Mi nombre es: {a} y mi apellido es: {b}".format(a=Nombre, b=Apellido))