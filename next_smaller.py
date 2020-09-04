from cw_test import Test


##############


def next_smaller(n):

    print(n)

    # Make a list of single-digit ints from the original int
    n_split = [int(i) for i in str(n)]

    # Starting from least significant digit, find the frist inversion
    for i in range(len(n_split) - 1, 0, -1):

        if n_split[i] < n_split[i - 1]:

            if i == 1 and n_split[1] == 0 and n_split[0] <= min((x for x in n_split[i:] if x > 0), default=10):
                return -1

            # Of the digits examined, find the smallest one that is larger than the inversion and swap it.
            # This gives us a number that is larger than the input, but not the smallest one.
            swap = n_split[i - 1:].index(max([x for x in n_split[i - 1:] if x < n_split[i - 1]])) + (i - 1)
            n_split[i - 1], n_split[swap] = n_split[swap], n_split[i - 1]

            # Of the remaing LSD, sort them to get the smallest possible number.
            n_split[i:] = sorted(n_split[i:], reverse=True)

            # Reassmeble an int out of the list of single digits.
            ret = int(''.join([str(i) for i in n_split]))
            if ret == n:
                return -1
            else:
                return ret

    return -1  # Didn't find an inversion, there is no possible larger int with these digits.


##############

if __name__ == "__main__":
    # Test.assert_equals(next_smaller(907), 790)
    # Test.assert_equals(next_smaller(531), 513)
    # Test.assert_equals(next_smaller(135), -1)
    # Test.assert_equals(next_smaller(2071), 2017)
    # Test.assert_equals(next_smaller(414), 144)
    # Test.assert_equals(next_smaller(123456798), 123456789)
    # Test.assert_equals(next_smaller(123456789), -1)
    # Test.assert_equals(next_smaller(1234567908), 1234567890)
    # Test.assert_equals(next_smaller(1027), -1)
    # Test.assert_equals(next_smaller(100), -1)

    Test.assert_equals(next_smaller(9009), -1)
    Test.assert_equals(next_smaller(6006), -1)
    Test.assert_equals(next_smaller(10149), -1)
    Test.assert_equals(next_smaller(202233445566), -1)
    Test.assert_equals(next_smaller(1001), -1)


##############


def next_smaller_v2(n):

    # print(n)

    # Make a list of single-digit ints from the original int
    n_split = [int(i) for i in str(n)]

    # Starting from least significant digit, find the frist inversion
    for i in range(len(n_split) - 1, 0, -1):

        if n_split[i] < n_split[i - 1]:

            if i == 1 and n_split[1] == 0 and n_split[0] < min((x for x in n_split[i:] if x > 0), default=10):
                return -1
                # n_split[i:] = sorted(n_split[i:], reverse=True)
                # if int(''.join([str(i) for i in n_split])) == n:
                #     return -1
                # else:
                #     return int(''.join([str(i) for i in n_split]))

            # Of the digits examined, find the smallest one that is larger than the inversion and swap it.
            # This gives us a number that is larger than the input, but not the smallest one.
            swap = n_split[i - 1:].index(max([x for x in n_split[i - 1:] if x < n_split[i - 1]])) + i - 1
            n_split[i - 1], n_split[swap] = n_split[swap], n_split[i - 1]

            # Of the remaing LSD, sort them to get the smallest possible number.
            n_split[i:] = sorted(n_split[i:], reverse=True)

            # Reassmeble an int out of the list of single digits.
            ret = int(''.join([str(i) for i in n_split]))
            if ret == n:
                return -1
            else:
                return ret

    return -1  # Didn't find an inversion, there is no possible larger int with these digits.


##############

def next_smaller_v1(n):

    print(n)

    # Make a list of single-digit ints from the original int
    n_split = [int(i) for i in str(n)]

    # Starting from least significant digit, find the frist inversion
    for i in range(len(n_split) - 1, 0, -1):
        if n_split[i] < n_split[i - 1]:

            # Of the digits examined, find the smallest one that is larger than the inversion and swap it.
            # This gives us a number that is larger than the input, but not the smallest one.
            swap = n_split[i - 1:].index(max([x for x in n_split[i - 1:] if x < n_split[i - 1]])) + (i - 1)
            n_split[i - 1], n_split[swap] = n_split[swap], n_split[i - 1]

            # Of the remaing LSD, sort them to get the smallest possible number.
            n_split[i:] = sorted(n_split[i:], reverse=True)

            # Reassmeble an int out of the list of single digits.
            return int(''.join([str(i) for i in n_split]))

    return -1  # Didn't find an inversion, there is no possible larger int with these digits.
