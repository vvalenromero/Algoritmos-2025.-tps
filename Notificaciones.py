class notificacion:  
    def __init__(self, Hora, App, Mensaje):  
        self.hora = Hora  
        self.aplicacion = App
        self.contenido = Mensaje

    def __str__(self):
        return "[" + self.hora + "] " + self.aplicacion + ": " + self.contenido  

def eliminarFacebook(lista):  
    nueva = []
    for notif in lista:
        if notif.aplicacion.lower() != "facebook":
            nueva.append(notif)
    return nueva

def mostrarTwitterPython(l):  
    print("Notificaciones de twitter que tienen la palabra python:")  
    for x in l:
        if x.aplicacion.lower() == "twitter":
            if "python" in x.contenido.lower():
                print(x)

def rangoNotificaciones(lista, desde, hasta):  
    pila = []  
    for i in lista:
        if i.hora >= desde and i.hora <= hasta:
            pila.append(i)
    print("Hay", len(pila), "notificaciones entre", desde, "y", hasta)
    return pila

def mostrarLista(lista, titulo = "lista de notificaciones"):  
    print(titulo + ":")
    for i in lista:
        print(i)


colaOriginal = [
    notificacion("09:00", "Telegram", "Recordatorio de reunion"),
    notificacion("10:15", "Facebook", "Tienes nuevos amigos sugeridos"),
    notificacion("11:00", "Twitter", "Aprende Python en 10 dias"),
    notificacion("12:30", "Linkedin", "Nueva oferta de trabajo"),
    notificacion("13:00", "twitter", "Comparte tu proyecto en python"),
    notificacion("15:00", "FACEBOOK", "Eventos cerca de ti")
]

mostrarLista(colaOriginal, "Notifs originales")

colaSinFb = eliminarFacebook(colaOriginal)

mostrarLista(colaSinFb, "Sin Facebook")

mostrarTwitterPython(colaSinFb)

pilaTemporal = rangoNotificaciones(colaSinFb, "10:00", "14:00")
