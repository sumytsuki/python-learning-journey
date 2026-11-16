# Blackjack Game
# Python Mini Projects
# Concepts: Functions, Lists, Loops, Conditionals, Random
# A command-line Blackjack game against a computer dealer.
import random

def deal_card():
    """Return a randomly selected card value."""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck)


def calculate_score(hand):
    """Calculate the score of a hand, adjusting Aces when needed."""

    # A two-card 21 is represented as 0 (Blackjack).
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    # Change an Ace from 11 to 1 if the hand exceeds 21.
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


def compare(player_score, dealer_score):
    """Determine the game result based on the final scores."""

    if player_score == dealer_score:
        return "It's a draw! 🙃"
    elif dealer_score == 0:
        return "Dealer has Blackjack. You lose! 😱"
    elif player_score == 0:
        return "Blackjack! You win! 😎"
    elif player_score > 21:
        return "You went over 21. You lose! 😭"
    elif dealer_score > 21:
        return "Dealer went over 21. You win! 😁"
    elif player_score > dealer_score:
        return "You win! 😃"
    else:
        return "You lose! 😤"


def play_game():
    """Run a single round of Blackjack."""

    player_hand = []
    dealer_hand = []

    player_score = -1
    dealer_score = -1
    game_over = False

    # Deal two starting cards to each participant.
    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    # Player's turn.
    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Your cards: {player_hand} | Score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            choice = input("Draw another card? Type 'y' or 'n': ")

            if choice == "y":
                player_hand.append(deal_card())
            else:
                game_over = True

    # Dealer draws until reaching at least 17.
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    # Display the final hands and game result.
    print(f"\nYour final hand: {player_hand} | Score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand} | Score: {dealer_score}")
    print(compare(player_score, dealer_score))


# Start a new round while the player wants to continue.
while input("Play Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
