'''

  Twitter: @g1_alexander

'''

#teoria: ciclo for (ciclo incondicional)
lista = [1,2,3,4,5,6]
tupla = (1,2,3,4)
diccionario = { 1:1 , 2:2 , 3:3 , 4:4 }
texto = "hola"
numero = str(123455)

#iterador
'''for i in lista:
    print(i)'''

#con rangos
'''for numero in range(1, 6, 2): #range(5) -> 0 ... 4 - range(1,5) -> 1 ...4 - range(1,6,2) -> 1,3,5
    print(numero)'''

#enumeracion
for enumerador, valor in enumerate(texto):
    print(f"""La posicion es {enumerador}
     y la letra es {valor}""")

# break 
for numero in range(30):
    if(numero == 25):
        break
    print(numero)

