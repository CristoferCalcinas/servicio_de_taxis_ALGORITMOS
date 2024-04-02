class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None  # Referencia al primer elemento de la cola
        self.rear = None  # Referencia al último elemento de la cola

    def is_empty(self):
        # Verifica si la cola está vacía
        return self.front is None

    def enqueue(self, data):
        # Agrega un elemento al final de la cola (encolar)
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        # Elimina y devuelve el elemento al frente de la cola (desencolar)
        if self.is_empty():
            return None
        popped = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return popped

    def peek(self):
        # Devuelve el elemento al frente de la cola sin eliminarlo
        if self.is_empty():
            return None
        return self.front.data

    def display(self):
        # Muestra los elementos de la cola
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def find(self, target):
        # Recorre la cola para encontrar el elemento target
        current = self.front
        while current:
            if current.data == target:
                return True  # Elemento encontrado
            current = current.next
        return False  # Elemento no encontrado

    def find_position(self, target):
        # Encuentra la posición del elemento en la cola
        current = self.front
        index = 0
        while current:
            if current.data == target:
                return index  # Devuelve la posición del elemento
            current = current.next
            index += 1
        return -1  # Devuelve -1 si el elemento no se encuentra

    def remove_at_position(self, position):
        if self.is_empty() or position < 0:
            return None  # No se puede eliminar si la cola está vacía o la posición es inválida

        if position == 0:
            return (
                self.dequeue()
            )  # Si la posición es 0, simplemente desencola el primer elemento

        current = self.front
        prev = None
        index = 0
        while current and index != position:
            prev = current
            current = current.next
            index += 1

        if not current:
            return None  # La posición está más allá del final de la cola

        # Elimina el nodo actual
        prev.next = current.next

        # Si el nodo a eliminar es el último, actualiza la referencia al último nodo
        if current == self.rear:
            self.rear = prev

        # Devuelve el dato del nodo eliminado
        popped_data = current.data
        return popped_data
