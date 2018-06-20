from collections import Counter
import random
import CardClass

main_list = [i for i in range(1, 53)]
def best_combinations(some_list):

    main_list = [i for i in range(1, 53)]

    priroritet_dict = {'A': 1, 'K': 2, 'Q': 3, 'J': 4, '10': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11,
                       '3': 12, '2': 13}

    cards_value = {1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8', 8: '9', 9: '10', 10: 'J', 11: 'Q', 12: 'K',
                   13: 'A',
                   14: '2', 15: '3', 16: '4', 17: '5', 18: '6', 19: '7', 20: '8', 21: '9', 22: '10', 23: 'J', 24: 'Q',
                   25: 'K', 26: 'A',
                   27: '2', 28: '3', 29: '4', 30: '5', 31: '6', 32: '7', 33: '8', 34: '9', 35: '10', 36: 'J', 37: 'Q',
                   38: 'K', 39: 'A',
                   40: '2', 41: '3', 42: '4', 43: '5', 44: '6', 45: '7', 46: '8', 47: '9', 48: '10', 49: 'J', 50: 'Q',
                   51: 'K', 52: 'A'}

    cards_suit = {1: 'c', 2: 'c', 3: 'c', 4: 'c', 5: 'c', 6: 'c', 7: 'c', 8: 'c', 9: 'c', 10: 'c', 11: 'c', 12: 'c',
                  13: 'c',
                  14: 'd', 15: 'd', 16: 'd', 17: 'd', 18: 'd', 19: 'd', 20: 'd', 21: 'd', 22: 'd', 23: 'd', 24: 'd',
                  25: 'd', 26: 'd',
                  27: 's', 28: 's', 29: 's', 30: 's', 31: 's', 32: 's', 33: 's', 34: 's', 35: 's', 36: 's', 37: 's',
                  38: 's', 39: 's',
                  40: 'h', 41: 'h', 42: 'h', 43: 'h', 44: 'h', 45: 'h', 46: 'h', 47: 'h', 48: 'h', 49: 'h', 50: 'h',
                  51: 'h', 52: 'h'}

    dict_of_suit = []
    dict_of_value = []

    for i in some_list:  # Додаємо 2 словники, 1 з кількістю мастей, яка повторюється і ще одни з картами які повторюються
        print(cards_suit[i], cards_value[i])
        dict_of_suit.append(cards_suit[i])
        dict_of_value.append(cards_value[i])
        main_list.remove(i)  # видаляємо елементи з головного списку

    dict_of_suit = dict(Counter(dict_of_suit))  # Створюємо словники з значеннями які повторюються
    dict_of_value = dict(Counter(dict_of_value))
    print(dict_of_suit, dict_of_value)


    for i in dict_of_suit.keys():  #ROYAL FLASH
        if dict_of_suit[i] == 5:
            rf = 'yes'
    if ('10' in dict_of_value.keys() and 'J' in dict_of_value.keys() and 'Q' in dict_of_value.keys()
        and 'K' in dict_of_value.keys() and 'A' in dict_of_value.keys() and rf == 'yes'):
        print('royal flash')

    for i in dict_of_suit.keys():  #strit FLASH
        if dict_of_suit[i] == 5:
            sf = 'yes'
    if ('9' in dict_of_value.keys() and '10' in dict_of_value.keys() and 'J' in dict_of_value.keys()
            and 'Q' in dict_of_value.keys() and 'K' in dict_of_value.keys() and sf == 'yes') :
        print('strit ff 9 - K')
    elif ('8' in dict_of_value.keys() and '9' in dict_of_value.keys() and '10' in dict_of_value.keys()
            and 'J' in dict_of_value.keys() and 'Q' in dict_of_value.keys() and sf == 'yes') :
        print('strit ff 8 - Q')
    elif ('7' in dict_of_value.keys() and '8' in dict_of_value.keys() and '9' in dict_of_value.keys()
          and '10' in dict_of_value.keys() and 'J' in dict_of_value.keys() and sf == 'yes'):
        print('strit ff 7 - J')
    elif ('6' in dict_of_value.keys() and '7' in dict_of_value.keys() and '8' in dict_of_value.keys()
          and '9' in dict_of_value.keys() and '10' in dict_of_value.keys() and sf == 'yes'):
        print('strit ff 6 - 10')
    elif ('5' in dict_of_value.keys() and '6' in dict_of_value.keys() and '7' in dict_of_value.keys()
            and '8' in dict_of_value.keys() and '9' in dict_of_value.keys() and sf == 'yes'):
        print('strit ff 5 - 9')
    elif ('4' in dict_of_value.keys() and '5' in dict_of_value.keys() and '6' in dict_of_value.keys()
          and '7' in dict_of_value.keys() and '8' in dict_of_value.keys() and sf == 'yes'):
        print('strit ff 4 - 8')
    elif ('3' in dict_of_value.keys() and '4' in dict_of_value.keys() and '5' in dict_of_value.keys()
          and '6' in dict_of_value.keys() and '7' in dict_of_value.keys() and sf == 'yes'):
        print('strit ff 3 - 7')
    elif ('2' in dict_of_value.keys() and '3' in dict_of_value.keys() and '4' in dict_of_value.keys()
          and '5' in dict_of_value.keys() and '6' in dict_of_value.keys() and sf == 'yes'):
        print('strit  ff 2 - 6')
    elif ('A' in dict_of_value.keys() and '2' in dict_of_value.keys() and '3' in dict_of_value.keys()
          and '4' in dict_of_value.keys() and '5' in dict_of_value.keys() and sf == 'yes'):
        print('strit ff A - 5')

    for i in dict_of_value.keys():  # kare
        if dict_of_value[i] == 4:
            print('4 of ', i)

    gg = []
    d = ''
    for i in dict_of_value.keys():  # full Доробити якщо є 2 різні пари який фул старший
         if dict_of_value[i] == 3:
             gg = i
             d = 's'
         if dict_of_value[i] == 2 and d == 's':
             gg2 = i
             print('fool of', gg, 'and', gg2)

    for i in dict_of_suit.keys():  # FLASH
        if dict_of_suit[i] == 5:
            print('flash', i)


    if '10' in dict_of_value.keys() and 'J' in dict_of_value.keys() and 'Q' in dict_of_value.keys() and 'K' in dict_of_value.keys() and 'A' in dict_of_value.keys():
        print('strit 10 - A')
    elif '9' in dict_of_value.keys() and '10' in dict_of_value.keys() and 'J' in dict_of_value.keys() and 'Q' in dict_of_value.keys() and 'K' in dict_of_value.keys():
        print('strit 9 - K')
    elif '8' in dict_of_value.keys() and '9' in dict_of_value.keys() and '10' in dict_of_value.keys() and 'J' in dict_of_value.keys() and 'Q' in dict_of_value.keys():
        print('strit 8 - Q')
    elif '7' in dict_of_value.keys() and '8' in dict_of_value.keys() and '9' in dict_of_value.keys() and '10' in dict_of_value.keys() and 'J' in dict_of_value.keys():
        print('strit 7 - J')
    elif '6' in dict_of_value.keys() and '7' in dict_of_value.keys() and '8' in dict_of_value.keys() and '9' in dict_of_value.keys() and '10' in dict_of_value.keys():
        print('strit 6 - 10')
    elif '5' in dict_of_value.keys() and '6' in dict_of_value.keys() and '7' in dict_of_value.keys() and '8' in dict_of_value.keys() and '9' in dict_of_value.keys():
        print('strit 6 - 10')
    elif '4' in dict_of_value.keys() and '5' in dict_of_value.keys() and '6' in dict_of_value.keys() and '7' in dict_of_value.keys() and '8' in dict_of_value.keys():
        print('strit 4 - 8')
    elif '3' in dict_of_value.keys() and '4' in dict_of_value.keys() and '5' in dict_of_value.keys() and '6' in dict_of_value.keys() and '7' in dict_of_value.keys():
        print('strit 3 - 7')
    elif '2' in dict_of_value.keys() and '3' in dict_of_value.keys() and '4' in dict_of_value.keys() and '5' in dict_of_value.keys() and '6' in dict_of_value.keys():
        print('strit 2 - 6')
    elif 'A' in dict_of_value.keys() and '2' in dict_of_value.keys() and '3' in dict_of_value.keys() and '4' in dict_of_value.keys() and '5' in dict_of_value.keys():  # Srit+
        print('strit A - 5')


    for i in dict_of_value.keys():  # set+
        if dict_of_value[i] == 3:
            print('set of', i)

    tp = []
    for i in dict_of_value.keys():  # two pair+
        if dict_of_value[i] == 2:
            tp.append(i)
            if len(tp) > 1:
                print('two pair of', tp)

    for i in dict_of_value.keys():  # pare+
        if dict_of_value[i] == 2:
            print('pair of ', i)


h1 = best_combinations((random.sample(main_list, k=10)))

examample1 = CardClass.Card(7, 'g')

#print(examample1.getRank())


