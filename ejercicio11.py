class Queue:
    # self.__elements contiene los elementos en characters_queue
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
    
    # Funciones para resolver el ejercicio

    def mostrar_personajes_de_planetas(self, planets):
        # Muestra personajes de los planetas especificados en 'planets'
        result = []
        for element in self.__elements:
            if element["planeta"] in planets:
                result.append(element)
        return result

    def obtener_planeta_natal(self, names):
        # Indica el planeta natal de los personajes con los nombres especificados en 'names'
        result = {}
        for element in self.__elements:
            if element["nombre"] in names:
                result[element["nombre"]] = element["planeta"]
        return result

    def insertar_antes_personaje(self, nuevo_personaje, nombre_objetivo):
        # Inserta un nuevo personaje antes de un personaje específico (por nombre)
        index = None
        for i, element in enumerate(self.__elements):
            if element["nombre"] == nombre_objetivo:
                index = i
                break
        if index is not None:
            self.__elements.insert(index, nuevo_personaje)

    def eliminar_despues_personaje(self, nombre_objetivo):
        # Elimina el personaje que está después de un personaje específico (por nombre)
        index = None
        for i, element in enumerate(self.__elements):
            if element["nombre"] == nombre_objetivo:
                index = i + 1
                break
        if index is not None and index < len(self.__elements):
            self.__elements.pop(index)

# Se Crea una cola e insertan personajes de prueba

characters_queue = Queue()

characters_queue.arrive({"nombre": "Luke Skywalker", "planeta": "Tatooine"})
characters_queue.arrive({"nombre": "Leia Organa", "planeta": "Alderaan"})
characters_queue.arrive({"nombre": "Han Solo", "planeta": "Corellia"})
characters_queue.arrive({"nombre": "Yoda", "planeta": "Dagobah"})
characters_queue.arrive({"nombre": "Jar Jar Binks", "planeta": "Naboo"})
characters_queue.arrive({"nombre": "Chewbacca", "planeta": "Kashyyyk"})

# Punto a
print("Personajes de Alderaan, Endor, y Tatooine:")
print(characters_queue.mostrar_personajes_de_planetas(["Alderaan", "Endor", "Tatooine"]))

# Punto b
print("\nPlaneta natal de Luke Skywalker y Han Solo:")
print(characters_queue.obtener_planeta_natal(["Luke Skywalker", "Han Solo"]))

# Punto c
print("\nInsertar un nuevo personaje antes de Yoda:")
print("Personaje insertado: Ahsoka Tano, planeta: Shili")
nuevo_personaje = {"nombre": "Ahsoka Tano", "planeta": "Shili"}
characters_queue.insertar_antes_personaje(nuevo_personaje, "Yoda")
print([char["nombre"] for char in characters_queue._Queue__elements])  # Mostrar nombres en la cola

# Punto d
print("\nEliminar personaje después de Jar Jar Binks:")
characters_queue.eliminar_despues_personaje("Jar Jar Binks")
print([char["nombre"] for char in characters_queue._Queue__elements])  # Mostrar nombres en la cola

# [char["name"] for char in characters_queue._Queue__elements] crea una lista con solo los nombres de los personajes en la cola
