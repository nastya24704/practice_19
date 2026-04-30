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


human = NotSleeping('Мистер Смит')
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()

mr_bean = NotSleeping('Мистер Бин', 9)
mr_bean.add_sheep()
mr_bean.add_sheep()
mr_bean.add_sheep()

print(human.name, 'насчитал', human.count_sheeps, 'овец')
print(mr_bean.name, 'насчитал', mr_bean.count_sheeps, 'овец')
