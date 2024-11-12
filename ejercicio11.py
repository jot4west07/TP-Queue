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
                index = i # index toma el valor de i que es el indice actual del personaje
                break
        if index is not None:
            self.__elements.insert(index, nuevo_personaje)  # insertar nuevo_personaje en el indice

    def eliminar_despues_personaje(self, nombre_objetivo):
        # Elimina el personaje que está después de un personaje específico (por nombre)
        index = None
        for i, element in enumerate(self.__elements):
            if element["nombre"] == nombre_objetivo:
                index = i + 1 # +1 porque es el personaje que esta despues 
                break
        # Después de obtener el index, se debe verificar que ese índice sea válido. Es decir, que no esté fuera de los límites de la lista. Si el index es mayor o igual a la longitud de la lista (len(self.__elements)), significa que no hay un "personaje después" de ese índice, porque habrías llegado al final de la lista
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
# se usa characters_queue._Queue__elements para acceder a este atributo privado desde fuera de la clase

# Punto d
print("\nEliminar personaje después de Jar Jar Binks:")
characters_queue.eliminar_despues_personaje("Jar Jar Binks")
print([char["nombre"] for char in characters_queue._Queue__elements])  # Mostrar nombres en la cola

# [char["nombre"] for char in characters_queue._Queue__elements] crea una lista con solo los nombres de los personajes en la cola
# for char in characters_queue._Queue__elements: Este ciclo for recorre todos los personajes en la lista self.__elements de la cola, donde cada char es un diccionario que representa a un personaje.
# char["nombre"]: Para cada personaje (char), se obtiene el valor asociado a la clave "nombre"
# La expresión char["nombre"] extrae los valores de la clave "nombre" de cada uno de esos diccionarios, por lo que la list comprehension generará la lista:
# ["Luke Skywalker", "Leia Organa", "Han Solo"]
