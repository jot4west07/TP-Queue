class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, element):
        self.__elements.append(element)

    def attention(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.__elements)

    def on_front(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None
    
    def move_to_end(self):
        element = self.attention()
        if element is not None:
            self.arrive(element)
    
    # Funciones 

    def obtener_personaje_por_superheroe(self, superheroe_nombre):
        # a. Determina el nombre del personaje del superhéroe dado
        for element in self.__elements:
            if element["superheroe"] == superheroe_nombre:
                return element["personaje"]
        return None

    def obtener_superheroes_femeninos(self):
        # b. Muestra los nombres de los superhéroes femeninos
        return [element["superheroe"] for element in self.__elements if element["genero"] == "F"]

    def obtener_personajes_masculinos(self):
        # c. Muestra los nombres de los personajes masculinos
        return [element["personaje"] for element in self.__elements if element["genero"] == "M"]

    def obtener_superheroe_por_personaje(self, nombre_personaje):
        # d. Determina el nombre del superhéroe del personaje dado
        for element in self.__elements:
            if element["personaje"] == nombre_personaje:
                return element["superheroe"]
        return None

    def comienza_con_s(self):
        # e. Muestra todos los datos de superhéroes o personajes cuyos nombres comienzan con 'S'
        return [element for element in self.__elements if element["personaje"].startswith("S") or element["superheroe"].startswith("S")]

    def existe_personaje(self, nombre_personaje):
        # f. Determina si un personaje específico se encuentra en la cola e indica su superhéroe
        encontrado = False
        for element in self.__elements:
            if element["personaje"] == nombre_personaje:
                encontrado = True
                print("El personaje si esta en la lista")
                print("Su nombre de supereroe es", element["superheroe"])
        if encontrado == False:
            print("El personaje no esta en la lista")

# Lista personajes marvel
personajes_marvel = Queue()

# Agregar personajes
personajes_marvel.arrive({"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"})
personajes_marvel.arrive({"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"})
personajes_marvel.arrive({"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"})
personajes_marvel.arrive({"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"})
personajes_marvel.arrive({"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"})

# a
print("a_ Nombre civil de Capitana Marvel:", personajes_marvel.obtener_personaje_por_superheroe("Capitana Marvel"))
print("")
# b
print("b_ Superhéroes femeninos:", personajes_marvel.obtener_superheroes_femeninos())
print("")
# c
print("c_ Personajes masculinos:", personajes_marvel.obtener_personajes_masculinos())
print("")
# d
print("d_ Superhéroe del personaje Scott Lang:", personajes_marvel.obtener_superheroe_por_personaje("Scott Lang"))
print("")
# e
print("e_ Datos de personajes o superhéroes que comienzan con 'S':", personajes_marvel.comienza_con_s())
print("")
# f
print("f_ Carol Danvers esta en la lista?")
personajes_marvel.existe_personaje("Carol Danvers")
print("")

