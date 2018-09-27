from random import shuffle

class Player():
    def __init__(self):
        self.hand = []
        self.hand_value = 0

    def compute_value(self):
        """Return numeric value of said hand."""
        self.hand_value = 0
        ace_count = 0
        for r, s in self.hand:
            if r in '2,3,4,5,6,7,8,9':
                self.hand_value += int(r)
            elif r in 'TJQK':
                self.hand_value += 10
            elif r == 'A':
                self.hand_value += 11
                ace_count += 1

        while self.hand_value > 21 and ace_count > 0:
            self.hand_value -= 10
            ace_count -= 1
        


    def hit(self, card): 
        """Add a card from top of the deck to target hand."""
        self.hand.append(card)
        self.compute_value()

class Game():
    def __init__(self, number_of_decks, number_of_players):
        self.number_of_decks = number_of_decks
        self.number_of_players = number_of_players
        self.deck = []
        self.players = [Player() for i in range(number_of_players + 1)]  # additional player to account for the dealer

    def deal(self):
        """Set up each round by creating starting hands for dealer and each player."""
        for p in list(range(len(self.players))) * 2:
            self.players[p].hit(self.deck.pop(0))

    def print_deal(self): 
        """Print initial deal output."""
        for p in range(1, len(self.players)):
            print("Player %s your hand is: %s" % (p, self.players[p].hand))

        print("Dealer is showing: %s" % (self.players[0].hand))

    def shuffle_deck(self):    
        """Shuffle total deck to create a new one."""
        self.deck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] * self.number_of_decks
        shuffle(self.deck)

print("Welcome to BlackJack.")
print("Everyone starts with 1000$")
print("Bets are fixed at 50$")
print("")

game = Game(6, 1)
game.shuffle_deck()
game.deal()
game.print_deal()


