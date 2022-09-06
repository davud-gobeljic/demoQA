import random
import string
import secrets


class RandomGen():
    def random_generator(self, size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))