from typing import Any, Optional  # Importa tipos genéricos y opcionales para anotaciones de tipo


class Queue:  # Define una clase Queue que implementa una cola básica

    def __init__(self):  # Constructor de la clase
        self.__elements = []  # Inicializa una lista privada donde se guardan los elementos de la cola

    def arrive(self, value: Any) -> None:  # Agrega (encola) un valor al final de la cola
        self.__elements.append(value)  # Inserta el valor recibido al final de la lista interna

    def attention(self) -> Optional[Any]:  # Atiende (desencola) el primer elemento de la cola
        return (  # Devuelve el elemento atendido o None si la cola está vacía
            self.__elements.pop(0)  # Elimina y retorna el primer elemento de la lista
            if self.__elements  # Solo si la lista tiene elementos
            else None  # Si está vacía, retorna None
        )

    def size(self) -> int:  # Devuelve la cantidad de elementos en la cola
        return len(self.__elements)  # Retorna la longitud de la lista interna
    
    def on_front(self) -> Optional[Any]:  # Devuelve el elemento del frente sin eliminarlo
        return (  # Devuelve el primer elemento o None si la cola está vacía
            self.__elements[0]  # Accede al primer elemento de la lista
            if self.__elements  # Solo si la lista tiene al menos un elemento
            else None  # Si la lista está vacía, devuelve None
        )

    def move_to_end(self) -> Optional[Any]:  # Mueve el elemento del frente al final de la cola
        if self.__elements:  # Verifica si hay elementos en la cola
            value = self.attention()  # Atiende (saca) el primer elemento
            self.arrive(value)  # Vuelve a encolarlo al final de la cola
            return value  # Devuelve el valor que fue movido
    
    def show(self):  # Muestra todos los elementos de la cola sin perderlos
        for i in range(len(self.__elements)):  # Recorre tantos elementos como hay en la cola
            print(self.move_to_end())  # Mueve el elemento del frente al final y lo imprime
        
