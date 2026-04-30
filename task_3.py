class NotSleeping:
    """
    A class representing a person who counts sheep to fall asleep.
    """

    def __init__(self, name: str, count_sheeps: int = 0) -> None:
        """
        Initialize a person with a name and an optional starting number of sheep.

        Args:
            name (str): The person's name.
            count_sheeps (int): The initial number of sheep counted (default is 0).
        """
        self.name = name
        self.count_sheeps = count_sheeps

    def add_sheep(self) -> None:
        """
        Increases the number of counted sheep by 1.
        """
        self.count_sheeps += 1

    def lost(self) -> None:
        """
        Resets the sheep count to 0 (the person lost count and starts over).
        """
        self.count_sheeps = 0

    def get_count_sheeps(self) -> int:
        """
        Returns the current number of counted sheep.

        Returns:
            int: The number of sheep counted.
        """
        return self.count_sheeps


human = NotSleeping('Мистер Смит')
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()
print(human.name, 'насчитал', human.count_sheeps, 'овец')
human.add_sheep()
human.lost()
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()
print(human.name, 'насчитал', human.get_count_sheeps(), 'овец')
