"""Play Phase 10 with 2 player"""

def create_deck ():

    # import modules
    import itertools, random

    # make a deck of cards
    deck = list(itertools.product(range(1,12),['Red','Red','Blue','Blue','Yellow','Yellow','Green','Green']))

    # shuffle the cards
    random.shuffle(deck)
    return deck


def deal_cards (player1_hand,player2_hand,deck,discard):
    # draw ten cards for each player
    player1_hand.extend(deal_player_hands (deck))
    player2_hand.extend(deal_player_hands (deck))

    discard.append(deck[0])
    del deck[0]


def deal_player_hands(deck):
    player_hand = []
    for i in range(10):
        player_hand.append([deck[i][0], deck[i][1]])  
    del deck [0:10]
    return player_hand

def is_winner(player_hand):
    return len(player_hand) == 0

def display_players_hand_discard(player_hand,player,discard):
    sort_player_hand(player_hand)
    print "\n Player " + str(player) + " hand: " + str(player_hand)
    print "\n Discard pile: {}".format(discard)

def sort_player_hand(player_hand):
    return player_hand.sort()

def draw_a_card(deck,player_hand,player):
    player_hand.append(deck[0])
    del deck[0]
    sort_player_hand(player_hand)
    display_players_hand_discard(player_hand,player,discard)
    
def decide_to_laydown_or_discard(player_hand,discard):
    input = True
    while input == True:
        user_input = raw_input("\n Would you like to lay down phase (L) or Discard (D)? ").upper()
        if user_input == "L":
            laydown_phase(player_hand)
            discard_from_hand(player_hand,discard)
            input = False
        elif user_input == "D":
            discard_from_hand(player_hand,discard)
            input = False
        else:
            print "incorrect entry"

def pick_up_discard(player_hand,discard,player):
    player_hand.append(discard[0])
    del discard[0]
    sort_player_hand(player_hand)
    display_players_hand_discard(player_hand,player,discard)

def discard_from_hand(player_hand,discard):
    user_input = int(raw_input("Which card index would you like to discard? "))
    discard[0] = player_hand[user_input]
    del player_hand[user_input]

def laydown_phase(player_hand):
    while True:
        card = raw_input("")

def players_turn(player_hand,discard,deck,player):
    display_players_hand_discard(player_hand,player,discard)
    user_input = raw_input("\n Would you like to Draw a card (D) or Pick up from Discard pile (P)? ").upper()
    if user_input == "D":
        draw_a_card(deck,player_hand,player)
    elif user_input == "P":
        pick_up_discard(player_hand,discard,player)

    decide_to_laydown_or_discard(player_hand,discard)

def run_game(player1_hand,player2_hand,deck,discard):
    player = 1
    while True:
        print "\n It is Player {}s turn.".format(player)
        if player == 1:
            players_turn(player1_hand,discard,deck,player)
            player = 2
        else:
            players_turn(player2_hand,discard,deck,player)
            player = 1

"""Start of Game"""
game = raw_input("Would you like to play Phase 10? ").lower()
if game == "yes":
    player1_hand = []
    player2_hand = []
    discard = []
    deck = create_deck()
    deal_cards(player1_hand,player2_hand,deck,discard)
    run_game(player1_hand,player2_hand,deck,discard)

else:
    exit()