import random
from string import ascii_lowercase, digits


def create_slug(length: int = 10):

    # Creates a new slug from random characters
    return "".join(random.sample(ascii_lowercase + digits, length))
