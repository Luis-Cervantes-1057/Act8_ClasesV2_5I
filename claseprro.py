print("CLASES VERSION 2 EL CONSTRUCTOR")

class Perro:
    #Funcion Constructor
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad

        #Funciones creadas por el usuario
    def muerde(self):
            print("ME MORDIO EL PERRO W")
    def chatperro(self,mensaje):
            print(f"Chat perro: {mensaje}")
    def chatperra(self,mensajep):
            print(f"Chat perra: {mensajep}")
    def datos (self):
            print(f"Color: {self.color}\nEdad: {self.edad}")
#Crear objeto
cofi = Perro("Trae smoking", 4)

#Llamada a funciones
cofi.datos()
cofi.muerde()
cofi.chatperro("HOLa soy DominiK")
cofi.chatperra("SOy ladygaga")
cofi.chatperro("Quieres ser mi cachorrita?")
cofi.chatperra("grrru.....")