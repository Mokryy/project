import random
from collections import Counter

a = [i for i in range(1, 53)]

cards_value = {1:'2', 2:'3', 3:'4', 4:'5',5:'6', 6:'7',7:'8', 8:'9',9:'10', 10:'J',11:'Q', 12:'K', 13:'A',
         14: '2', 15: '3', 16: '4', 17: '5', 18: '6', 19: '7', 20: '8', 21: '9',22: '10', 23: 'J', 24: 'Q', 25: 'K', 26: 'A',
         27: '2', 28: '3', 29: '4', 30: '5', 31: '6', 32: '7',33: '8', 34: '9', 35: '10', 36: 'J', 37: 'Q', 38: 'K', 39: 'A',
         40: '2', 41: '3', 42: '4', 43: '5', 44: '6', 45: '7', 46: '8', 47: '9', 48: '10', 49: 'J', 50: 'Q', 51: 'K', 52: 'A'}

cards_suit = {1:'c', 2:'c', 3:'c', 4:'c',5:'c', 6:'c',7:'c', 8:'c',9:'c', 10:'c',11:'c', 12:'c', 13:'c',
         14: 'd', 15: 'd', 16: 'd', 17: 'd', 18: 'd', 19: 'd', 20: 'd', 21: 'd',22: 'd', 23: 'd', 24: 'd', 25: 'd', 26: 'd',
         27: 's', 28: 's', 29: 's', 30: 's', 31: 's', 32: 's',33: 's', 34: 's', 35: 's', 36: 's', 37: 's', 38: 's', 39: 's',
         40: 'h', 41: 'h', 42: 'h', 43: 'h', 44: 'h', 45: 'h', 46: 'h', 47: 'h', 48: 'h', 49: 'h', 50: 'h', 51: 'h', 52: 'h'}

first_hand = (random.sample(a, k=2))
for i in first_hand:
    print(cards_value[i], cards_suit[i])
    a.remove(i)
print('-------------')

second_hand = (random.sample(a, k=2))
for i in second_hand:
    print(cards_value[i], cards_suit[i])
    a.remove(i)
print('-------------')

table_cards = (random.sample(a, k=5))
for i in table_cards:
    print(cards_value[i], cards_suit[i])
    a.remove(i)
print(table_cards)


firt_ready_hand = first_hand + table_cards
print(firt_ready_hand)


f = []
ff = []
for i in firt_ready_hand:
    f.append(cards_suit[i])
    ff.append(cards_value[i])

cards_suit = dict(Counter(f))
cards_value = dict(Counter(ff))
print(cards_suit, cards_value)


for i in cards_suit.keys(): #FLASH
    if cards_suit[i] == 5:
        print('flash', i)
#---------------------------------------------



for i in cards_value.keys(): #kare
    if cards_value[i] == 4:
        print('4 of ', i)
#----------------------------------------



for i in cards_value.keys(): #pare
    if cards_value[i] == 2:
        print('pair of ', i)
#----------------------------------------

for i in cards_value.keys(): #two pair
    if cards_value[i] == 2:
        gg = i
        d = 's'
    if cards_value[i] == 2 and d =='s':
        gg2 = i
        print('two pair of', gg, 'and', gg2)

for i in cards_value.keys(): #set
    if cards_value[i] == 3:
        print('set of', i)

gg = ''
gg2 = ''
d = ''
for i in cards_value.keys(): #full Доробити якщо є 2 різні пари який фул старший
    if cards_value[i] == 3:
        gg = i
        d = 's'
    if cards_value[i] == 2 and d =='s':
        gg2 = i
        print('fool of', gg, 'and', gg2)

if 'A' in cards_value.keys() and '2' in cards_value.keys() and '3' in cards_value.keys() and '4' in cards_value.keys() and '5' in cards_value.keys(): #Srit
    print('strit A - 5')
elif '2' in cards_value.keys() and '3' in cards_value.keys() and '4' in cards_value.keys() and '5' in cards_value.keys() and '6' in cards_value.keys():
    print('strit 2 - 6')
elif '3' in cards_value.keys() and '4' in cards_value.keys() and '5' in cards_value.keys() and '6' in cards_value.keys() and '7' in cards_value.keys():
    print('strit 3 - 7')
elif '4' in cards_value.keys() and '5' in cards_value.keys() and '6' in cards_value.keys() and '7' in cards_value.keys() and '8' in cards_value.keys():
    print('strit 4 - 8')
elif '5' in cards_value.keys() and '6' in cards_value.keys() and '7' in cards_value.keys() and '8' in cards_value.keys() and '9' in cards_value.keys():
    print('strit 5 - 9')
elif '6' in cards_value.keys() and '7' in cards_value.keys() and '8' in cards_value.keys() and '9' in cards_value.keys() and '10' in cards_value.keys():
    print('strit 6 - 10')
elif '7' in cards_value.keys() and '8' in cards_value.keys() and '9' in cards_value.keys() and '10' in cards_value.keys() and 'J' in cards_value.keys():
    print('strit 7 - J')
elif '8' in cards_value.keys() and '9' in cards_value.keys() and '10' in cards_value.keys() and 'J' in cards_value.keys() and 'Q' in cards_value.keys():
    print('strit 8 - Q')
elif '9' in cards_value.keys() and '10' in cards_value.keys() and 'J' in cards_value.keys() and 'Q' in cards_value.keys() and 'K' in cards_value.keys():
    print('strit 9 - K')
elif '10' in cards_value.keys() and 'J' in cards_value.keys() and 'Q' in cards_value.keys() and 'K' in cards_value.keys() and 'A' in cards_value.keys():
    print('strit 10 - A')
