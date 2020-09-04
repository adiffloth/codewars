from cw_test import Test


##############


def next_bigger(n):

    # Make a list of single-digit ints from the original int
    n_split = [int(i) for i in str(n)]

    # Starting from least significant digit, find the frist inversion
    for i in range(len(n_split) - 1, 0, -1):
        if n_split[i] > n_split[i - 1]:

            # Of the digits examined, find the smallest one that is larger than the inversion and swap it.
            # This gives us a number that is larger than the input, but not the smallest one.
            swap = n_split[i - 1:].index(min([x for x in n_split[i - 1:] if x > n_split[i - 1]])) + (i - 1)
            n_split[i - 1], n_split[swap] = n_split[swap], n_split[i - 1]

            # Of the remaing LSD, sort them to get the smallest possible number.
            n_split[i:] = sorted(n_split[i:])

            # Reassmeble an int out of the list of single digits.
            return int(''.join([str(i) for i in n_split]))

    return -1  # Didn't find an inversion, there is no possible larger int with these digits.


##############

def next_bigger_v2(n):

    # Make a list of single-digit ints from the original int
    n_split = [int(i) for i in str(n)]

    # Starting from least significant digit, find the frist inversion and flip it
    for i in range(len(n_split) - 1, 0, -1):
        if n_split[i] > n_split[i - 1]:
            n_split[i], n_split[i - 1] = n_split[i - 1], n_split[i]

            n_split[i:] = sorted(n_split[i:])

            return int(''.join([str(i) for i in n_split]))
    return -1


def next_bigger_v1(n):

    # Make a list of single-digit ints from the original int
    n_split = [int(i) for i in str(n)]

    # Starting from least significant digit, find the frist inversion and flip it
    for i in range(len(n_split) - 1, 0, -1):
        if n_split[i] > n_split[i - 1]:
            n_split[i], n_split[i - 1] = n_split[i - 1], n_split[i]

            # Need to put the sort logic in here

            return int(''.join([str(i) for i in n_split]))
    return -1


##############


if __name__ == "__main__":
    Test.assert_equals(next_bigger(12), 21)
    Test.assert_equals(next_bigger(513), 531)
    Test.assert_equals(next_bigger(2017), 2071)
    Test.assert_equals(next_bigger(414), 441)
    Test.assert_equals(next_bigger(144), 414)
    Test.assert_equals(next_bigger(95), -1)
    Test.assert_equals(next_bigger(987200), -1)
    Test.assert_equals(next_bigger(9876543210), -1)
    Test.assert_equals(next_bigger(1234), 1243)
    Test.assert_equals(next_bigger(7890), 7908)
    Test.assert_equals(next_bigger(1), -1)
    Test.assert_equals(next_bigger(345621), 346125)
    Test.assert_equals(next_bigger(5082), 5208)
