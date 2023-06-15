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


class Kaarten:
    def __init__(self, aantal, kleur, vorm, vulling ):
        self.aantal = aantal
        self.kleur = kleur
        self.vorm = vorm
        self.vulling = vulling

    def is_set(self):
        if k1.aantal == k2.aantal !=k3.aantal or k1.aantal != k2.aantal == k1.aantal or k1.aantal == k3.aantal != k2.aantal:
            print(False)
        elif k1.kleur == k2.kleur !=k3.kleur or k1.kleur != k2.kleur == k1.kleur or k1.kleur == k3.kleur != k2.kleur:
            print(False)
        elif k1.vorm == k2.vorm !=k3.vorm or k1.vorm != k2.vorm == k1.vorm or k1.vorm == k3.vorm != k2.vorm:
            print(False)
        elif k1.vulling == k2.vulling !=k3.vulling or k1.vulling != k2.vulling == k1.vulling or k1.vulling == k3.vulling != k2.vulling:
            print(False)
        else:
            print(True)
            
    
k1 = Kaarten(2,"groen", "diamant", "open")
k2 = Kaarten(1,"paars", "driehoek", "gestreept")
k3 = Kaarten(3,"blauw", "rondje", "solide")

k1,k2,k3.is_set()
