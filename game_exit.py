from enum import Enum, auto


# this inspection is an error in PyCharm when dealing with auto
# noinspection PyArgumentList
class GameExit(Enum):
    FALSE = auto()
    TO_DESKTOP = auto()
    TO_MENU = auto()
