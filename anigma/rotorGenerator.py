import random
import pickle
import os
from datetime import date


def __main__():
    letters = ''
    for i in range(0, 255):
        letters += chr(i)
    today = date.today()
    random.seed(str(today))

    r1 = list(letters)
    random.shuffle(r1)
    r1 = ''.join(r1)

    r2 = list(letters)
    random.shuffle(r2)
    r2 = ''.join(r2)

    r3 = list(letters)
    random.shuffle(r3)
    r3 = ''.join(r3)

    if os.path.isfile('rotors'):
        os.remove('rotors')
    f = open('rotors', 'xb')
    pickle.dump((r1, r2, r3), f)
    f.close()


if __main__ is not None:
    __main__()


