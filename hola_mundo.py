"hola mundo"

print("hola mundo")
print("esto es una prueba")
print(10-1)

numero1 = 10
numero2 = 5
resultado = numero1 * numero2
print('El producto entre ' + str(numero1) + ' y ' + str(numero2) + ' da ' + str(resultado))
miNombre = "Facundo Ghisoni"
miNombre = 'Facundo'
miApellido = 'Ghisoni'
miEdad = 21

print('Mi nombre completo es ' + miNombre + " " + miApellido + " y tengo " + str(miEdad))
miNumeroFavorito = 10

print("Mi numero favorito es: " + str(miNumeroFavorito))

# def hola():
    # print("todo bien?")
    # return "quien sos"
# hola()
# print("hola " + hola())

#--------------------- tp3 ---------------------
# 1
# numeroEntero = -10

# print("El valor absoluto de num es: " + str(abs(numeroEntero)))
# 2
# miNombre = "Facundo"

# print("El nombre " + miNombre + " tiene " + str(len(miNombre)) + " letras")
# 3

# numero = 2
# exponente = 2

# print(str(numero**exponente))

# 4


# baseRectangulo = 3
# alturaRectangulo = 4

# def calcularPerimetro():
#     perimetro = 2*(baseRectangulo+alturaRectangulo)
#     return perimetro
# print(calcularPerimetro())

# 5

# base = 2
# altura = 3

# def calcularArea():
#     area=base*altura
#     return area 
# print(calcularArea())

# 6

# a=5
# b=10
# c=0

# def cambio(a,b,c):
#     c=b
#     b=a
#     a=c
#     return (a,b)

# print(cambio(a, b,c))

# 7

# a=3
# b=4

# a,b=b,a
# print(a,b)

# 8

# alumno = "pepe"
# nota1 = 8
# nota2 = 8

# def promedioNotas(unos,doss):
#     resultado2 = (unos+doss)/2
#     return resultado2

# print("el promedio de los parciales del alumno " + alumno + " es: " + str(promedioNotas(nota1, nota2)))

# 9

dolares = 100
reales = 200
pesos = 1000

def conversion(dolares,reales):
    dolares = (dolares*102.5)
    reales = (reales*104.5)
    contador = dolares + reales

    return  contador



print(conversion(dolares, reales)+pesos)
 


