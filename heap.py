from typing import Any  # Importa el tipo genérico Any para usar en anotaciones de tipo


class HeapMax:  # Define una clase para un montículo máximo (heap máximo)

    def __init__(self):  # Método constructor de la clase
        self.elements = []  # Inicializa la lista interna que almacenará los elementos del heap

    def size(self) -> int:  # Devuelve la cantidad de elementos en el heap
        return len(self.elements)  # Retorna la longitud de la lista interna

    def add(self, value: Any) -> None:  # Agrega un nuevo valor al heap
        self.elements.append(value)  # Inserta el valor al final de la lista
        self.float(self.size() - 1)  # Llama a float para reubicar el valor respetando la propiedad de heap

    def remove(self) -> Any:  # Elimina y devuelve el valor máximo del heap
        last = self.size() - 1  # Calcula el índice del último elemento
        self.interchange(0, last)  # Intercambia la raíz (máximo) con el último elemento
        value = self.elements.pop()  # Extrae el último elemento, que era el máximo
        self.sink(0)  # Reorganiza el heap hundiendo el nuevo valor en la raíz
        return value  # Devuelve el valor eliminado

    def float(self, index: int) -> None:  # Sube un elemento hacia arriba en el heap para mantener el orden
        father = (index - 1) // 2  # Calcula el índice del padre del nodo actual
        while index > 0 and self.elements[index] > self.elements[father]:  # Mientras no sea la raíz y el hijo sea mayor que el padre
            # print(f'flotar desde {index} a {father}')  # Línea de depuración comentada
            self.interchange(index, father)  # Intercambia el elemento actual con su padre
            index = father  # Actualiza el índice actual al índice del padre
            father = (index - 1) // 2  # Recalcula el índice del nuevo padre

    def sink(self, index: int) -> None:  # Hundir un elemento hacia abajo en el heap para mantener el orden
        left_son = (2 * index) + 1  # Calcula el índice del hijo izquierdo
        control = True  # Bandera para controlar el bucle
        while control and left_son < self.size():  # Mientras haya hijo izquierdo dentro del heap
            right_son = left_son + 1  # Calcula el índice del hijo derecho

            mayor = left_son  # Supone inicialmente que el hijo mayor es el izquierdo
            if right_son < self.size():  # Verifica que el hijo derecho exista
                if self.elements[right_son] > self.elements[mayor]:  # Compara hijo derecho con el supuesto mayor
                    mayor = right_son  # Actualiza el índice del mayor al del hijo derecho

            if self.elements[index] < self.elements[mayor]:  # Si el valor actual es menor que el mayor de sus hijos
                # print(f'hundir desde {index} a {mayor}')  # Línea de depuración comentada
                self.interchange(index, mayor)  # Intercambia el nodo actual con el mayor de sus hijos
                index = mayor  # Actualiza el índice al nuevo lugar del elemento
                left_son = (2 * index) + 1  # Recalcula el índice del nuevo hijo izquierdo
            else:  # Si el elemento ya está en la posición correcta
                control = False  # Sale del bucle

    def interchange(self, index_1: int, index_2: int) -> None:  # Intercambia dos elementos del heap dados sus índices
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]  # Intercambia los valores en la lista

    def heapsort(self) -> list:  # Ordena los elementos del heap y devuelve una lista
        result = []  # Crea una lista vacía donde se almacenará el resultado ordenado
        while self.size() > 0:  # Mientras haya elementos en el heap
            result.append(self.remove())  # Extrae el máximo y lo agrega al resultado
        return result  # Devuelve la lista ordenada de mayor a menor

    def arrive(self, value: Any, priority: int) -> None:  # Inserta un valor con prioridad simulando una cola de prioridad
        # priority 1-low, 2-medium, 3-high  # Comentario que indica el significado de las prioridades
        self.add([priority, value])  # Agrega una lista con prioridad y valor al heap

    def attention(self) -> Any:  # Atiende el elemento de mayor prioridad del heap
        value = self.remove()  # Elimina el elemento máximo del heap
        return value  # Devuelve el valor eliminado


class HeapMin:  # Define una clase para un montículo mínimo (heap mínimo)

    def __init__(self):  # Constructor de la clase
        self.elements = []  # Inicializa la lista interna que almacenará los elementos del heap

    def size(self) -> int:  # Devuelve la cantidad de elementos en el heap
        return len(self.elements)  # Retorna el número de elementos en la lista interna

    def add(self, value: Any) -> None:  # Agrega un nuevo valor al heap mínimo
        self.elements.append(value)  # Inserta el valor al final de la lista
        self.float(self.size() - 1)  # Reubica el valor hacia arriba para mantener la propiedad de heap mínimo

    def search(self, value):  # Busca un elemento en el heap usando el primer campo del valor almacenado
        for index, element in enumerate(self.elements):  # Recorre todos los elementos del heap
            if element[1][0] == value:  # Compara el primer caracter del identificador almacenado con el valor buscado
                return index  # Devuelve el índice donde se encontró el valor

    def remove(self) -> Any:  # Elimina y devuelve el valor mínimo del heap
        last = self.size() - 1  # Calcula el índice del último elemento
        self.interchange(0, last)  # Intercambia la raíz (mínimo) con el último elemento
        value = self.elements.pop()  # Extrae el último elemento que era el mínimo
        self.sink(0)  # Reorganiza el heap hundiendo el nuevo valor de la raíz
        return value  # Devuelve el valor eliminado

    def float(self, index: int) -> None:  # Sube un elemento hacia arriba en el heap mínimo
        father = (index - 1) // 2  # Calcula el índice del padre del nodo actual
        while index > 0 and self.elements[index] < self.elements[father]:  # Mientras no sea la raíz y el hijo sea menor que el padre
            self.interchange(index, father)  # Intercambia el valor con su padre
            index = father  # Actualiza el índice al del padre
            father = (index - 1) // 2  # Recalcula el índice del nuevo padre

    def sink(self, index: int) -> None:  # Hundir un elemento hacia abajo en el heap mínimo
        left_son = (2 * index) + 1  # Calcula el índice del hijo izquierdo
        control = True  # Bandera para controlar el bucle
        while control and left_son < self.size():  # Mientras haya hijo izquierdo dentro del heap
            right_son = left_son + 1  # Calcula el índice del hijo derecho

            minor = left_son  # Supone inicialmente que el menor es el hijo izquierdo
            if right_son < self.size():  # Comprueba si existe hijo derecho
                if self.elements[right_son] < self.elements[minor]:  # Compara los dos hijos para encontrar el menor
                    minor = right_son  # Actualiza el índice del menor al del hijo derecho

            if self.elements[index] > self.elements[minor]:  # Si el valor actual es mayor que el menor de sus hijos
                self.interchange(index, minor)  # Intercambia el valor con el hijo menor
                index = minor  # Actualiza el índice del elemento hundido
                left_son = (2 * index) + 1  # Recalcula el hijo izquierdo para seguir hundiendo
            else:  # Si el elemento ya está colocado correctamente
                control = False  # Sale del bucle

    def interchange(self, index_1: int, index_2: int) -> None:  # Intercambia dos elementos del heap por índice
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]  # Intercambia los valores en la lista

    # def monticulizar  # Comentario de referencia para una posible función de monticulización

    def heapsort(self) -> list:  # Ordena los elementos del heap y devuelve una lista
        result = []  # Crea una lista vacía donde se guardará el resultado ordenado
        while self.size() > 0:  # Mientras haya elementos en el heap
            result.append(self.remove())  # Elimina el mínimo y lo agrega al resultado
        return result  # Devuelve la lista ordenada de menor a mayor

    def arrive(self, value: Any, priority: int) -> None:  # Inserta un valor con prioridad simulando una cola de prioridad mínima
        # priority 1-low, 2-medium, 3-high  # Explica las prioridades
        self.add([priority, value])  # Agrega una lista con prioridad y valor al heap

    def attention(self) -> Any:  # Atiende el elemento con menor prioridad numérica (más importante en un min-heap)
        value = self.remove()  # Elimina el elemento mínimo del heap
        return value  # Devuelve el valor eliminado

    def change_priority(self, index, new_priority):  # Cambia la prioridad de un elemento dentro del heap
        if index < len(self.elements):  # Verifica que el índice sea válido
            previous_priority = self.elements[index][0]  # Guarda la prioridad anterior del elemento
            self.elements[index][0] = new_priority  # Actualiza la prioridad al nuevo valor
            if new_priority > previous_priority:  # Si la nueva prioridad numérica es mayor (menos prioridad en un min-heap)
                self.sink(index)  # Hundimos el elemento porque su prioridad empeoró
            elif new_priority < previous_priority:  # Si la nueva prioridad numérica es menor (más prioridad)
                self.float(index)  # Flotamos el elemento porque su prioridad mejoró


# priority_queue = HeapMin()  # Ejemplo comentado de creación de una cola de prioridad basada en HeapMin

# priority_queue.arrive('x', 1)  # Inserta un elemento con prioridad 1
# priority_queue.arrive('b', 2)  # Inserta un elemento con prioridad 2
# priority_queue.arrive('a', 2)  # Inserta otro elemento con prioridad 2
# priority_queue.arrive('f', 1)  # Inserta un elemento con prioridad 1
# priority_queue.arrive('y', 1)  # Inserta un elemento con prioridad 1
# priority_queue.arrive('j', 2)  # Inserta un elemento con prioridad 2
# priority_queue.arrive('z', 3)  # Inserta un elemento con prioridad 3
# print(priority_queue.elements)  # Muestra el contenido interno del heap

# while priority_queue.size() > 0:  # Mientras haya elementos en la cola de prioridad
#     print(priority_queue.attention())  # Atiende (extrae) en orden de prioridad mínima

# h = HeapMin()  # Crea un heap mínimo de ejemplo
# h.add(19)  # Agrega el número 19
# h.add(5)   # Agrega el número 5
# h.add(1)   # Agrega el número 1
# h.add(3)   # Agrega el número 3
# h.add(9)   # Agrega el número 9


# list_sort = h.heapsort()  # Ordena los elementos del heap y guarda el resultado en una lista

# print(list_sort)  # Imprime la lista ordenada
# print(h.elements)  # Imprime el contenido del heap (debería quedar vacío tras el heapsort)

