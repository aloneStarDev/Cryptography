import random
import pickle
from datetime import date


class Rotor:
    def __init__(self):
        self.letters = ''
        for i in range(0, 255):
            self.letters += chr(i)

        self.rotor_value = list(self.letters)
        random.shuffle(self.rotor_value)
        self.data = ''.join(self.rotor_value)


def __main__():
    today = date.today()
    random.seed(str(today))
    rotors = [Rotor().data for _ in range(3)]

    with open("rotors", "wb") as rotors_file:
        pickle.dump(tuple(rotors), rotors_file)


if __main__ is not None:
    __main__()
