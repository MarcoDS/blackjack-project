from random import shuffle
from time import sleep

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.completed = False
        self.bet = 50
        self.is_blackjack = False
        self.is_busted = False

    def hit(self, card): 
        """Add a card from top of the deck to target hand."""
        self.cards.append(card)
        self.compute_value()
        return card

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

        if self.value == 21 and len(self.cards) == 2:
            self.is_blackjack = True

        if self.value > 21:
            self.is_busted = True

    def splittable(self):
        ranks = [r for r, s in self.cards]
        return len(set(ranks)) == 1 and len(self.cards) == 2 and list(set(ranks)).count('A') == 0


class Player():
    def __init__(self):
        self.bankroll = 1000
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

    def cleanup(self):
        for p in range(len(self.players)):
            self.players[p].hands = [Hand()]

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

    def resolve_dealer(self):
        print("Dealer's hand is: %s for %s" % (self.players[0].hands[0].cards, self.players[0].hands[0].value))
        while self.players[0].hands[0].value < 17:
            print("Dealer hits a %s" % (self.players[0].hands[0].hit(game.draw_card())))
        
        if self.players[0].hands[0].value < 22:
            print("Dealer stays with: %s for %s" % (self.players[0].hands[0].cards, self.players[0].hands[0].value))
        else:
            print("Dealer busts with: %s for %s" % (self.players[0].hands[0].cards, self.players[0].hands[0].value))

    def resolve_bets(self):
        for p in range(1, len(self.players)):
            for i in range(len(self.players[p].hands)):
                if self.players[p].hands[i].is_busted:
                    self.players[p].bankroll -= self.players[p].hands[i].bet 
                    print("Player %s busted at %s. Loses %s$, total at %s$" % (p, self.players[p].hands[i].value, self.players[p].hands[i].bet, self.players[p].bankroll))
                elif self.players[p].hands[i].value > self.players[0].hands[0].value or self.players[0].hands[0].is_busted:
                    if self.players[p].hands[i].is_blackjack:
                       self.players[p].hands[i].bet += int(self.players[p].hands[i].bet * 0.5)                
                    self.players[p].bankroll += self.players[p].hands[i].bet
                    print("Player %s wins at %s. Receives %s$, total at %s$" % (p, self.players[p].hands[i].value, self.players[p].hands[i].bet, self.players[p].bankroll))
                elif self.players[p].hands[i].value == self.players[0].hands[0].value:
                    print("Player %s pushes at %s. Receives back initial bet, total at %s$" % (p, self.players[p].hands[i].value, self.players[p].bankroll))
                else:  # Neither busted, dealer has better hand
                    self.players[p].bankroll -= self.players[p].hands[i].bet
                    print("Player %s lost at %s. Loses %s$, total at %s$" % (p, self.players[p].hands[i].value, self.players[p].hands[i].bet, self.players[p].bankroll))


print("Welcome to BlackJack.")
print("Everyone starts with 1000$")
print("Bets are fixed at 50$")
print("")
sleep(1)

number_of_players = 0

while number_of_players < 1 or number_of_players > 8:
    try:
        number_of_players = int(input("How many players 1-8? "))
    except:
        print("Incorrect input")
        continue
    if number_of_players < 1 or number_of_players > 8:
        print("Incorrect input")

game = Game(6, number_of_players)

sleep(0.5)
print("")
print("")
print("Shuffling...")
game.shuffle_deck()
print("")
print("")
playing = True
while playing == True:
    print("Dealing...")
    game.deal()
    print("")
    print("")
    sleep(1)
    game.print_deal()

    for p in range(1, len(game.players)):
        print("")
        print("")
        print("Player %s" % (p))
        print("")
        hands_resolved = 0
        while hands_resolved < len(game.players[p].hands):
            i = hands_resolved
            if len(game.players[p].hands) > 1:
                print("Hand %s: %s" % ((i+1),game.players[p].hands[i].cards))

            if game.players[p].hands[i].is_blackjack:
                print("!!BLACKJACK!! Congratulations..")
                hands_resolved +=1

            elif game.players[p].hands[i].value == 21:
                print("21! Congratulations..")
                hands_resolved += 1
                
            elif game.players[p].hands[i].is_busted:
                print("Oops, that's a bust...")
                hands_resolved += 1
                # Take bet
            else:            
                print("Hand value is %s" % (game.players[p].hands[i].value))
                print("")
                print("What do you want to do?")
                if game.players[p].hands[i].splittable() and len(game.players[p].hands[i].cards) == 2:
                    decision = input("[H]it, [S]tand, S[p]lit [D]ouble: ")
                elif len(game.players[p].hands[i].cards) == 2:
                    decision = input("[H]it, [S]tand or [D]ouble: ")
                else:
                    decision = input("[H]it or [S]tand: ")
                decision = decision.lower()

                if decision == 'h':  # Hit
                    game.players[p].hands[i].hit(game.draw_card())
                    print("Your current hand is: %s" % (game.players[p].hands[i].cards))

                elif decision == 'd' and len(game.players[p].hands[i].cards) == 2:  # Double
                    game.players[p].hands[i].hit(game.draw_card())
                    game.players[p].hands[i].bet *= 2
                    print("Your final hand is: %s" % (game.players[p].hands[i].cards))
                    hands_resolved += 1

                elif decision == 's':  # Stand
                    hands_resolved += 1

                elif decision == 'p' and game.players[p].hands[i].splittable():   # Split
                    game.players[p].split(i)
                else:
                    print("Incorrect input")
    print("")
    print("")
    sleep(0.5)
    print("All players are done.")
    print("Time for the dealer")
    print("")
    print("")
    sleep(1)
    game.resolve_dealer()
    print("")
    print("")
    sleep(1)
    game.resolve_bets()
    print("")
    print("")

    keep_playing = input("Type 'quit' to stop playing, anything else to keep going:")
    keep_playing = keep_playing.lower()
    if keep_playing == "quit":
        print("Thanks for playing.")
        playing = False
    game.cleanup()

