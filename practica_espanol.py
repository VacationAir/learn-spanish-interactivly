import random
#Poner el artículo correcto
puntuacion_pos = 0 #Puntuación positiva, aciertos
puntuacion_neg = 0 #Puntuación negativa, fallos
a = "libro"
b = "manzana"
c = "caramelo"
d = "hipopótamo"
e = "perro"
f = "pizza"
g = "sartén"
list_palabras = [a, b, c, d, e, f, g]
a = "el"
b = "la"
c = "el"
d = "el"
e = "el"
f = "la"
g = "la"
list_art = [a, b, c, d, e, f, g]
for i in range(len(list_palabras)):
	index = random.randint(0, len(list_palabras) - 1)
	palabra = list_palabras[index]
	articulo_correcto = list_art[index]
	print(f"Cual es el artículo correcto de {palabra}")
	user_input = input("")
	if user_input == articulo_correcto:
		print("Muy bien!")
		puntuacion_pos = puntuacion_pos + 1
	else:
		print("-999 Aura")
print(f"Tu puntuación es {puntuacion_pos} de {len(list_palabras)}, o {round((puntuacion_pos)/(len(list_palabras))*100, 2)}") 
