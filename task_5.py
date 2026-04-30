class Game:
    """
    A class representing a basketball game.
    """

    def __init__(self, teams: dict) -> None:
        """
        Initialize the game with team information.

        Args:
            teams (dict): Dictionary with 'command1' and 'command2' keys.
        """
        self.command1: str = teams['command1']
        self.command2: str = teams['command2']
        self.score1: int = 0
        self.score2: int = 0

    def ball_thrown(self, command: int, points: int) -> None:
        """
        Adds points to the specified team.

        Args:
            command (int): Team number (1 or 2)
            points (int): Number of points to add
        """
        if command == 1:
            self.score1 += points
        elif command == 2:
            self.score2 += points

    def get_score(self) -> tuple:
        """
        Returns the current score.

        Returns:
            tuple: (score of team 1, score of team 2)
        """
        return (self.score1, self.score2)

    def get_winner(self) -> str:
        """
        Returns the winner's team name or 'Draw'.

        Returns:
            str: Team name or 'Draw'
        """
        if self.score1 > self.score2:
            return self.command1
        elif self.score2 > self.score1:
            return self.command2
        else:
            return 'ничья'


game_one = Game({'command1' : 'Юта Джаз', 'command2' : 'Майами Хит'})
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
