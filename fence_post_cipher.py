from cw_test import Test

##############


def encode_rail_fence_cipher(string, n):
    base_freq = (n - 1) * 2  # Frequency of cycling through all the rails
    list_of_rails = [[] for _ in range(n)]

    # Put each char in the plain text string into the correct rail.
    # All the rails have frequency = (n-1)/2.
    for i in range(len(string)):
        list_of_rails[int(i % base_freq if (i % base_freq < base_freq / 2)
                          else i % base_freq - (2 * (i % (base_freq / 2))))].append(string[i])

    return ''.join([item for sublist in list_of_rails for item in sublist])


def decode_rail_fence_cipher(string, n):

    base_freq = (n - 1) * 2  # Frequency of cycling through all the rails
    indexes = []  # Which rail to pull from when reconstructing the plain text
    list_of_rails = [[] for _ in range(n)]  # Break  cipher text into rails
    counts = []  # How many chars in each rail
    string_len = len(string)  # Save the length for later
    out = []  # Plain text list of chars

    # Fill out the list of indexes: zero to n/2 and back down.
    for i in range(string_len):
        indexes.append(int(i % base_freq if (i % base_freq < base_freq / 2)
                       else i % base_freq - (2 * (i % (base_freq / 2)))))

    # How many of each index are there? Use this in the next step.
    for i in range(n):
        counts.append(indexes.count(i))

    # Counting backwards from n, break the cipher text into individual rails.
    for i in range(n - 1, -1, -1):
        list_of_rails[i] = string[-counts[i]:]
        string = string[:-counts[i]]

    # The rails are strings, convert them to lists of chars
    for i in range(len(list_of_rails)):
        list_of_rails[i] = list(list_of_rails[i])

    # Use the list of indexes to pop the first char off the appropriate rail
    # and add to output
    for i in range(string_len):
        out.append(list_of_rails[indexes[i]].pop(0))

    # Make string out list of chars and return
    return ''.join(out)


##############

if __name__ == "__main__":

    # encode_rail_fence_cipher('WEAREDISCOVEREDFLEEATONCE', 3)

    # decode_rail_fence_cipher('WECRLTEERDSOEEFEAOCAIVDEN', 3)

    Test.assert_equals(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3), "WECRLTEERDSOEEFEAOCAIVDEN")

    hw = 'Hello, World!'

    Test.assert_equals(encode_rail_fence_cipher(hw, 3), "Hoo!el,Wrdl l")
    Test.assert_equals(encode_rail_fence_cipher(hw, 4), "H !e,Wdloollr")
    Test.assert_equals(encode_rail_fence_cipher("", 3), "")

    Test.assert_equals(decode_rail_fence_cipher("H !e,Wdloollr", 4), "Hello, World!")
    Test.assert_equals(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3), "WEAREDISCOVEREDFLEEATONCE")
    Test.assert_equals(decode_rail_fence_cipher("", 3), "")
