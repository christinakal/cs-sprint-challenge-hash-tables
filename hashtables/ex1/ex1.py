# NOTES: weight limit, list of weights(weights) and I have a weight limit

# --> two items whose sum of weights equals the weight limit(limit). --> Return a tuple of the two items' weights - should run as O(N)


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Initialize storage for weights 
    needed_weights = dict()

    # Check: If the input array is less than 2 
    if len(weights) < 2:
        return None

    for current_weight_index in range(len(weights)):

        # keep track of the current weight
        current_weight = weights[current_weight_index]

        # if the weight is found, then that means that was inserted previously
        if current_weight in needed_weights:
            # get the index of the weight and add it to the needed_weights
            excisted_weight_index = needed_weights[current_weight]
 
            # return a tuple 
            return (current_weight_index, excisted_weight_index)

        # store info about this current weight
        needed_weights[limit - current_weight] = current_weight_index

    return None


## Hints
 
# * A brute-force solution would involve two nested loops, yielding a
#   quadratic-runtime solution. How can we use a hash table in order to
#   implement a solution with a better runtime?

# * Think about what we can store in the hash table in order to help us to
#   solve this problem more efficiently. 

# * What if we store each weight in the input list as keys? What would be
#   a useful thing to store as the value for each key? 

# ==> as a key we can store the current weight and as a value the current weight's index


#   ASK MELQUI ABOUT THIS:
# * If we store each weight's list index as its value, we can then check
#   to see if the hash table contains an entry for `limit - weight`. If it
#   does, then we've found the two items whose weights sum up to the
#   `limit`!