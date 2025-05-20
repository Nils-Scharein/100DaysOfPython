import random
from art import logo

#Start Variablen
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = [random.choice(cards)]
player_hand = [random.choice(cards), random.choice(cards)]


def deal_cards(hand):
    random_card = random.choice(cards)
    if random_card == 11:
        if sum(hand) + 11 > 21:
            hand.append(1)
        else:
            hand.append(11)
    else:
        hand.append(random_card)
    return hand

def create_dealer_hand(hand):
    deal_cards(hand)
    if sum(hand) < 17:
        deal_cards(hand)
        return hand
    else:
        return hand

def ask_y_n(question):
    while True:
        q = input(question).lower()
        if q == "y":
            return True
        elif q == "n":
            return False
        else:
            print("Pls select y for yes or n for no")


def main(player_hand, dealer_hand):
    if ask_y_n("Do you Want to play Black Jack?"):
        print(logo)
        print(f"Dealer Hand: {dealer_hand} = {sum(dealer_hand)}")
        print(f"Your Hand: {player_hand} = {sum(player_hand)}")
        dealer_hand = create_dealer_hand(dealer_hand)
        while True:
            if ask_y_n("Do you want another card?") == True:
                deal_cards(player_hand)
                print(f"Your Hand: {player_hand} = {sum(player_hand)}")
                if sum(player_hand) > 21:
                    break
            else:
                break
        if sum(player_hand) > 21:
            print(f"You lost to a break. Your Hand {sum(player_hand)}")
        if sum(dealer_hand) > 21:
            print(f"You won. The Dealer had a Break. {sum(dealer_hand)}.")
        if sum(player_hand) > sum(dealer_hand):
            print(f"You won. Yours {sum(player_hand)} Dealer {sum(dealer_hand)}.")
        if sum(dealer_hand) > sum(player_hand) and sum(dealer_hand) <= 21:
            print(f"You won. Yours {sum(player_hand)} Dealer {sum(dealer_hand)}.")
    else:
        print("Schade")

main(player_hand, dealer_hand)

