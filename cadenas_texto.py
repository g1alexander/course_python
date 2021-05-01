'''

  Twitter: @g1_alexander

'''
#Teoria: cadenas de texto

#declarar
texto = "soy un texto"
texto = 'soy un texto'
texto = """soy un texto"""
texto = '''soy un texto'''

# resaltar o combinar comillas
print("hol'a'")
print('hol"a"')

# formateo

nombre = "alexander"
apellido = "granados"
edad = 21

print("Hola, mi nombre es: {0} {1} {2}".format(nombre, apellido, edad))
print(f"Hola, mi nombre es: {nombre} {apellido}, y tengo {edad} anios")

#contatenar
nombre_completo1 = nombre + " " + apellido
nombre_completo2 = f"{nombre} {apellido}"

print("primero", nombre_completo1)
print("segundo", nombre_completo2)

#slicing
palabra = "hola"
print("letra: ", palabra[0]) #h
print("letra: ", palabra[1]) #o
print("letra: ", palabra[2]) #l
print("letra: ", palabra[3]) #a


print("negativo: ", palabra[-1]) #a
print("negativo: ", palabra[-2]) #l
print("negativo: ", palabra[-3]) #o
print("negativo: ", palabra[-4]) #h

print("todos", palabra[:])
print("negativo", palabra[::-1])

#metodos
palabra = "chauu"
palabra = palabra.replace("c", "g")
print(palabra)
print(palabra.capitalize())
print(palabra.find("h"))
print(palabra.upper())

#metodo split
palabra = "hola soy un texto"
print(palabra.split())
