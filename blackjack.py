from random import shuffle

class Game():

	def __init__(self, number_of_decks, number_of_players):
		self.number_of_decks = number_of_decks
		self.number_of_players = number_of_players
		self.current_deck = []
		self.hands = {}

	def deal(self): 
		#Sets up each round by creating starting hands for dealer and each player
	    self.hands['dealer'] = []
	    self.hit('dealer')
	    self.hit('dealer')

	    for i in range(self.number_of_players):
	        self.hands['player ' + str(i)] = []
	        self.hit(str(i))
	        self.hit(str(i))
	   
	    return self.hands

	def hit(self, target): 
		#Adds a card from top of the deck to target hand
		if target == 'dealer':
			self.hands[target].append(self.current_deck.pop(0))
		else:
			self.hands['player ' + str(target)].append(self.current_deck.pop(0))
		return self.hands

	def print_deal(self): 
		#Prints initial deal output
		for i in range(self.number_of_players):
			print("Player %s your hand is: %s" % ((i+1), self.hands['player ' + str(i)]))

		print("Dealer is showing: %s" % (self.hands['dealer'][0]))

	def shuffle_deck(self):    
		#Shuffles total deck to create a new one
	    self.current_deck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] * self.number_of_decks
	    shuffle(self.current_deck)
	    return self.current_deck

def hand_value(hand):
	#Returns numeric value of said hand
	value = 0
	ace_count = 0
	for r,s in hand:
		if r in '2,3,4,5,6,7,8,9':
			value += int(r)
		elif r in 'TJQK':
			value += 10
		elif r == 'A':
			value += 11
			ace_count += 1

	while value > 21 and ace_count > 0:
		value -= 10
		ace_count -= 1

	return value

print("Welcome to BlackJack.")
print("Everyone starts with 1000$")
print("Bets are fixed at 50$")
print("")

current_game = Game(6, 1)
current_game.shuffle_deck()
current_game.deal()
current_game.print_deal()


#	decision = input("Player %s will you Hit, Stand or Double ?" % (i))
