'''
Aantekeningen TA over klassen 
Maak een klasse 'Kaart' en een klasse "spel'

class Card:
     Def __int__(arg)
     
     
Self arg = random
     Def __ str __()
     Def is- Set(self, kaart1, kaart2)


 Kaart = Card (arg)
 Kaart_is_set( … )


 Class SetGame
 Methode die alle mogelijke sets bekijkt
 Methode: Vindt alle sets in kaarten
 Print het naar mijn scherm
 Methode:  vind 1 set     

class Kaart:
     aantal = 1
     figuur = 'rondje'
'''


import random

aantal = ["1", "2", "3"]
kleur = ["rood", "groen", "paars"]
vorm = ["diamant", "ovaal", "golf"]
vulling = ["solide", "gestreept", "open"]
test= 0

def kaartengenerator(n):
    lijst_met_kaarten = []

    for i in range(1, n + 1):
        nieuwelijst = []

        nieuwelijst.append(random.choice(aantal))
        nieuwelijst.append(random.choice(kleur))
        nieuwelijst.append(random.choice(vorm))
        nieuwelijst.append(random.choice(vulling))
        lijst_met_kaarten.append(nieuwelijst)

    return lijst_met_kaarten


print(kaartengenerator(3))


def is_set(invoer):
    kaarten = invoer
    truth_tabel = 4 * [True]
    truth = []
    for i in range(4):
        if kaarten[0][i] != kaarten[1][i] != kaarten[2][i] and kaarten[0][i] != kaarten[2][i] or kaarten[0][i] == \
                kaarten[1][i] == kaarten[2][i]:
            truth.append(True)
        else:
            truth.append(False)
    uitkomst = truth_tabel == truth

    return uitkomst
