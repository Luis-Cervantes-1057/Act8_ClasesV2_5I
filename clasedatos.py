class Informacion:

    def mi_lista(self):
        lista_Nomperros=["boby","Cofi","fany"]
        for x in lista_Nomperros: 
            print(x)

    def mi_tupla(self):
        tupla_Minovia=("Alesita","Mi pastelito","Mi niña")
        for x in tupla_Minovia: 
            print(x)

    def mi_set(self):
        set_Carros={"Camaro","ZL1","2019"}
        for x in set_Carros: 
            print(x)

    def mi_diccionario(self):
        equipos = {
        "Barcelona": "Lamine Yamal",
        "Argentina": "Lionel Andres MESSI",
        "America" : "Henry la bomba yucateca Martin"
        }
        for x,y in equipos.items():
            print(x,y)

#Creando el objeto
datos = Informacion()
print("Listado de Nombres de perros")
datos.mi_lista()
print("")
print("Tupla de pronombres de mi noviecita")
datos.mi_tupla()
print(" ")
print("Conjunto de un carro")
datos.mi_set()
print("")
print("Diccionario de mis equipos")
datos.mi_diccionario()
