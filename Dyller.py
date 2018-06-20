import random
from Card import Card
from Combination import Combination

class Dyller:
    def __init__(self):
        self.deck = []

    def shuffleDeck(self):
        for rank in range(0, 13):
            for suit in range(0, 4):
                currentCard = Card(rank, suit)
                self.deck.append(currentCard)

    def getNextCard(self):
        # rewrite random to return not list but one element
        nextCard = random.sample(self.deck, k=1)

        for i, o in enumerate(self.deck):
            if o.getRank() == nextCard[0].getRank() and o.getSuit() == nextCard[0].getSuit():
                del self.deck[i]
                break
        return nextCard

    def getNextCards(self, cards_count):
        cards = []
        for i in range(0, cards_count):
            cards.append(self.getNextCard()[0])
        return cards

    def getSuitsByCardRank(self, rank, card_list):
        suits = []
        for card in card_list:
            if rank == card.rank:
                suits.append(card.suit)
        return suits

    def getStrFlashFromRank(self, card_list, card_rank):  # Шукає СтФ від заданого рангу
        suits_counts = [0, 0, 0, 0]
        for rank in range(card_rank, card_rank + 5):
            suits = self.getSuitsByCardRank(rank, card_list)
            if len(suits) > 0:
                for suit in suits:
                    suits_counts[suit] += 1
        if max(suits_counts) == 5:
            return Combination(8, [card_rank + 4])

    def getRoyalFlash(self, card_list):
        combination = self.getStrFlashFromRank(card_list, 8)
        if combination != None:
            return Combination(9, [12])

    def getHighestStrFlash(self, card_list):
        for i in reversed(range(0, 8)):
            combination = self.getStrFlashFromRank(card_list, i)
            if combination != None:
                return combination

    def getFourKindOf(self, card_list):
        rank_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for card in card_list:
            rank_counts[card.rank] += 1
        if max(rank_counts) == 4:
            index = rank_counts.index(max(rank_counts))
            rank_counts[index] = 0

            for card_rank in reversed(rank_counts):
                if card_rank > 0:
                    rank_counts.reverse()
                    return Combination(7, [index, 12 - rank_counts.index(card_rank)])

    def getFullHouse(self, card_list):
        rank_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for card in card_list:
            rank_counts[card.rank] += 1
        rank_counts.reverse()

        if max(rank_counts) == 3:
            set_index = rank_counts.index(3)
            rank_counts[set_index] = 0
            set_index = 12 - set_index

            if max(rank_counts) >= 2:
                pair_index = 12 - rank_counts.index(max(rank_counts))

                return Combination(6, [set_index, pair_index])

    def getFlash(self, card_list):
        suits_counts = [0, 0, 0, 0]
        for card in card_list:
            suits_counts[card.suit] += 1
        if max(suits_counts) >= 5:
            flash_suit = suits_counts.index(max(suits_counts))
            flash_cards = []
            for card in card_list:
                if card.suit == flash_suit:
                    flash_cards.append(card.rank)
            flash_cards.sort(reverse=True)
            return Combination(5, flash_cards[0:5])

    def getStreight(self, card_list):
        card_rank_list = []
        for card in card_list:
            card_rank_list.append(card.rank)
        card_rank_list.sort(reverse=True)

        counter = 1
        for i in range(1, len(card_rank_list)):
            if card_rank_list[i] + 1 == card_rank_list[i - 1]:
                counter += 1
                if counter == 5:
                    return Combination(4, [card_rank_list[i - 4]])
            else:
                counter = 1

    def getSet(self, card_list):
        rank_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for card in card_list:
            rank_counts[card.rank] += 1
        if max(rank_counts) == 3:
            index = rank_counts.index(3)
            rank_counts[index] = 0

            cards_ranks = [index]
            for card_rank in reversed(rank_counts):
                if card_rank > 0:
                    rank_counts.reverse()
                    kiker = (12 - rank_counts.index(card_rank))
                    cards_ranks.append(kiker)
                    if len(cards_ranks) == 3:
                       return Combination(3, cards_ranks)


    def getTwoPairs(self, card_list):
        card_ranks = []
        for card in card_list:
            card_ranks.append(card.rank)
        card_ranks.sort(reverse=True)
        card_ranks_result = []
        first_pair = None
        second_pair = None
        for i in range(1, len(card_ranks)):
            if card_ranks[i] == card_ranks[i - 1]:
                first_pair = card_ranks[i]
                card_ranks.remove(card_ranks[i - 1])
                card_ranks.remove(card_ranks[i - 1])
                break

        for i in range(1, len(card_ranks)):
            if card_ranks[i] == card_ranks[i - 1]:
                second_pair = card_ranks[i]
                card_ranks.remove(card_ranks[i - 1])
                card_ranks.remove(card_ranks[i - 1])
                break

        if first_pair != None and second_pair != None:
            if first_pair > second_pair:
                card_ranks_result.append(first_pair)
                card_ranks_result.append(second_pair)
            else:
                card_ranks_result.append(second_pair)
                card_ranks_result.append(first_pair)
            card_ranks_result += card_ranks
            return  Combination(2, card_ranks_result[0:3])

    def getPair(self, card_list):
        card_ranks = []
        for card in card_list:
            card_ranks.append(card.rank)
        card_ranks.sort(reverse=True)
        card_ranks_result = []
        for i in range(1, len(card_ranks)):
            if card_ranks[i] == card_ranks[i - 1]:
                card_ranks_result.append(card_ranks[i])
                card_ranks.remove(card_ranks[i - 1])
                card_ranks.remove(card_ranks[i - 1])
                card_ranks_result += card_ranks
                return Combination(1, card_ranks_result[0:5])

    def getKiker(self, card_list):
        card_ranks = []
        for card in card_list:
            card_ranks.append(card.rank)
        card_ranks.sort(reverse=True)
        return Combination(0, card_ranks[0:5])


    # def f(self, player_one_card_list, player_two_card_list):
    #     p1_wins_count = 0
    #     p2_wins_count = 0
    #
    #     for one in self.deck:
    #         print("*****")
    #         for two in self.deck:
    #             print("***")
    #             for three in self.deck:
    #                 print("*")
    #                 for four in self.deck:
    #                     print('.')
    #                     for five in self.deck:
    #                         p1_local_card_list = player_one_card_list
    #                         p1_local_card_list.append(one)
    #                         p1_local_card_list.append(two)
    #                         p1_local_card_list.append(three)
    #                         p1_local_card_list.append(four)
    #                         p1_local_card_list.append(five)
    #                         p1_combination = self.getHighestCombination(p1_local_card_list)
    #
    #                         p2_local_card_list = player_two_card_list
    #                         p2_local_card_list.append(one)
    #                         p2_local_card_list.append(two)
    #                         p2_local_card_list.append(three)
    #                         p2_local_card_list.append(four)
    #                         p2_local_card_list.append(five)
    #                         p2_combination = self.getHighestCombination(p2_local_card_list)
    #
    #                         if p1_combination.compare(p2_combination) == 1:
    #                             p1_wins_count += 1
    #                             #print("p1+")
    #                         elif p1_combination.compare(p2_combination) == -1:
    #                             p2_wins_count +=1
    #                             #print("p2+")
    #
    #
    #     return p1_wins_count / (p1_wins_count + p2_wins_count) * 100




    def getHighestCombination(self, card_list):

        rf = self.getRoyalFlash(card_list)
        if rf != None:
            return rf

        sf = self.getHighestStrFlash(card_list)
        if sf != None:
            return sf

        kare = self.getFourKindOf(card_list)
        if kare != None:
            return kare

        fh = self.getFullHouse(card_list)
        if fh != None:
            return fh

        fl = self.getFlash(card_list)
        if fl != None:
            return fl

        st = self.getStreight(card_list)
        if st != None:
            return st

        set = self.getSet(card_list)
        if set != None:
            return set

        tp = self.getTwoPairs(card_list)
        if tp != None:
            return tp

        kik = self.getKiker(card_list)
        if kik != None:
            return kik

    def __str__(self):
        return (self.card.rank)



