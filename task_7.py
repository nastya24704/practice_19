class TrafficLight:
    """
    A class representing a traffic light.
    """
    permissible_values = ['зеленый', 'желтый', 'красный', 'желтый']

    def __init__(self):
        """
        Initialize the traffic light with a green signal.
        """
        self.current_signal = 'зеленый'
        self._index = 0

    def next_signal(self):
        """
        Switch to the next signal.
        """
        self._index = (self._index + 1) % len(self.permissible_values)
        self.current_signal = self.permissible_values[self._index]


seven_roads = TrafficLight()
print(seven_roads.current_signal)
for _ in range(5):
    seven_roads.next_signal()
print(seven_roads.current_signal)
