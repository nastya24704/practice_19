class Dog:
    """
    A class representing a dog.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a dog with a name.

        Args:
            name (str): The dog's name.
        """
        self.name: str = name

    def say(self) -> None:
        """Prints the sound the dog makes."""
        print("Гав!")

    def __str__(self) -> str:
        """Returns the dog's name when printed."""
        return self.name
