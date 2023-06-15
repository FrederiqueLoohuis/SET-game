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

'''

class Kaart:
    def __init__(self, aantal, kleur, vorm, vulling ):
        self.aantal = aantal
        self.kleur = kleur
        self.vorm = vorm
        self.vulling = vulling
        self.attrs = (aantal, kleur, vorm, vulling)

    def is_set(self,k2,k3):
        def same_or_different(attr1, attr2, attr3):
            if attr1 == attr2 !=attr3 or attr1 != attr2 == attr3 or attr1 == attr3 != attr2:
                return False
            else: return True
        for attr1,attr2,attr3 in zip(self.attrs, k2.attrs, k3.attrs):
            if not same_or_different(attr1, attr2, attr3):
                return False
        return True

k1 = Kaart(2,"groen", "diamant", "open")
k2 = Kaart(2,"paars", "driehoek", "gestreept")
k3 = Kaart(2,"blauw", "rondje", "solide")
print(k1.is_set(k2,k3))
