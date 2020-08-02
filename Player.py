import abc

class AbstractPlayer(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractclassmethod
    def ask_card(self):
        pass





class Player(AbstractPlayer):
    pass


class Dealer(AbstractPlayer):
    pass

class Bot(AbstractPlayer):
    pass



