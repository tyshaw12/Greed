from game.casting.actor import Actor
from game.shared.point import Point
import random
class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a value of itself.

    Attributes:
        _value (string): The value of the artifact.
    """
    def __init__(self):
        super().__init__()
        self._value = 1
    
    def get_value(self):
        """Gets the artifact value.
        
        Returns:
            value: the artifact value.
        """
        
        return self._value
    
    def set_value(self, value):
        """Set artifact worth to the given value.
        Args:
            points: The value of the rock or gem.
        """
            
        self._value = value
        
    def rain(self, max_y):
        """ Moves the gems and rocks according to the velocity, you can make it really fast and it looks funny because of the FRAME_RATE.
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = self._position.get_x()
        y = (self._position.get_y() + 1) % max_y
        self._position = Point(x, y)

    def change_x(self):
        x = random.randint(1, 59) * 15
        self._position = Point(x,self._position.get_y())