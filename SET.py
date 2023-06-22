# Enum = een set van unieke waardes die een symbolische naam hebben.
import random
import pygame
import math
from enum import Enum


# De set kleuren die we mogen gebruiken
class Kleur(Enum):
    rood = 'red'
    groen = 'green'
    paars = 'purple'


class Vorm(Enum):
    diamant = 'diamond'
    golfje = 'squiggle'
    rondje = 'oval'


class Vulling(Enum):
    solide = 'filled'
    gestreept = 'shaded'
    open = 'empty'


class Kaart:
    def __init__(self, aantal: int, kleur: Kleur, vorm: Vorm,
                 vulling: Vulling):  # self = het object (dus de kaart waar het om gaat)
        self.aantal = aantal
        self.kleur = kleur
        self.vorm = vorm
        self.vulling = vulling
        self.attrs = (aantal, kleur, vorm, vulling)
        self.img = pygame.image.load(f'Kaarten/{kleur}{vorm}{vulling}{aantal}.gif')

    def __eq__(self, other):
        if self.attrs == other.attrs:
            return True
        else:
            return False

# de volgende functie controleert of op een kaart alle symbolen hetzelfde zijn of juist allemaal anders.
def is_set(k1: Kaart, k2: Kaart, k3: Kaart):
    allemaal_zelfde = (k1.aantal == k2.aantal and k2.aantal == k3.aantal) \
                      and (k1.kleur == k2.kleur and k2.kleur == k3.kleur) \
                      and (k1.vorm == k2.vorm and k2.vorm == k3.vorm) \
                      and (k1.vulling == k2.vulling and k2.vulling == k3.vulling)

    allemaal_anders = (k1.aantal != k2.aantal and k1.aantal != k3.aantal and k2.aantal != k3.aantal) \
                      and (k1.kleur != k2.kleur and k1.kleur != k3.kleur and k2.kleur != k3.kleur) \
                      and (k1.vorm != k2.vorm and k1.vorm != k3.vorm and k2.vorm != k3.vorm) \
                      and (k1.vulling != k2.vulling and k1.vulling != k3.vulling and k2.vulling != k3.vulling)

    return allemaal_zelfde or allemaal_anders


# alle mogelijke sets vinden in verzameling van 12 kaarten
# 12 kies 3 = 220 mogelijke sets
# 81 kaarten
# 81 kies 3 = 85320

''' In de volgende functie maken we een functie die index creëert met de opties van kaart combinaties. Dus stel er zijn 12 kaarten dan berekent deze functie hoeveel combinaties van 3 kaarten je kan maken (zonder de inhoud van die kaarten te weten'''
def genereer_opties():
    opties = []
    # Nadat kaart 1 is geweest hoeven we die niet meer ergens mee te vergelijken,
    # omdat we dat dan al in deze loop hebben gedaan
    for kaart_index_1 in range(12):
        for kaart_index_2 in range(kaart_index_1 + 1, 12):
            for kaart_index_3 in range(kaart_index_2 + 1, 12):
                opties.append((kaart_index_1, kaart_index_2, kaart_index_3))

    return opties


kies_3_uit_12_opties = genereer_opties()

def vind_sets(kaarten):
    math.comb(12,3)
    global kies_3_uit_12_opties
    if len(kaarten) != 12:
        raise ValueError(f'12 kaarten verwacht, kreeg er {len(kaarten)}')
    sets = [] # we maken een lijst om de gevonden sets in op te slaan

    # we gaan door de verschillende combinaties van 3 kaarten heen
    for (kaart_index_1, kaart_index_2, kaart_index_3) in kies_3_uit_12_opties:
        kaart1 = kaarten[kaart_index_1]
        kaart2 = kaarten[kaart_index_2]
        kaart3 = kaarten[kaart_index_3]
        if is_set(kaart1, kaart2, kaart3):
            sets.append((kaart1, kaart2, kaart3)) # we voegen de gevonden sets toe aan de lijst sets

    return sets

# De volgende functie vind een enkele set
def vind_set(kaarten):
    global kies_3_uit_12_opties
    if len(kaarten) != 12:
        raise ValueError(f'12 kaarten verwacht, kreeg er {len(kaarten)}')
    # we gaan door de verschillende combinaties van 3 kaarten heen
    for (kaart_index_1, kaart_index_2, kaart_index_3) in kies_3_uit_12_opties:
        kaart1 = kaarten[kaart_index_1]
        kaart2 = kaarten[kaart_index_2]
        kaart3 = kaarten[kaart_index_3]
        if is_set(kaart1, kaart2, kaart3):
            return ((kaart1, kaart2, kaart3)) # we voegen de gevonden sets toe aan de lijst sets

    return None


# Er zijn 81 kaarten, alle mogelijke kaarten
def genereer_stapel():
    stapel = []
    for kleur in ['red', 'green', 'purple']:
        for aantal in [1,2,3]:
            for vulling in ['filled', 'shaded', 'empty']:
                for vorm in ['squiggle', 'oval', 'diamond']:
                    kaart = Kaart(aantal, kleur, vorm, vulling)
                    stapel.append(kaart)
    return stapel


def pop_12_kaarten():
    stapel = genereer_stapel()
    random.shuffle(stapel)

    kaarten_op_tafel = stapel[:12]
    stapel = stapel[12:]

    return kaarten_op_tafel, stapel

# set = input van de user
def vernieuw_spel(kaarten_op_tafel, stapel, set):
    for x in set:
        kaarten_op_tafel.remove(x)

    random.shuffle(stapel)
    kaarten_op_tafel.append(stapel[:3])
    stapel = stapel[3:]
    return kaarten_op_tafel, stapel

    # kaarten_op_tafel = []
    # while len(stapel) >= 12:
    #     kaarten_op_tafel = stapel[:12]
    #     stapel = stapel[12:]

'''
if geen set
    verwijder bovenste 3 kaarten en vul aan met nieuwe pop_12_kaarten
'''




# uit de stapel pakken we nu 12 kaarten. De stapel bestaat nu uit het aantal kaarten dat overblijft.


async def main():
    async with asyncio.timeout(30):
        await long_running_task()

# def pop_12_kaarten
# uit sets van 81 kaarten >> 12 kaarten halen
# gebruik pop, dan wordt die verwijderd.
random.shuffle
# genereert stapel van 81 kaarten, die schut je met random.shuffle en dan pak je 12 kaarten.

# gebruik functie vind set om te kijken of er sets in de 12 kaarten zit. Zo niet, geneer nieuwe 12 kaarten.
# totdat je set hebt of de stapel leeg is.

'''
functie die kaarten van tafel als je een set hebt gevonden en 3 nieuwe plaatst
'''
