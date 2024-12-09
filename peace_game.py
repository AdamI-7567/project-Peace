# Import necessary modules
import random

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Split the deck into two hands
half = len(deck) // 2
player1_hand = deck[:half]
player2_hand = deck[half:]

def card_comparison(p1_card, p2_card):
    if ranks.index(p1_card[0]) > ranks.index(p2_card[0]):
        return 1
    elif ranks.index(p1_card[0]) < ranks.index(p2_card[0]):
        return 2
    else:
        return 0

def play_round(player1_hand, player2_hand):
    if len(player1_hand) == 0 or len(player2_hand) == 0:
        return

    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)

    print(f"Player 1 plays: {p1_card}")
    print(f"Player 2 plays: {p2_card}")

    result = card_comparison(p1_card, p2_card)

    if result == 1:
        print("Round won by Player 1")
        player1_hand.extend([p1_card, p2_card])
    elif result == 2:
        print("Round won by Player 2")
        player2_hand.extend([p1_card, p2_card])
    else:
        print("It's a tie! War!")
        war(player1_hand, player2_hand)

def war(player1_hand, player2_hand):
    if len(player1_hand) < 4 or len(player2_hand) < 4:
        return

    p1_cards = player1_hand[:4]
    p2_cards = player2_hand[:4]

    player1_hand = player1_hand[4:]
    player2_hand = player2_hand[4:]

    print(f"Player 1 puts down: {p1_cards[:-1]}")
    print(f"Player 2 puts down: {p2_cards[:-1]}")
    print(f"Player 1 plays: {p1_cards[-1]}")
    print(f"Player 2 plays: {p2_cards[-1]}")

    result = card_comparison(p1_cards[-1], p2_cards[-1])

    if result == 1:
        print("Player 1 wins the war!")
        player1_hand.extend(p1_cards + p2_cards)
    elif result == 2:
        print("Player 2 wins the war!")
        player2_hand.extend(p1_cards + p2_cards)
    else:
        print("It's a tie again! Each player takes their cards back!")
        player1_hand.extend(p1_cards)
        player2_hand.extend(p2_cards)

def play_game():
    # Create a deck of cards
    deck = [(rank, suit) for rank in ranks for suit in suits]

    # Shuffle the deck
    random.shuffle(deck)

    # Split the deck into two hands
    half = len(deck) // 2
    player1_hand = deck[:half]
    player2_hand = deck[half:]

    while len(player1_hand) != 0 and len(player2_hand) != 0:
        play_round(player1_hand, player2_hand)
        print(f"Player 1 has {len(player1_hand)} cards left.")
        print(f"Player 2 has {len(player2_hand)} cards left.")

    if len(player1_hand) == 0:
        print("Player 2 won the game!")
    elif len(player2_hand) == 0:
        print("Player 1 won the game!")

# Call the main function to start the game
play_game()

