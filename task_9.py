class StrandsDNA:
    """
    A class for storing DNA strands.
    """

    def __init__(self) -> None:
        """Initialize an empty list of DNA strands."""
        self.all_strands = []

    def add_strands(self, strands: str) -> None:
        """
        Add DNA strands from a space-separated string.

        Args:
            strands: String containing DNA strands separated by spaces.
        """
        new_strands = strands.split()
        self.all_strands.extend(new_strands)

    def get_max_strands(self) -> str:
        """
        Return a string containing the longest unique DNA strands in alphabetical order.

        Returns:
            Space-separated string of the longest strands, or empty string if no strands.
        """
        if not self.all_strands:
            return ""

        max_len = max(len(s) for s in self.all_strands)
        max_strands = [s for s in self.all_strands if len(s) == max_len]
        unique_strands = sorted(set(max_strands))
        return ' '.join(unique_strands)

    def __str__(self) -> str:
        """
        Return all DNA strands as a space-separated string.
        """
        return ' '.join(self.all_strands)


covid_19 = StrandsDNA()
covid_19.add_strands('GAAT ACCGTT TTGAC TGGGAC')
print(covid_19)
covid_19.add_strands('ACCT AGGCT TGGGAC')
covid_19.add_strands('CATTTT TAATTC')
print(covid_19)
print(covid_19.get_max_strands())
