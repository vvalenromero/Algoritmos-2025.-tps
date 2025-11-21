from typing import Any, Optional  # Importa tipos genéricos y opcionales para anotaciones


class Queue:  # Define una clase Queue que implementa una cola sencilla

    def __init__(self):  # Constructor de la clase
        self.__elements = []  # Lista privada que almacena los elementos de la cola

    def arrive(self, value: Any) -> None:  # Encola un nuevo elemento al final de la cola
        self.__elements.append(value)  # Agrega el valor recibido al final de la lista interna

    def attention(self) -> Optional[Any]:  # Atiende (desencola) el primer elemento de la cola
        return (  # Devuelve el elemento atendido o None si la cola está vacía
            self.__elements.pop(0)  # Elimina y devuelve el primer elemento de la lista
            if self.__elements  # Si la lista no está vacía
            else None   # Si está vacía, devuelve None
        )

    def size(self) -> int:  # Devuelve la cantidad de elementos en la cola
        return len(self.__elements)  # Retorna la longitud de la lista interna
    
    def on_front(self) -> Optional[Any]:  # Devuelve el elemento que está al frente de la cola sin desencolarlo
        return (  # Devuelve el primer elemento o None si no hay elementos
            self.__elements[0]  # Accede al primer elemento de la lista
            if self.__elements  # Solo si la lista no está vacía
            else None  # Si está vacía, devuelve None
        )

    def move_to_end(self) -> Optional[Any]:  # Mueve el elemento del frente al final de la cola
        if self.__elements:  # Verifica si hay elementos en la cola
            value = self.attention()  # Atiende (saca) el elemento del frente
            self.arrive(value)  # Lo vuelve a encolar al final
            return value  # Devuelve el valor que fue movido
    
    def show(self):  # Muestra todos los elementos de la cola en orden, rotando la cola
        for i in range(len(self.__elements)):  # Recorre la cantidad total de elementos
            print(self.move_to_end())  # Mueve el elemento del frente al final y lo imprime
