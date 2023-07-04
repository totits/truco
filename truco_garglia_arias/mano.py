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
        
        #FALTA ARREGLAR ESTO. QUE TIRE EN QUE JERARQUIA ESTA LA CARTA
        for i in range(0, 14):
            if carta_j1 in jerarquia[i]:
                print(jerarquia[i].index(carta_j1))
        
        """
        if carta_j1 in jerarquia[0]:
            carta_j1_jerarquia = 1
        elif carta_j1 in jerarquia[1]:
            carta_j1_jerarquia = 2
        elif carta_j1 in jerarquia[2]:
            carta_j1_jerarquia = 3
        elif carta_j1 in jerarquia[3]:
            carta_j1_jerarquia = 4
        elif carta_j1 in jerarquia[4]:
            carta_j1_jerarquia = 5
        elif carta_j1 in jerarquia[5]:
            carta_j1_jerarquia = 6
        elif carta_j1 in jerarquia[6]:
            carta_j1_jerarquia = 7
        elif carta_j1 in jerarquia[7]:
            carta_j1_jerarquia = 8
        elif carta_j1 in jerarquia[8]:
            carta_j1_jerarquia = 9
        elif carta_j1 in jerarquia[9]:
            carta_j1_jerarquia = 10
        elif carta_j1 in jerarquia[10]:
            carta_j1_jerarquia = 11
        elif carta_j1 in jerarquia[11]:
            carta_j1_jerarquia = 12
        elif carta_j1 in jerarquia[12]:
            carta_j1_jerarquia = 13
        elif carta_j1 in jerarquia[13]:
            carta_j1_jerarquia = 14
        else:
            pass
        
        if carta_j2 in jerarquia[0]:
            carta_j2_jerarquia = 1
        elif carta_j2 in jerarquia[1]:
            carta_j2_jerarquia = 2
        elif carta_j2 in jerarquia[2]:
            carta_j2_jerarquia = 3
        elif carta_j2 in jerarquia[3]:
            carta_j2_jerarquia = 4
        elif carta_j2 in jerarquia[4]:
            carta_j2_jerarquia = 5
        elif carta_j2 in jerarquia[5]:
            carta_j2_jerarquia = 6
        elif carta_j2 in jerarquia[6]:
            carta_j2_jerarquia = 7
        elif carta_j2 in jerarquia[7]:
            carta_j2_jerarquia = 8
        elif carta_j2 in jerarquia[8]:
            carta_j2_jerarquia = 9
        elif carta_j2 in jerarquia[9]:
            carta_j2_jerarquia = 10
        elif carta_j2 in jerarquia[10]:
            carta_j2_jerarquia = 11
        elif carta_j2 in jerarquia[11]:
            carta_j2_jerarquia = 12
        elif carta_j2 in jerarquia[12]:
            carta_j2_jerarquia = 13
        elif carta_j2 in jerarquia[13]:
            carta_j2_jerarquia = 14
        else:
            pass
        
        if carta_j1_jerarquia < carta_j2_jerarquia:
            ganador = "jugador 1"
        elif carta_j1_jerarquia > carta_j2_jerarquia:
            ganador = "jugador 2"
        else:
            ganador = "empate"
        """

        print(carta_j1, carta_j2)
        print(f"ganador: chupala")

        


mano = Mano()

mano.comparacion()