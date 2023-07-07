import main
import random


class Mano():
    def __init__(self) :
        #jerarquias de cartas
        self.mano_j1 = main.lista_j1_tupla
        self.mano_j2 = main.lista_j2_tupla
        
    def seleccion_carta(self):

        print(main.lista_j1_tupla)

        while True:
            indice_carta_j1 = int(input("Jugar carta 1, 2 o 3: "))
            if indice_carta_j1 == 1:
                carta_j1 = self.mano_j1[0]
                break
            elif indice_carta_j1 == 2:
                carta_j1 = self.mano_j1[1]
                break
            elif indice_carta_j1 == 3:
                carta_j1 = self.mano_j1[2]
                break
            else:
                print("Error en la eleccion")

        carta_j2 = random.choice(self.mano_j2)
        return carta_j1, carta_j2
    def comparacion(self):

        jerarquia = [
        [(main.palos[3], main.numeros[0])],
        [(main.palos[1], main.numeros[0])],
        [(main.palos[3], main.numeros[6])],
        [(main.palos[0], main.numeros[6])],
        [(main.palos[3], main.numeros[2]),(main.palos[2], main.numeros[2]),(main.palos[1], main.numeros[2]),(main.palos[1], main.numeros[2])],
        [(main.palos[3], main.numeros[1]),(main.palos[2], main.numeros[1]),(main.palos[1], main.numeros[1]),(main.palos[1], main.numeros[1])],
        [(main.palos[0], main.numeros[0]),(main.palos[2], main.numeros[0])],
        [(main.palos[3], main.numeros[9]),(main.palos[2], main.numeros[9]),(main.palos[1], main.numeros[9]),(main.palos[1], main.numeros[9])],
        [(main.palos[3], main.numeros[8]),(main.palos[2], main.numeros[8]),(main.palos[1], main.numeros[8]),(main.palos[1], main.numeros[8])],
        [(main.palos[3], main.numeros[7]),(main.palos[2], main.numeros[7]),(main.palos[1], main.numeros[7]),(main.palos[1], main.numeros[7])],
        [(main.palos[1], main.numeros[6]),(main.palos[2], main.numeros[6])],
        [(main.palos[3], main.numeros[5]),(main.palos[2], main.numeros[5]),(main.palos[1], main.numeros[5]),(main.palos[1], main.numeros[5])],
        [(main.palos[3], main.numeros[4]),(main.palos[2], main.numeros[4]),(main.palos[1], main.numeros[4]),(main.palos[1], main.numeros[4])],
        [(main.palos[3], main.numeros[3]),(main.palos[2], main.numeros[3]),(main.palos[1], main.numeros[3]),(main.palos[1], main.numeros[3])]
        ]

        carta_j1, carta_j2 = Mano.seleccion_carta(self)
        
        # busco carta 1 en la lista de jerarquias
        for i in range(len(jerarquia)):
            for x in range (len(jerarquia[i])):
                if (carta_j1[0] in jerarquia[i][x]) and (carta_j1[1] in jerarquia[i][x]):
                    carta_j1_jerarquia = jerarquia[i]
                    # busco carta 2 en la lista de jerarquias
                    for y in range(len(jerarquia)):
                        for z in range (len(jerarquia[y])):
                            if (carta_j2[0] in jerarquia[y][z]) and (carta_j2[1] in jerarquia[y][z]):
                                carta_j2_jerarquia = jerarquia[y]
                                # comparo las jerarquias de las cartas
                                if i < y:
                                    ganador = 1
                                elif i > y:
                                    ganador = 2
                                else:
                                    ganador = 3
        


                                



                    
            
        

        print(carta_j1, carta_j2)
        print(f"ganador: {ganador}")


        


mano = Mano()

mano.comparacion()
