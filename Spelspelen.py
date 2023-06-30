'''
Door het volgende script te runnen begint het spel.
'''
# importing required library
import pygame
import SET

# activeer de pygame library .
pygame.init()
X = 600
Y = 800

# Hieronder creëren we de display. X en Y bepalen de grootte van het scherm
scrn = pygame.display.set_mode((X, Y))

# We bepalen de naam van de pygame window
pygame.display.set_caption('image')

# We creëren een klok die de tijd bijhoudt gedurende het spel.
clock = pygame.time.Clock()


# We bepalen de coördinaten van de kaarten die op het scherm zullen verschijnen.
# Elke cel in de grid heeft een x- en een y-coördinaat, en de positie van de cel wordt bepaald op basis van de rij- en kolomindex in de grid.
grid_breedte = 4
grid_hoogte = 3

grid = []
for col in range(grid_hoogte):
	for row in range(grid_breedte):
		grid.append((110*row,220*col))

def print_screen(kaarten_op_tafel, aangeklikt):
	global grid, scrn

	scrn.fill((0, 0, 0))

	index = 0
	for coord, krt in zip(grid, kaarten_op_tafel): # zip rits twee lijsten aan elkaar
		# print(krt)
		if index in aangeklikt:
			# als deze kaart aangeklikt is, geef dan de achtergrond een kleurtje
			rechthoek = pygame.Rect(coord, (110, 220))
			pygame.draw.rect(scrn, (0, 0, 255), rechthoek)
		imp = krt.img
		scrn.blit(imp, coord)
		index += 1
	pygame.display.flip()

computer_countdown_duur = 30 * 1000 # in milliseconde
computer_verwijdert = True

if __name__ == '__main__':
	print(grid)

	op_tafel, stapel = SET.pak_12_kaarten()

	aangeklikt = set()

	speler_punten = 0
	computer_punten = 0

	computer_countdown = computer_countdown_duur

	status = True
	while (status):
	# Hier itereren we over de lijst van Event objecten.
	# Een event bepaalt hoe je interacteert met je scherm, bijvoorbeeld door kaarten aan te klikken
		for i in pygame.event.get():

			# if event object type is QUIT
			# then quitting the pygame
			# and program both.
			if i.type == pygame.QUIT:
				status = False

			# als er geklikt wordt
			if i.type == pygame.MOUSEBUTTONDOWN:
				x, y = pygame.mouse.get_pos()
				# kijk in welke grid cel we zitten
				col = x // 110
				row = y // 210

				# kijk of die buiten onze grid valt
				if col >= grid_breedte:
					continue # doe er niets mee
				if row >= grid_hoogte:
					continue # doe er niets mee

				index = row * grid_breedte + col
				# als deze al aangeklikt is halen we hem uit de set van aangeklikte kaart indexen
				if index in aangeklikt:
					aangeklikt.remove(index)
				else:
					aangeklikt.add(index)
				# print(x, y, col, row, index)
				print(aangeklikt)

			if len(aangeklikt) >= 3:
				# check of het een set is
				kaart_index_1 = aangeklikt.pop()
				kaart_index_2 = aangeklikt.pop()
				kaart_index_3 = aangeklikt.pop()

				# pak de kaarten op die plekken
				kaart_1 = op_tafel[kaart_index_1]
				kaart_2 = op_tafel[kaart_index_2]
				kaart_3 = op_tafel[kaart_index_3]

				is_set = SET.is_set(kaart_1, kaart_2, kaart_3)

				print('Set:', is_set)

				if is_set:
					print("Gefeliciteerd, je hebt een set")
					speler_punten += 1
					if len(stapel) < 3:
						# spel afgelopen!
						status = False
					else:
						# verwijder set en vul aan met 3 kaarten
						op_tafel, stapel = SET.vernieuw_spel(op_tafel, stapel, (kaart_index_1, kaart_index_2, kaart_index_3))
						# reset de countdown
						computer_countdown += computer_countdown_duur
				else:
					print('Helaas pindakaas!')

		# is de countdown afgelopen?
		frame_tijd = clock.get_time()
		computer_countdown -= frame_tijd
		# print(clock.get_time() - begintijd_computer_countdown)
		if computer_countdown <= 0:
			# doe een computer beurt
			computer_set = SET.vind_set(op_tafel)

			if computer_set is None:
				print('Geen set')
				if len(stapel) < 3:
					status = False
				else:
					op_tafel, stapel = SET.vernieuw_spel(op_tafel, stapel, (0, 1, 2))
			else:
				computer_punten += 1
				print("haha wij hebben hem wel gevonden")
				if computer_verwijdert:
					if len(stapel) < 3:
						status = False
					else:
						op_tafel, stapel = SET.vernieuw_spel(op_tafel, stapel, computer_set)
						aangeklikt.clear()

			# reset de countdown
			computer_countdown += computer_countdown_duur

		print_screen(op_tafel, aangeklikt)
		clock.tick(60)

	# Spel afgelopen
	print('Computer punten:', computer_punten, 'Jouw punten:', speler_punten)
	# We deactiveren de pygame library
	pygame.quit()
