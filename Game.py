from Player import Bot



class Game:
    def __init__(self):
        self.players = []
        self.player = None
        self.dealer = None
        self.all_players_count = 1


    @staticmethod
    def _ask_starting(self):
        while True:
            choice  = input('Wanna play (y/n)')
            if choice == 'n':
                exit(1)
            elif choice =='y':
                return True


    def start_game(self):
        self._ask_starting()

        bot_count = int(input('Hello, wrire bots count!'))
        self.all_players_count = bot_count +1
        for _ in range(bot_count):
            b = Bot()
            self.players.append(b)


