def has_negatives(a):
    numbers = dict()
    result = []

    for number in a:
        # add the numbers to the dictionary
        numbers[number] = 1
        
        # if the current number's negative version is in the dictionary, add the positive version to result arr
        # make sure to exclude zero
        if number != 0 and -number in numbers:
            result.append(abs(number))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
