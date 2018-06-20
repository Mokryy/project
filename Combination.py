import Constants

class Combination:

    def __init__(self, rank, cards_ranks):
        self.rank = rank
        self.cards_ranks = cards_ranks

    def compare(self, another_combination):

        if self.rank > another_combination.rank:
            return 1
        elif self.rank < another_combination.rank:
            return -1
        else:
            for i in range(0, len(self.cards_ranks)):
                if self.cards_ranks[i] > another_combination.cards_ranks[i]:
                    return 1
                elif self.cards_ranks[i] < another_combination.cards_ranks[i]:
                    return -1
            return 0

    def getCombinationForPrint(self):
        return Constants.all_combinations[self.rank]

