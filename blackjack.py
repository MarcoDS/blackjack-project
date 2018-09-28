from random import shuffle

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.completed = False

    def hit(self, card): 
        """Add a card from top of the deck to target hand."""
        self.cards.append(card)
        self.compute_value()

    def compute_value(self):
        """Return numeric value of said hand."""
        self.value = 0
        ace_count = 0
        for r, s in self.cards:
            if r in '2,3,4,5,6,7,8,9':
                self.value += int(r)
            elif r in 'TJQK':
                self.value += 10
            elif r == 'A':
                self.value += 11
                ace_count += 1

        while self.value > 21 and ace_count > 0:
            self.value -= 10
            ace_count -= 1

    def splittable(self):
        ranks = [r for r, s in self.cards]
        return len(set(ranks)) == 1 and len(self.cards) == 2 and list(set(ranks)).count('A') == 0


class Player():
    def __init__(self):
        self.bankroll = 0
        self.hands = [Hand()]

    def split(self, target):
        self.hands.append(Hand())
        new_hand = target + 1
        self.hands[new_hand].hit(self.hands[target].cards.pop(1))
        self.hands[target].hit(game.draw_card())  #is it ok to call draw_card() like this here 
        self.hands[new_hand].hit(game.draw_card())

class Game():
    def __init__(self, number_of_decks, number_of_players):
        self.number_of_decks = number_of_decks
        self.number_of_players = number_of_players
        self.deck = []
        self.players = [Player() for i in range(number_of_players + 1)]  # additional player to account for the dealer

    def deal(self):
        """Set up each round by creating starting hands for dealer and each player."""
        for p in list(range(len(self.players))) * 2:
            self.players[p].hands[0].hit(self.draw_card())

    def draw_card(self):
        return self.deck.pop(0)

    def print_deal(self): 
        """Print initial deal output."""
        for p in range(1, len(self.players)):
            print("Player %s your hand is: %s" % (p, self.players[p].hands[0].cards))

        print("Dealer is showing: %s" % (self.players[0].hands[0].cards[0]))

    def shuffle_deck(self):    
        """Shuffle total deck to create a new one."""
        self.deck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] * self.number_of_decks
        shuffle(self.deck)


print("Welcome to BlackJack.")
print("Everyone starts with 1000$")
print("Bets are fixed at 50$")
print("")

game = Game(6, 4)
game.shuffle_deck()
game.deal()
game.print_deal()
print("...")
print("...")

for p in range(1, len(game.players)):
    print("")
    print("Player %s" % (p))
    hands_resolved = 0
    while hands_resolved < len(game.players[p].hands):
        i = hands_resolved
        if len(game.players[p].hands) > 1:
            print("Hand %s: %s" % ((i+1),game.players[p].hands[i].cards))
        if game.players[p].hands[i].value == 21:
            if len(game.players[p].hands[i].cards) == 2:
                print("!!BLACKJACK!! Congratulations..")
                # Pay player with bonus
            else:
                print("21! Congratulations..")
            hands_resolved += 1
            
        elif game.players[p].hands[i].value > 21:
            print("Oops, that's a bust...")
            hands_resolved += 1
            # Take bet
        else:            
            print("Hand value is %s" % (game.players[p].hands[i].value))
            print("What do you want to do?")
            if game.players[p].hands[i].splittable():
                decision = raw_input("[H]it, [S]tand, S[p]lit [D]ouble: ")
            else:
                decision = raw_input("[H]it, [S]tand or [D]ouble: ")
            decision = decision.lower()
            if decision == 'h':
                game.players[p].hands[i].hit(game.draw_card())
                print("Your current hand is: %s" % (game.players[p].hands[i].cards))
            elif decision == 'd':
                game.players[p].hands[i].hit(game.draw_card())
                print("Your final hand is: %s" % (game.players[p].hands[i].cards))
                # Double bet
                hands_resolved += 1
            elif decision == 's':
                hands_resolved += 1
            elif decision == 'p' and game.players[p].hands[i].splittable():
                game.players[p].split(i)
            else:
                print("Incorrect input")

