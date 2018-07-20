# Función que recibe dos parámetros y devuelve el resultado de elevarlos entre si.
def operator(num1, num2):
	result = num1**num2
	return result

value = operator(2, 3) # Variable que almacena el resulta de elevar 2 a la 3 (2^3).
print(value) # Imprime el valor.

myList = [5, 4, "Bryan", 3.1416] # Se crea una lista con distintos elementos.
print(myList) # Imprime la lista.
print(myList[1:3]) # Imprime los elementos de la lista desde la posición 1 hasta la 2 sin incluir al 3 [1, 3). 
myList.append("Alejo") # Agrega un elemento en la última posición de la lista. 
print(myList) # Imprime la lista.
myList.insert(0, "Biojo") # Inserta un elemento en la lista en la posición indicada.
print(myList) # Imprime la lista.
myList.extend(["lalaland", 2.718281, "lel"]) # Agrega varios elementos a la lista desde la posición final.
print(myList) # Imprime la lista.
print(myList.index("Bryan")) # Devuelve la posición donde se encuentra el elemento indicado.
# Imprime true o false si el elemento se encuentra en la lista.
print("Bryan" in myList) 
print("Bryan2" in myList)
myList.remove("lalaland") # Elimina el elemento indicado de la lista.
print(myList) # Imprime la lista.
myList.pop() # Elimina el último elemento de una lista.
print(myList) # Imprime la lista.

# Creación de nuevas listas:

myList1 = [5, 4, "Bryan"]
myList2 = ["Biojó", "Alejo"]
myList3 = [1, 2, 3]

myList4 = myList1 + myList2 + myList3 # Une (concatena) dos o más listas.
print(myList4) # Imprime la lista.
myList5 = [5, 4, "Bryan"] * 3 # Repetidor de lista: Repite las listas las veces que se indique.
print(myList5) # Imprime la lista.
myList1.reverse()
print(myList1) # Imprime la lista.

# Creación de una tupla.

nTupla = (1, "papu", 7, 7, 2018)
print(nTupla) # Imprime la tupla.
nList = list(nTupla) # Pasar de una tupla a una lista.
print(nList) # Imprime la tupla convertida en lista.
nTupla1 = tuple(nList) # Pasar de una lista a una tupla
print(nTupla1) # Imprime la tupla
print(nTupla1.count(7)) # Contar cuantas veces se encuentra un elemento en una tupla.
print(len(nTupla1)) # Imprime el número de elementos que hay en una tupla.
nTupla2 = ("unit",) # Tupla unitaria.
print(len(nTupla2)) # Imprime la tupla unitaria.

# Desempaquetado de tupla

tuplaPrueba = ("Bryan Biojo", 19, 8, 1997)
nombre, dia, mes, anio = tuplaPrueba # Asigna cada uno de los elementos de la tupla a las variables.
# Imprime los valores de las variables.
print(nombre)
print(dia)
print(mes)
print(anio)
#ls2