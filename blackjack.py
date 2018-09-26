from random import shuffle

def shuffle_deck(n):    
    initial_deck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] * n
    shuffle(initial_deck)
    return initial_deck

def deal(game): #make a class
    game['dealer'] = []
    game['dealer'].append(game['deck'].pop(0))
    game['dealer'].append(game['deck'].pop(0))

    for i in range(1,game['players'] + 1):
        game['player ' + str(i)] = []
        game['player ' + str(i)].append(game['deck'].pop(0))
        game['player ' + str(i)].append(game['deck'].pop(0))
        print("Player %s your hand is: %s" % (i, game['player ' + str(i)]))

    print("Dealer is showing: %s" % (game['dealer'][0]))
    return game

def start_game(number_of_decks, number_of_players):
	game = {'deck': shuffle_deck(number_of_decks), 'players': number_of_players} #initialize game with a number of decks shuffled and a number of players
	return game

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

game = start_game(6, 1)
deal(game)


#for i in range(1,game['players'] + 1):
#	decision = input("Player %s will you Hit, Stand or Double ?" % (i))
