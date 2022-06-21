from enum import Enum, auto


# this inspection is an error in PyCharm when dealing with auto
# noinspection PyArgumentList
class PlayerAction(Enum):
    EXIT_TO_MENU = auto()
    EXIT_TO_DESKTOP = auto()
    START_MOVING_LEFT = auto()
    START_MOVING_RIGHT = auto()
    STOP_MOVING = auto()
    SHOOT = auto()
