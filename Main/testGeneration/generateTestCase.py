from random import randint

def getTestCases():
    data = ""
    for i in range(6):
        Y = randint(0, 1000)
        X = randint(0, 1000)

        data += str(X) + ";" + str(Y) + ";" + str(X+Y) + "\n"
    return data