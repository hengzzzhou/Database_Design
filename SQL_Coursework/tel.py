import random


def get_tel(numIn):
    while True:
        a = "+1-"
        b = hash(str(numIn + random.randint(0, 999))) % 10000000000
        str_out = a + str(b)
        # print(strOut)
        if len(str_out) == 13:
            return str_out
