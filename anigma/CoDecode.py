import pickle
import os
import rotorGenerator

state = 0
alphabet = ''
for i in range(0, 255):
    alphabet += chr(i)

if not os.path.isfile('rotors'):
    rotorGenerator.__main__()
f = open('rotors', 'rb')
r1, r2, r3 = pickle.load(f)
f.close()


def reflector(c):
    return alphabet[len(alphabet) - alphabet.find(c) - 1]


def enigma_one_char(c):
    c1 = r1[alphabet.find(c)]
    c2 = r2[alphabet.find(c1)]
    c3 = r3[alphabet.find(c2)]
    reflected = reflector(c3)
    c3 = alphabet[r3.find(reflected)]
    c2 = alphabet[r2.find(c3)]
    c1 = alphabet[r1.find(c2)]
    return c1


def rotateRotors():
    global r1, r2, r3
    r1 = r1[1:] + r1[0]
    if state % 255 == 0:
        r2 = r2[1:] + r2[0]
    if state % (255 * 255) == 0:
        r3 = r3[1:] + r3[0]


def __main__(plain):
    global state
    cipher = ''
    for i in plain:
        state += 1
        cipher += enigma_one_char(i)
        rotateRotors()

    return cipher
