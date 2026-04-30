class Game:
    """
    A class representing a basketball game.
    """

    def __init__(self, teams):
        self.command1 = teams['command1']
        self.command2 = teams['command2']
        self.score1 = 0
        self.score2 = 0

    def ball_thrown(self, command, points):
        if command == 1:
            self.score1 += points
        elif command == 2:
            self.score2 += points

    def get_score(self):
        return (self.score1, self.score2)

    def get_winner(self):
        if self.score1 > self.score2:
            return self.command1
        elif self.score2 > self.score1:
            return self.command2
        else:
            return 'ничья'


game_one = Game({'command1': 'Юта Джаз', 'command2': 'Майами Хит'})
game_one.ball_thrown(1, 2)
game_one.ball_thrown(1, 3)
game_one.ball_thrown(2, 2)
game_one.ball_thrown(1, 1)
print(game_one.get_score())
game_one.ball_thrown(2, 3)
game_one.ball_thrown(2, 2)
game_one.ball_thrown(1, 2)
print(game_one.get_score())
print(game_one.get_winner())
