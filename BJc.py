import random
playerIn = True
dealerIn = True

deck_count = input("How many Deck of Cards? ")

# deck of cards / player dealer hand
deck = (['A'] * 4 + (list(range(2, 10)) * 4)+ [10] * 16) * int(deck_count)

playerHand = []
dealerHand = []

# deal the cards
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# calculate the total of each hand
def total(turn):
    total = 0
    face = ['J', 'Q', 'K']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

# check for winner
def revealdealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

# game loop
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

while playerIn or dealerIn:
    print(f"Dealer [{revealdealerHand()}]")
    print(f"Player {playerHand} = {total(playerHand)}")
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn = False
    else:
        dealCard(playerHand)
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break

if total(playerHand) == 21:
    print(f"\nPlayer {playerHand} = {total(playerHand)}\nDealer {dealerHand} = {total(dealerHand)}\nBlackJack! Player Wins!")
elif total(dealerHand) == 21:
    print(f"\nPlayer {playerHand} = {total(playerHand)}\nDealer {dealerHand} = {total(dealerHand)}\nBlackjack! Dealer wins!")
elif total(playerHand) > 21:
    print(f"\nPlayer {playerHand} = {total(playerHand)}\nDealer {dealerHand} = {total(dealerHand)}\nPlayer bust! Dealer wins!")
elif total(dealerHand) > 21:
    print(f"\nPlayer {playerHand} = {total(playerHand)}\nDealer {dealerHand} = {total(dealerHand)}\nDealer busts! Player wins!")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"\nPlayer {playerHand} = {total(playerHand)}\nDealer {dealerHand} = {total(dealerHand)}\nDealer Wins!")
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f"\nPlayer {playerHand} = {total(playerHand)}\nDealer {dealerHand} = {total(dealerHand)}\nPlayer Wins!")