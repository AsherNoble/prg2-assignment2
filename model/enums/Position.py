from enum import Enum
class Position(Enum):
    Fullback = "Fullback"
    Wing = "Wing"
    Centre = "Centre"
    Halfback = "Halfback"
    Forward = "Forward"

    def __str__(self):
        return self.value