from random import shuffle

number_of_decks = 6
number_of_players = 2

def shuffle_deck(n):    
    initial_deck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] * n
    shuffle(initial_deck)
    return initial_deck

#suits = [s for r,s in mydeck] 
#ranks = [r for r,s in mydeck] 

def initial_deal(game):
    game['dealer'] = []
    game['dealer'].append(game['deck'].pop(0))
    game['dealer'].append(game['deck'].pop(0))

    for i in range(1,game['players'] + 1):
        game['player ' + str(i)] = []
        game['player ' + str(i)].append(game['deck'].pop(0))
        game['player ' + str(i)].append(game['deck'].pop(0))

    return game


game = {'deck': shuffle_deck(number_of_decks), 'players': number_of_players} #initialize game with a number of decks shuffled and a number of players



initial_deal(game)
