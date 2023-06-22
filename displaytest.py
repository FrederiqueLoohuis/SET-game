# importing required library
import pygame
import SET
'''
Bij start spel print 12 kaarten op scherm
schrijf functie waarbij je het spel vernieuwd >> kaarten verwijderen en nieuwe op het scherm displayen

functie update_screen:
def update_screen(kaarten_op_tafel):
	

'''

# activate the pygame library .
pygame.init()
X = 600
Y = 800

# create the display surface object
# of specific dimension..e(X, Y).
# scherm object >> X en Y >> grootte van scherm
scrn = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('image')

# image kun je laden met load
# create a surface object, image is drawn on it.
# convert?
# data set dowloaden >> setwd naar waar het staat >> image naam geven mt bijvoorbeeld groenediamantleeg

# kaart = SET.Kaart(2, 'red', 'oval', 'filled')
# imp = kaart.img
# imp = pygame.image.load('Kaarten\greendiamondempty1.gif')

# Using blit to copy content from one surface to other
# image op scherm
# coordinaten in pixels
# scrn.blit(imp, (0,0))



grid = []
for col in range(3):
	for row in range(4):
		grid.append((110*row,220*col))

print(grid)


def print_screen(kaarten_op_tafel):
	for coord, krt in zip(grid, kaarten_op_tafel): # zip rits twee lijsten aan elkaar
		print(krt)
		imp = krt.img
		scrn.blit(imp, coord)

op_tafel, stapel = SET.pop_12_kaarten()
print_screen(op_tafel)


# paint screen one time
pygame.display.flip()
#pygame.display.fill((0, 0, 0)) #misschien screen.fill, achtergrond kleur scherm. Kleur meegeven = tuple

status = True
while (status):
# hier in de logica van je spel zetten
# iterate over the list of Event objects: events is hoe je interact met je scherm, bijvoorbeeld klikken. getallen intikken = event
# that was returned by pygame.event.get() method.
	for i in pygame.event.get():

		# if event object type is QUIT
		# then quitting the pygame
		# and program both.
		if i.type == pygame.QUIT:
			status = False
        # klok
        # stapel leeg?

# deactivates the pygame library
pygame.quit()
