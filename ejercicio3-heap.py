class HeapMax:

    def __init__(self):
        self.elements = []
    
    def add(self, value):
        self.elements.append(value)
        self.float(len(self.elements)-1)

    def remove(self):
        if len(self.elements) > 0:
            self.interchange(0, len(self.elements)-1)
            value = self.elements.pop()
            self.sink(0)
            return value
        else:
            return None

    def interchange(self, index_1, index_2):
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    # Nuevo metodo size para obtener el tamaño 
    def size(self):
        return len(self.elements)

    def float(self, index):
        father = (index-1) // 2
        # Cambio de la linea para comparar las prioridades de los elementos, accediendo a la primera posición del elemento (que es la prioridad)
        while index > 0 and self.elements[index][0] > self.elements[father][0]:  # Compara las prioridades
        # self.elements[index][0] accede a la prioridad del elemento en la posición index, y self.elements[father][0] accede a la prioridad del elemento en la posición father
            self.interchange(index, father)
            index = father
            father = (index-1) // 2

    def sink(self, index):
        left_child = (index * 2) + 1
        control = True
        while control and left_child < len(self.elements):
            right_child = (index * 2) + 2
            max = left_child
            if right_child < len(self.elements):
                if self.elements[right_child][0] > self.elements[left_child][0]:  # Compara las prioridades
                    max = right_child
            if self.elements[index][0] < self.elements[max][0]:  # Compara las prioridades
                self.interchange(index, max)
                index = max
                left_child = (index * 2) + 1
            else:
                control = False

    def arrive(self, value, priority):
        self.add([priority, value])

    def atention(self):
        return self.remove()

    def change_proirity(self, index, new_priority):
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority > previous_priority:
                self.float(index)
            elif new_priority < previous_priority:
                self.sink(index)


# Se crea la cola de prioridad
lista_operaciones = HeapMax()

# Cargar las actividades iniciales en la cola
operaciones_iniciales = [
    {"encargado": "Snoke", "descripcion": "Reunión estratégica", "hora": "10:00"},
    {"encargado": "Kylo Ren", "descripcion": "Entrenamiento de sable de luz", "hora": "11:00"},
    {"encargado": "Capitán Phasma", "descripcion": "Inspección de armamento", "hora": "12:00"},
    {"encargado": "Capitán Phasma", "descripcion": "Supervisión de entrenamiento", "hora": "13:00"},
    {"encargado": "General Hux", "descripcion": "Revisión de sistemas de defensa", "hora": "14:00"},
    {"encargado": "General Hux", "descripcion": "Evaluación de seguridad", "hora": "15:00"},
    {"encargado": "General Hux", "descripcion": "Revisión de suministros", "hora": "16:00"},
    {"encargado": "General Hux", "descripcion": "Informe de situación", "hora": "17:00"}
]

# Definir las prioridades de cada encargado
prioridades = {
    "Snoke": 3,
    "Kylo Ren": 3,
    "Capitán Phasma": 2,
    "General Hux": 1
}

# Agregar operaciones iniciales a la cola con sus prioridades
for operation in operaciones_iniciales:
    encargado = operation["encargado"] # encargado toma el nombre del encargado  de la mision
    # El 1 en prioridades.get(encargado, 1) asegura que cualquier encargado que no esté en el diccionario prioridades reciba una prioridad de nivel 1, evitando errores y garantizando que todas las operaciones tengan un nivel de prioridad asignado
    priority = prioridades.get(encargado, 1)  # Asigna la prioridad correspondiente, si el general no esta se asigna prioridad 1
    lista_operaciones.arrive(operation, priority) # llega a la lista_operaciones la operacion y su prioridad

# Función para atender y gestionar operaciones adicionales
def process_operations(queue):
    count = 0 # contador para luego de 5 agregar la operacion de Capitan Phasma, y 6 para Snoke
    while queue.size() > 0:
        count += 1
        # Atender la operación de mayor prioridad
        operation = queue.atention()
        print(f"Atendiendo operación: {operation}")

        # Después de la quinta operación, agregar operación de Capitan Phasma
        if count == 5:
            new_operation = {
                "encargado": "Capitán Phasma",
                "descripcion": "Revisión de intrusos en el hangar B7",
                "hora": "18:00",
                "stormtroopers": 25
            }
            # Llega a arrive la nueva operacion y la prioridad con la clave[Capitan Phasma]
            queue.arrive(new_operation, prioridades["Capitán Phasma"]) 
            print("Agregada operación de Capitán Phasma.")

        # Después de la sexta operación, agregar operación de Snoke
        if count == 6:
            new_operation = {
                "encargado": "Snoke",
                "descripcion": "Destrucción del planeta Takodana",
                "hora": "19:00"
            }
            queue.arrive(new_operation, prioridades["Snoke"])
            print("Agregada operación de Snoke.")

# Procesar las operaciones

process_operations(lista_operaciones)
