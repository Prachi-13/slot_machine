import uuid
import random
from core.config.constants import (
    SYMBOLS_LIST,
    THIRTY_PERCENT_CHANCE,
    SIXTY_PERCENT_CHANCE,
)


def generate_random_string(string_length=10):
    """
    Generates a random string using `uuid` of given length.
    """
    if type(string_length) != int:
        raise ValueError("length is not integer")
    rand_uuid = str(uuid.uuid4())
    uuid_str = "".join(rand_uuid.split("-"))
    return uuid_str[:string_length]


def generate_random_blocks(user_credits):
    result = generate_random_symbols_list()
    re_roll_chances = generate_random_number(0, 100) / 100
    if user_credits < 40:
        return result
    elif user_credits >= 40 and user_credits <= 60:
        # 30% chance that user will re-roll in this round
        if re_roll_chances > 0 and re_roll_chances <= THIRTY_PERCENT_CHANCE:
            result = generate_random_symbols_list()
    elif user_credits > 60:
        # 60% chance that user will re-roll in this round
        if re_roll_chances > 0 and re_roll_chances <= SIXTY_PERCENT_CHANCE:
            result = generate_random_symbols_list()
    return result


def generate_random_symbols_list():
    return [random.choice(SYMBOLS_LIST) for _ in range(3)]


def generate_random_number(low, high):
    return random.randint(low, high)
