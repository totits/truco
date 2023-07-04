import random

palos = ["oro", "basto", "copa", "espada"]
numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]

def random_cartas():
        numero1 = random.choice(numeros)
        palo1 = random.choice(palos)

        numero2 = random.choice(numeros)
        palo2 = random.choice(palos)

        while numero2 == numero1 and palo2 == palo1:
            numero2 = random.choice(numeros)
            palo2 = random.choice(palos)

        numero3 = random.choice(numeros)
        palo3 = random.choice(palos)

        while (numero3 == numero1 and palo3 == palo1) or (numero2 == numero3 and palo2 == palo3):
            numero3 = random.choice(numeros)
            palo3 = random.choice(palos)

        return numero1, palo1, numero2, palo2, numero3, palo3

# cartas del jugador optimizadas para ENVIDO
j1_n1, j1_p1, j1_n2, j1_p2, j1_n3, j1_p3 = random_cartas()
lista_j1 = [j1_n1, j1_p1, j1_n2, j1_p2, j1_n3, j1_p3]
j2_n1, j2_p1, j2_n2, j2_p2, j2_n3, j2_p3 = random_cartas()
lista_j2 = [j2_n1, j2_p1, j2_n2, j2_p2, j2_n3, j2_p3]

# cartas del jugador optimizadas para MANO o TRUCO
lista_j1_tupla = [(j1_n1, j1_p1), (j1_n2, j1_p2), (j1_n3, j1_p3)]
lista_j2_tupla = [(j2_n1, j2_p1), (j2_n2, j2_p2), (j2_n3, j2_p3)]