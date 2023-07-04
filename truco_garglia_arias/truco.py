import main
import envido

class Truco():
    def __init__(self):
        pass
    def jugar(self):
        numero1_jugador1, palo1_jugador1, numero2_jugador1, palo2_jugador1, numero3_jugador1, palo3_jugador1 = main.lista_j1
        resultado_jugador1 = self.envido(numero1_jugador1, palo1_jugador1, numero2_jugador1, palo2_jugador1, numero3_jugador1, palo3_jugador1)

        numero1_jugador2, palo1_jugador2, numero2_jugador2, palo2_jugador2, numero3_jugador2, palo3_jugador2 = main.lista_j2
        resultado_jugador2 = self.envido(numero1_jugador2, palo1_jugador2, numero2_jugador2, palo2_jugador2, numero3_jugador2, palo3_jugador2)
        
    