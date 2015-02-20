__author__ = 'Ramon'

x = 3
print("Meti", x, "Goles")

# TODO learn python
y = 0xA
z = 0b1100  # esto esta en binario. Hay que separar los comentarios 2 espacios despues del final de la linea
print(y, z)
print(y ** x)  # exponencial, donde y es la base y x el exponente

string2 = """varias
lineas"""
print(string2)

#creando un arreglo de constantes
const_array = ('cadena de texto', 15, 2.8, 'otro dato', 25)
print(const_array[1])  # Salida: 15
print(const_array[0:5])  # Salida: el arreglo
print(const_array[3:])  # Devuelve: ('otro dato', 25)
print(const_array[:2])  # Devuelve: ('cadena de texto', 15)
print(const_array[-1])  # Salida: 25

#creando una lista
mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]
mi_lista[1] += 5
print(mi_lista[1])
w = 3.8
mi_lista.append(w)
print(mi_lista[0:6])

#creando un diccionario, que permite asignar clave: valor
mi_diccionario = {'clave_1': 1, 'clave_2': 2, 'clave_3': 3}
print(mi_diccionario['clave_2'])  # Salida: valor_2
del mi_diccionario['clave_2']
mi_diccionario['clave_1'] = 5
print(mi_diccionario['clave_1'])

#asignacion multiple
a, b, c = 'string', 15, True
print(a, b, c)

mi_lista2 = ['Argentina', 'Buenos Aires']
pais, ciudad = mi_lista2
print(pais, ciudad)

#if
# compra = int(input("Precio del objeto: "))  #funcion para leer un int
compra = 10
if compra <= 100:
    print("Pago en efectivo")
elif compra > 100 and compra < 300:
    print("Pago con tarjeta de débito")
else:
    print("Pago con tarjeta de crédito")

#while
anno = 2010
while anno < 2015:
    print(anno)
    anno += 1

#for
for cadena in mi_lista:
    print(cadena)

for anno in range(2001, 2013):
    print("Informes del Año", str(anno))


#funciones
def mi_funcion(nombre="Fl@sh", apellido="Gordon"):
    nombre_completo = nombre, apellido
    return nombre_completo


variable = mi_funcion()
print("Nombre Completo:",variable[0],variable[1])

variable = mi_funcion(apellido="Fula",nombre="Superman")
print("Nombre Completo 2:",variable[0],variable[1])

variable = ["Batman","Locote en licra"]
variable2 = mi_funcion(*variable)  #se pasa un arreglo como argumento, pero la funcion recibe argumentos individuales
print("Nombre Completo 3:",variable2[0],variable2[1])

variable = {"apellido":"That dude is just gay","nombre":"Aquaman"}
variable2 = mi_funcion(**variable)
print("Nombre Completo 4:",variable2[0],variable2[1])


def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios, **kwords):
    print(parametro_fijo)
    for argumento in arbitrarios:
        print(argumento)
    # Los argumentos arbitrarios tipo clave, se recorren como los diccionarios
    for clave in kwords:
        print("El valor de", clave, "es", kwords[clave])


recorrer_parametros_arbitrarios("Fixed", "arbitrario 1", "arbitrario 2","arbitrario 3", clave1="valor uno",clave2="valor dos")


#recursive function
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print("fibonacci=", fibonacci(20))


#Merge Algorithm
def cortar_arreglo(array):
    i = 0
    a = []
    b = []
    for num in array:
        if i < len(array)/2:
            a.append(array[i])
        else:
            b.append(array[i])
        i += 1
    return a, b

array = [5, 4, 1, 8, 7, 2, 6, 3]
A, B = cortar_arreglo(array)
#las funciones sort las debo implementar recursivamente
A.sort()
B.sort()
print("A=", A, " y B=", B)

C = []
n = 8
k, i, j = 1, 0, 0  # para desplazarse por los arreglos

while k <= n:
    if i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        elif A[i] > B[j]:
            C.append(B[j])
            j += 1
    else:
        if i > j:
            C.append(B[j])
        else:
            C.append(A[i])
    k += 1

for numero in C:
    print(numero)

lines = list(open('IntegerArray.txt', 'r'))
#print(lines)

var_array = []

with open("IntegerArray.txt", "r") as my_file:
    for line in my_file:
        var_array.append(int(line.strip()))
        #var_array += map(int, line.strip().split())

print(var_array)
