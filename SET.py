'''
Als eerst is het belangrijk om de juiste packages te hebben geïnstalleerd en vervolgens om ze te importeren.
'''
import random
import pygame
import math
from enum import Enum


'''
We maken verschillende klassen aan voor Kleur, Vorm en Vulling. 
De klassen die we maken zijn Enums. Dit zijn sets van unieke waardes die we een symbolische naam geven. 
# rood is de symbolische naam voor de waarde 'red'
'''

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


'''
Hieronder schrijven we de klasse Kaart. 
de __init__ constructor gebruiken we om aan te geven wat de waardes zijn van de specifieke kaart die we initialiseren 
'''
class Kaart:
    def __init__(self, aantal: int, kleur: Kleur, vorm: Vorm,
                 vulling: Vulling):  # self = het object (dus de kaart waar het om gaat)
        self.aantal = aantal
        self.kleur = kleur
        self.vorm = vorm
        self.vulling = vulling
        self.attrs = (aantal, kleur, vorm, vulling)
        self.img = pygame.image.load(f'Kaarten/{kleur.value}{vorm.value}{vulling.value}{aantal}.gif')

'''
de volgende functie controleert of er een set is.
We kijken of de aantallen en de objecten van de klassen kleur, vorm en vulling voor de 3 kaarten allemaal het zelfde zijn of allemaal anders.
'''
def is_set(k1: Kaart, k2: Kaart, k3: Kaart):
    aantal_set = (k1.aantal == k2.aantal and k2.aantal == k3.aantal) or (k1.aantal != k2.aantal and k1.aantal != k3.aantal and k2.aantal != k3.aantal)
    kleur_set = (k1.kleur == k2.kleur and k2.kleur == k3.kleur) or (k1.kleur != k2.kleur and k1.kleur != k3.kleur and k2.kleur != k3.kleur)
    vorm_set = (k1.vorm == k2.vorm and k2.vorm == k3.vorm) or (k1.vorm != k2.vorm and k1.vorm != k3.vorm and k2.vorm != k3.vorm)
    vulling_set = (k1.vulling == k2.vulling and k2.vulling == k3.vulling) or (k1.vulling != k2.vulling and k1.vulling != k3.vulling and k2.vulling != k3.vulling)

    return aantal_set and kleur_set and vorm_set and vulling_set




''' 
In de volgende functie maken we een functie die index creëert met de opties van kaart combinaties. 
Dus stel er zijn 12 kaarten dan berekent deze functie hoeveel combinaties van 3 kaarten je kan maken
(zonder de inhoud van die kaarten te weten
12 kies 3 = 220 mogelijke sets
81 kaarten
81 kies 3 = 85320
'''
def genereer_opties():
    opties = []
    # Nadat kaart 1 is geweest hoeven we die niet meer ergens mee te vergelijken,
    # omdat we dat dan al in deze loop hebben gedaan
    for kaart_index_1 in range(12):
        for kaart_index_2 in range(kaart_index_1 + 1, 12):
            for kaart_index_3 in range(kaart_index_2 + 1, 12):
                opties.append((kaart_index_1, kaart_index_2, kaart_index_3))

    return opties

# bereken dit maar 1 keer, omdat het resultaat altijd hetzelfde is:
kies_3_uit_12_opties = genereer_opties()

'''
Hieronder schrijven we een functie die meerdere sets kan vinden. De gevonden sets worden bij gehouden in de lijst 'sets'.
ipv genereer_opties() : math.comb(12,3) gebruiken in de functie hieronder?
Er moeten altijd 12 kaarten op tafel liggen >> liggen deze er niet dan moet de functie een error geven.
er moeten eerste nieuwe kaarten neergelegd worden. 
'''
def vind_sets(kaarten):
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

'''
De volgende functie vindt een enkele set, maar nu wordt de gevonden set niet opgeslagen in een lijst.
'''
def vind_set(kaarten) -> tuple:
    global kies_3_uit_12_opties
    if len(kaarten) != 12:
        raise ValueError(f'12 kaarten verwacht, kreeg er {len(kaarten)}')
    # we gaan door de verschillende combinaties van 3 kaarten heen
    for (kaart_index_1, kaart_index_2, kaart_index_3) in kies_3_uit_12_opties:
        kaart1 = kaarten[kaart_index_1]
        kaart2 = kaarten[kaart_index_2]
        kaart3 = kaarten[kaart_index_3]
        if is_set(kaart1, kaart2, kaart3):
            return kaart_index_1, kaart_index_2, kaart_index_3  # we voegen de gevonden sets toe aan de lijst sets

    return None

'''
Hieronder schrijven we een functie die de stapel kaarten genereert.
De functie geeft alle 81 mogelijke kaarten.
Elke kaart wordt weergegeven met het index nummer van de kleur, het aantal, de vulling en de vorm.
alle kaarten die gegenereerd worden, worden toegevoegd aan de lijst stapel[]
'''
# Er zijn 81 kaarten, alle mogelijke kaarten
def genereer_stapel():
    stapel = []
    for kleur in Kleur:
        for aantal in [1,2,3]:
            for vulling in Vulling:
                for vorm in Vorm:
                    kaart = Kaart(aantal, kleur, vorm, vulling)
                    stapel.append(kaart)
    return stapel

'''
Hieronder schrijven we een functie die 12 random kaarten op tafel legt.
De functie pakt steeds de bovenste kaarten van de stapel. 
De stapel bestaat nu uit alle kaarten die onder de 12 kaarten lagen.
'''
def pak_12_kaarten():
    stapel = genereer_stapel()
    random.shuffle(stapel)

    kaarten_op_tafel = stapel[:12]
    stapel = stapel[12:]

    return kaarten_op_tafel, stapel

'''
Met de volgende functie wordt de gevonden set verwijderd uit de stapel
'''
def vernieuw_spel(kaarten_op_tafel, stapel, set: tuple):
    kaart_index_1, kaart_index_2, kaart_index_3 = set

    kaarten_op_tafel[kaart_index_1] = stapel[0]
    kaarten_op_tafel[kaart_index_2] = stapel[1]
    kaarten_op_tafel[kaart_index_3] = stapel[2]

    stapel = stapel[3:]
    return kaarten_op_tafel, stapel




