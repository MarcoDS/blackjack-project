from random import shuffle

class Game():
	
	def __init__(self, number_of_decks, number_of_players):
		self.number_of_decks = number_of_decks
		self.number_of_players = number_of_players
		self.current_deck = []
		self.hands = {}

	def deal(self): #make a class
	    self.hands['dealer'] = []
	    self.hit('dealer')
	    self.hit('dealer')

	    for i in range(1,self.number_of_players + 1):
	        self.hands['player ' + str(i)] = []
	        self.hit(str(i))
	        self.hit(str(i))
	   
	    return self.hands

	def hit(self, target): #target should be dealer or player id
		if target == 'dealer':
			self.hands[target].append(self.current_deck.pop(0))
		else:
			self.hands['player ' + str(target)].append(self.current_deck.pop(0))
		return self.hands

	def print_deal(self): #i see i can replace the default print / look up the syntax
		for i in range(1,self.number_of_players + 1):
			print("Player %s your hand is: %s" % (i, self.hands['player ' + str(i)]))

		print("Dealer is showing: %s" % (self.hands['dealer'][0]))

	def shuffle_deck(self):    
	    self.current_deck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] * self.number_of_decks
	    shuffle(self.current_deck)
	    return self.current_deck

def hand_value(hand):
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
