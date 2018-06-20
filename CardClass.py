from Dyller import Dyller
from Card import Card

dyller = Dyller()
dyller.shuffleDeck()


p1_cards = dyller.getNextCards(2)
p2_cards = dyller.getNextCards(2)
table_cards = dyller.getNextCards(5)

first_ready_hand = p1_cards + table_cards
second_ready_hand = p2_cards + table_cards

print("first player cards:")
for card in p1_cards:
    card.print()

print("second player cards:")
for card in p2_cards:
    card.print()

print("table cards")
for card in table_cards:
    card.print()

first_player_combination = dyller.getHighestCombination(first_ready_hand)
second_player_combination = dyller.getHighestCombination(second_ready_hand)

if (first_player_combination.compare(second_player_combination)) == 1:
    print('first player won')
elif (first_player_combination.compare(second_player_combination)) == -1:
    print('second player won')
else:
    print('a draw')

