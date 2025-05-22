import random

tarifas = {
    "automovil": 47,
    "camioneta": 59,
    "camion": 71,
    "colectivo": 64
}

tiposVehiculos = list(tarifas)  

class vehiculo:  
    def __init__(self, Tipo):  
        self.tipo = Tipo
        self.tarifa = tarifas[Tipo]

    def __str__(self):  
        return self.tipo + " ($" + str(self.tarifa) + ")"  

class cabina:  
    def __init__(self, n):  
        self.numero = n
        self.recaudado = 0
        self.contador = {
            "automovil": 0,
            "camioneta": 0,
            "camion": 0,
            "colectivo": 0
        }

    def atender(self, v):  
        self.recaudado = self.recaudado + v.tarifa
        self.contador[v.tipo] = self.contador[v.tipo] + 1
        print("Cabina", self.numero, "atendio a", v, "total:", self.recaudado)  

    def mostrarResumen(self):  
        print("Resumen de cabina", self.numero)
        print("Recaudado: $", self.recaudado)
        for t in tiposVehiculos:
            print(t + ":", self.contador[t])

def totalRecaudado(c):  
    return c.recaudado

cabinas = []
for i in range(3):  
    cabinas.append(cabina(i + 1))

for i in range(30):  
    tipo = random.choice(tiposVehiculos)
    v = vehiculo(tipo)
    c = random.choice(cabinas)
    c.atender(v)

cabinaMax = max(cabinas, key=totalRecaudado)
print("La cabina que más recaudó fue la", cabinaMax.numero, "con $", cabinaMax.recaudado)

for c in cabinas:
    c.mostrarResumen()
