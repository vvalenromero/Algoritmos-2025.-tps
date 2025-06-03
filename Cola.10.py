from cola import Queue
from stack import Stack

cola_notificaciones = Queue()
cola_notificaciones.arrive(("11:30", "Facebook", "Nuevo mensaje de Juan"))
cola_notificaciones.arrive(("12:15", "Twitter", "Aprendiendo Python es genial"))
cola_notificaciones.arrive(("14:00", "Instagram", "Nueva foto subida"))
cola_notificaciones.arrive(("15:30", "Twitter", "Python en producción"))
cola_notificaciones.arrive(("16:00", "Facebook", "Has sido etiquetado en una foto"))
cola_notificaciones.arrive(("10:00", "Twitter", "Hola mundo"))
cola_notificaciones.arrive(("13:45", "Facebook", "Evento hoy a las 18"))
cola_notificaciones.arrive(("11:50", "Twitter", "Curso de Python gratuito"))

def eliminar_facebook(q: Queue):
    n = q.size()
    i = 0
    while i < n:
        notif = q.attention()
        if notif[1] != "Facebook":
            q.arrive(notif)
        i += 1

def mostrar_twitter_python(q: Queue):
    resultados = []
    n = q.size()
    i = 0
    while i < n:
        notif = q.attention()
        if notif[1] == "Twitter" and "Python" in notif[2]:
            resultados.append(notif)
        q.arrive(notif)
        i += 1
    return resultados

def notificaciones_pila_intervalo(q: Queue, inicio: str = "11:43", fin: str = "15:57") -> int:
    pila = Stack()
    n = q.size()
    i = 0
    while i < n:
        notif = q.attention()
        hora = notif[0]
        if inicio <= hora <= fin:
            pila.push(notif)
        q.arrive(notif)
        i += 1
    return pila.size()



print("Antes de eliminar Facebook:")
cola_notificaciones.show()

eliminar_facebook(cola_notificaciones)

print("\nDespués de eliminar Facebook:")
cola_notificaciones.show()

print("\nNotificaciones de Twitter con 'Python':")
for t in mostrar_twitter_python(cola_notificaciones):
    print(t)

cantidad = notificaciones_pila_intervalo(cola_notificaciones)
print(f"\nCantidad de notificaciones entre 11:43 y 15:57 almacenadas en pila: {cantidad}")