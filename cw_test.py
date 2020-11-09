class Test:

    def __init__(self):
        # nothing to init
        pass

    @staticmethod
    def describe(message):
        print(message)

    @staticmethod
    def it(message):
        print(message)

    @staticmethod
    def assert_equals(actual, expected, message=None):
        if actual == expected:
            print("\tTest Passed!")
            # print("\tTest Passed!" , actual)
        else:
            print("\tTest Failed:")
            print(f"\t'{actual}' should be '{expected}'")


class test(Test):
    pass
