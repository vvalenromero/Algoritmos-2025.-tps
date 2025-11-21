from typing import Any, Optional  # Importa tipos genéricos y opcionales para anotaciones de tipo


class Stack:  # Define una clase Stack que implementa una pila (LIFO)

    def __init__(self):  # Constructor de la clase
        self.__elements = []  # Inicializa una lista privada que almacenará los elementos de la pila

    def push(self, value: Any) -> None:  # Apila (agrega) un elemento en la parte superior de la pila
        self.__elements.append(value)  # Inserta el valor al final de la lista, que representa la cima de la pila

    def pop(self) -> Optional[Any]:  # Desapila (extrae) el elemento de la cima de la pila
        return (  # Devuelve el elemento extraído o None si la pila está vacía
            self.__elements.pop()  # Elimina y devuelve el último elemento de la lista
            if self.__elements  # Solo si la lista tiene elementos
            else None  # Si está vacía, devuelve None
        )

    def size(self) -> int:  # Devuelve la cantidad de elementos en la pila
        return len(self.__elements)  # Retorna la longitud de la lista interna

    def on_top(self) -> Optional[Any]:  # Devuelve el elemento que está en la cima sin extraerlo
        return (  # Devuelve el último elemento de la lista o None si está vacía
            self.__elements[-1]  # Accede al último elemento de la lista
            if self.__elements  # Solo si hay elementos en la pila
            else None  # Si la pila está vacía, devuelve None
        )

    def show(self):  # Muestra todos los elementos de la pila sin perderlos
        aux_stack = Stack()  # Crea una pila auxiliar para ayudar a mostrar sin modificar el contenido final
        while self.size() > 0:  # Mientras la pila original tenga elementos
            value = self.pop()  # Desapila el elemento de la cima
            print(value)  # Imprime el valor desapilado
            aux_stack.push(value)  # Lo apila en la pila auxiliar
        
        while aux_stack.size() > 0:  # Una vez mostrados, restaura los elementos a la pila original
            self.push(aux_stack.pop())  # Desapila de la auxiliar y vuelve a apilar en la pila original
