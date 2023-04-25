num1="120"
num2="150"



num3=105
sueldo=1035.78
texto= "Curso de Python"

print(num1)
print(num2)
print(num3)
print(sueldo)
print(texto)

# Int() convertir datos a entero
# Float, convertir datos a Float
# str convierte un dato x un dato tipo cadena
# hex, Convierte x entero en una cadena Hexadecimal

print(num1+num2)
#convertir de dato tipo cadena a numeros enteros
print(int(num1)+int(num2))

#convertir u obtener el dato entero de la variable float
print(int(sueldo))

#al aplicar una , para querer concatenar variables, la coma lo que hace es realiza la impresión del primer contenido y
#lo acompaña con el siguiente contenido
#si queremos hacer una concatenación entre tipos de datos diferentes tenemos que alinear los datos al mismo nivel
print("Sueldo mensual es : " + str(sueldo))

#de entero a float
print(float(num3))

#de dato entero a hexa
print(hex(num3))