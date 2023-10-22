import random

class Something :


    def number(self):
        ratul = random.randint(1,6)
        dahyun = random.randint(1,6)
        return ratul, dahyun



something = Something()

print(something.number())

import random


class Something:
    def __init__(self, p,q):
        self.p = p
        self.q = q
    def number(self):
        ratul = random.randint(1, 6)
        dahyun = random.randint(1, 6)
        return ratul, dahyun


something = Something()

print(something.number())



