import random


def hit_card():
    """Return a random card from deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    Return cards score: if first hand cards are black jack then returns 0,
    else if Ace in cards and total sum is over than 21 then count 1 for Ace,
    else return actual cards sum result
    """
    if sum(cards) == 21 and len(cards) == 2:  # Black Jack
        return 0
    if sum(cards) > 21 and 11 in cards:  # Ace could be 1 & 11
        cards.remove(11)
        cards.append(1)
    score = sum(cards)
    return score


def winner_judgment(user_score, dealer_score):
    """
    Final winner judgement
    """
    if user_score == 0:
        return "You got Black Jack!"
    elif dealer_score == 0:
        return "Dealer got Black Jack! You lose."
    elif user_score > 21:
        return "You got Bust, You lose."
    elif dealer_score > 21:
        return "Dealer got Bust, You win."
    elif user_score == dealer_score:
        return "Draw 🙃"
    elif user_score > dealer_score:
        return "You win."
    else:
        return "You lose."


def clear():
    """Clear screen."""
    import os

    return os.system("cls")


def black_jack():
    """Black Jack game play"""

    wanna_play = input("Do you want to play BlackJack Games? type 'y' or 'n': ").lower()

    if wanna_play == "n":
        return None

    clear()
    user_cards = []
    dealer_cards = []
    should_continue = True

    for _ in range(2):
        user_cards.append(hit_card())
        dealer_cards.append(hit_card())

    while should_continue:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"\tdealer's first card: {dealer_cards[0]}")

        if user_score > 21 or user_score == 0 or dealer_score == 0:
            should_continue = False
        else:
            hit_or_stand = input("Type 'y' to hit, type 'n' to stand: ").lower()
            if hit_or_stand == "y":
                user_cards.append(hit_card())
            else:
                should_continue = False

    while dealer_score != 17 and dealer_score < 17:
        dealer_cards.append(hit_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"\tYour final cards: {user_cards}, final score: {user_score}")
    print(f"\tdealer's final card: {dealer_cards}, final score: {dealer_score}")
    print(winner_judgment(user_score, dealer_score))

    black_jack()


if __name__ == "__main__":
    black_jack()
