from random import randint
from Main.models import Test, Input

class Exam:
    def __init__(self, id):
        self.__generationProgramme = None
        self.__testCases = None
        self.__generators = []

        testItem = Tes.objects.get(pk=id)
        self.__generationProgramme = testItem.output_generator
        self.__testCases = testItem.no_test_cases

        for input_item in Input.objects.filter(test=testItem):
            self.__generators.append([input_item.name, self.__getGenerator(input_item.data_type, input_item.values)])

    def __getGenerator(self, Dtype, values):
        if Dtype == "Real":
            return 1
        elif Dtype == "Character":
            return 2
        elif Dtype == "String":
            return 3
        else:
            return 4

    def getTestCases(self):
        testCases = []

        for i in range(self.__testCases):
            testCase = []
            for name, gen in self.__generators:
                testCase.append([name, gen.getValue()])
            testCases.append(testCase)
        return testCases

# Kept for compatibility
def getTestCases():
    data = ""
    for i in range(6):
        Y = randint(0, 1000)
        X = randint(0, 1000)

        data += str(X) + ";" + str(Y) + ";" + str(X+Y) + "\n"
    return data