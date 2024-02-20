import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

#=================================================================================
class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

#=================================================================================
class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card = Card(suit,rank)

                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):
        # Remove one card from the list of all_cards
        return self.all_cards.pop()

#=================================================================================

class Player:

    def __init__(self,name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        # Remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List pf multiple cards
            self.all_cards.extend(new_cards)

        else:
            # For a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)}"

#=================================================================================

player_one = Player("one")
player_two = Player("two")

new_deck = Deck()
new_deck.shuffle()


for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


game_on = True

round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One is out of cards! Player Two wins!")
        game_on = False
        break

    elif len(player_two.all_cards) == 0:
        print("Player Two is out of cards! Player One wins!")
        game_on = False
        break

    # START A NEW ROUND
    player_one_cards = [player_one.remove_one()]

    player_two_cards = [player_two.remove_one()]

    # WHILE IN BATTLE

    in_battle = True

    while in_battle:
        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            in_battle = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            in_battle = False

        else:
            print("BATTLE!")

            # Occurs when the cards are equal.
            # The players take another card each and continue the current war.

            # First check to see if player has enough cards

            # Check to see if a player is out of cards:

            if len(player_one.all_cards) < 5:
                print("Player One unable to wage battle")
                print("PLAYER TWO WINS")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to wage battle")
                print("PLAYER ONE WINS")
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
