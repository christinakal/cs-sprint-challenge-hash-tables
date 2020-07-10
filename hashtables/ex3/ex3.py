def intersection(arrays):
    hits = dict()
    result = []

    for array in arrays:
        
        for number in array:
            if number in hits:
                hits[number] += 1
            else:
                hits[number] = 1


        for number in hits:
            result.append(number)


    return result
    


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))


# input will be like:

# [
#     [1, 2, 3, 4, 5],
#     [12, 7, 2, 9, 1],m
#     [99, 2, 7, 1,]
# ]