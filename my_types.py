import enum


class DictConvertStringType(enum.Enum):
    """Converting format type from dict to string:
    ALL     - "key": value,
    KEYS    - "key",
    VALUES  - value
    """

    ALL = 1
    KEYS = 2
    VALUES = 3


class InputType(enum.Enum):
    """Input data type
    KEYBOARD- input() from keyboard
    FILE    - from file
    """

    KEYBOARD = 1
    FILE = 2
