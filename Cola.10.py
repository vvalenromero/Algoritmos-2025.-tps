from cola import Queue  # Importa la clase Queue definida en el módulo cola
from stack import Stack  # Importa la clase Stack definida en el módulo stack

cola_notificaciones = Queue()  # Crea una cola vacía para almacenar notificaciones
cola_notificaciones.arrive(("11:30", "Facebook", "Nuevo mensaje de Juan"))  # Encola una notificación de Facebook con hora y mensaje
cola_notificaciones.arrive(("12:15", "Twitter", "Aprendiendo Python es genial"))  # Encola una notificación de Twitter sobre aprender Python
cola_notificaciones.arrive(("14:00", "Instagram", "Nueva foto subida"))  # Encola una notificación de Instagram sobre una nueva foto
cola_notificaciones.arrive(("15:30", "Twitter", "Python en producción"))  # Encola una notificación de Twitter mencionando Python en producción
cola_notificaciones.arrive(("16:00", "Facebook", "Has sido etiquetado en una foto"))  # Encola otra notificación de Facebook sobre una etiqueta
cola_notificaciones.arrive(("10:00", "Twitter", "Hola mundo"))  # Encola una notificación de Twitter con mensaje 'Hola mundo'
cola_notificaciones.arrive(("13:45", "Facebook", "Evento hoy a las 18"))  # Encola una notificación de Facebook sobre un evento
cola_notificaciones.arrive(("11:50", "Twitter", "Curso de Python gratuito"))  # Encola una notificación de Twitter sobre un curso de Python


def eliminar_facebook(q: Queue):  # Define una función que elimina todas las notificaciones de Facebook de la cola
    n = q.size()  # Obtiene la cantidad actual de elementos en la cola
    i = 0  # Inicializa un contador
    while i < n:  # Recorre exactamente n elementos de la cola
        notif = q.attention()  # Atiende (desencola) la primera notificación
        if notif[1] != "Facebook":  # Si la red social de la notificación no es Facebook
            q.arrive(notif)  # Vuelve a encolarla al final de la cola
        i += 1  # Incrementa el contador


def mostrar_twitter_python(q: Queue):  # Define una función que obtiene notificaciones de Twitter que mencionen 'Python'
    resultados = []  # Lista donde se guardarán las notificaciones que cumplan la condición
    n = q.size()  # Obtiene la cantidad de notificaciones en la cola
    i = 0  # Inicializa el contador del bucle
    while i < n:  # Recorre todas las notificaciones existentes
        notif = q.attention()  # Desencola la siguiente notificación
        if notif[1] == "Twitter" and "Python" in notif[2]:  # Verifica si es de Twitter y su mensaje contiene la palabra 'Python'
            resultados.append(notif)  # Agrega la notificación a la lista de resultados
        q.arrive(notif)  # Vuelve a encolar la notificación para no perderla
        i += 1  # Incrementa el contador
    return resultados  # Devuelve la lista de notificaciones que cumplen la condición


def notificaciones_pila_intervalo(q: Queue, inicio: str = "11:43", fin: str = "15:57") -> int:  # Define una función que cuenta notificaciones en un rango horario usando una pila
    pila = Stack()  # Crea una pila vacía para almacenar notificaciones dentro del intervalo
    n = q.size()  # Obtiene la cantidad de notificaciones en la cola
    i = 0  # Inicializa el contador
    while i < n:  # Recorre todas las notificaciones de la cola
        notif = q.attention()  # Desencola la siguiente notificación
        hora = notif[0]  # Extrae la hora de la notificación
        if inicio <= hora <= fin:  # Verifica si la hora está dentro del intervalo dado
            pila.push(notif)  # Apila la notificación en la pila
        q.arrive(notif)  # Vuelve a encolar la notificación para mantener la cola intacta
        i += 1  # Incrementa el contador
    return pila.size()  # Devuelve la cantidad de elementos en la pila (notificaciones dentro del intervalo)


print("Antes de eliminar Facebook:")  # Muestra un título antes de eliminar notificaciones de Facebook
cola_notificaciones.show()  # Muestra el contenido actual de la cola de notificaciones

eliminar_facebook(cola_notificaciones)  # Llama a la función para eliminar todas las notificaciones de Facebook

print("\nDespués de eliminar Facebook:")  # Muestra un título después de realizar la eliminación
cola_notificaciones.show()  # Muestra la cola resultante sin notificaciones de Facebook

print("\nNotificaciones de Twitter con 'Python':")  # Título para la sección de filtrado de notificaciones de Twitter con 'Python'
for t in mostrar_twitter_python(cola_notificaciones):  # Recorre todas las notificaciones de Twitter que mencionan 'Python'
    print(t)  # Imprime cada notificación que cumple la condición

cantidad = notificaciones_pila_intervalo(cola_notificaciones)  # Llama a la función que cuenta notificaciones en el intervalo y guarda el resultado
print(f"\nCantidad de notificaciones entre 11:43 y 15:57 almacenadas en pila: {cantidad}")  # Imprime la cantidad obtenida