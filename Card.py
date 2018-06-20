import Constants

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getRankForPrint(self):
        return Constants.all_ranks[self.rank]

    def getSuitForPrint(self):
        return Constants.all_suits[self.suit]

    def getSuit(self):
        return self.suit

    def print(self):
        print(str(self.getRankForPrint()) + self.getSuitForPrint())