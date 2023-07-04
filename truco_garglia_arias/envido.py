import pygame
from pygame.locals import *
import random
import main

class ManoEnvido():
    def __init__(self):
        pass

    #def cartas_generadas(self):
     #   numero1, palo1, numero2, palo2, numero3, palo3 = main.random_cartas()
      #  return numero1, palo1, numero2, palo2, numero3, palo3

    def envido(self, numero1, palo1, numero2, palo2, numero3, palo3):
        lista_num = [numero1, numero2, numero3]

        for i in range(3):
            if lista_num[i] >= 10:
                lista_num[i] = 0

        if palo1 == palo2 and palo1 == palo3:
            lista_ord = sorted(lista_num, reverse=True)
            val1, val2 = lista_ord[0], lista_ord[1]
            resultado = val1 + val2 + 20
        elif palo1 != palo2 and palo1 != palo3 and palo2 != palo3:
            resultado = max(lista_num)
            if resultado == 0:
                resultado = 20
        else:
            if palo1 == palo2:
                val1, val2 = lista_num[0], lista_num[1]
            elif palo1 == palo3:
                val1, val2 = lista_num[0], lista_num[2]
            elif palo2 == palo3:
                val1, val2 = lista_num[1], lista_num[2]
            resultado = val1 + val2 + 20

        return resultado

    def jugar(self):
        numero1_jugador1, palo1_jugador1, numero2_jugador1, palo2_jugador1, numero3_jugador1, palo3_jugador1 = main.lista_j1
        resultado_jugador1 = self.envido(numero1_jugador1, palo1_jugador1, numero2_jugador1, palo2_jugador1, numero3_jugador1, palo3_jugador1)

        numero1_jugador2, palo1_jugador2, numero2_jugador2, palo2_jugador2, numero3_jugador2, palo3_jugador2 = main.lista_j2
        resultado_jugador2 = self.envido(numero1_jugador2, palo1_jugador2, numero2_jugador2, palo2_jugador2, numero3_jugador2, palo3_jugador2)

        pygame.init()
        width, height = 800, 600
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Envido Game")
        clock = pygame.time.Clock()

        bg_color = (235, 235, 208)
        text_color = (0, 0, 0)

        font = pygame.font.Font(None, 36)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            window.fill(bg_color)

            text_jugador1 = font.render("Jugador 1", True, text_color)
            window.blit(text_jugador1, (50, 50))

            text_carta1_jugador1 = font.render("Carta 1: {} de {}".format(numero1_jugador1, palo1_jugador1), True, text_color)
            window.blit(text_carta1_jugador1, (50, 100))

            text_carta2_jugador1 = font.render("Carta 2: {} de {}".format(numero2_jugador1, palo2_jugador1), True, text_color)
            window.blit(text_carta2_jugador1, (50, 150))

            text_carta3_jugador1 = font.render("Carta 3: {} de {}".format(numero3_jugador1, palo3_jugador1), True, text_color)
            window.blit(text_carta3_jugador1, (50, 200))

            text_jugador2 = font.render("Jugador 2", True, text_color)
            window.blit(text_jugador2, (400, 50))

            text_carta1_jugador2 = font.render("Carta 1: {} de {}".format(numero1_jugador2, palo1_jugador2), True, text_color)
            window.blit(text_carta1_jugador2, (400, 100))

            text_carta2_jugador2 = font.render("Carta 2: {} de {}".format(numero2_jugador2, palo2_jugador2), True, text_color)
            window.blit(text_carta2_jugador2, (400, 150))

            text_carta3_jugador2 = font.render("Carta 3: {} de {}".format(numero3_jugador2, palo3_jugador2), True, text_color)
            window.blit(text_carta3_jugador2, (400, 200))

            text_envido_jugador1 = font.render("El envido es: {}".format(resultado_jugador1), True, text_color)
            window.blit(text_envido_jugador1, (50, 300))

            text_envido_jugador2 = font.render("El envido es: {}".format(resultado_jugador2), True, text_color)
            window.blit(text_envido_jugador2, (400, 300))

            if resultado_jugador1 > resultado_jugador2:
                text_ganador = font.render("¡Jugador 1 gana!", True, text_color)
                window.blit(text_ganador, (50, 400))
            elif resultado_jugador1 < resultado_jugador2:
                text_ganador = font.render("¡Jugador 2 gana!", True, text_color)
                window.blit(text_ganador, (400, 400))
            else:
                text_ganador = font.render("¡Es un empate!", True, text_color)
                window.blit(text_ganador, (200, 400))

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

ManoEnvido = ManoEnvido()
ManoEnvido.jugar()
