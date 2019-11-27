
# For an input array, return the products for sliding windows of some length K.
# Bonus: Do it in O(N) time.

# Example 
    # - input: [4, 3, 2, 0, 4, 2, 2], 3
    # - output: [24, 0, 0, 0, 16]


# O ( n * k ) solution
def print_products1(array, K):

    start = 0
    prods = []
    while start <= ( len(array) - K):

        newN = 1
        for val in array[start: (start + K)]:
            newN *= val

        prods.append(newN)
        start += 1

    return prods


# O ( n ) solution
def print_products2(array, K):

    last_zero_index = None
    start = 0
    newN = 1

    # initialize sliding window prods with first value
    for ind in range(start, (start + K)):
        if array[ind] == 0:
            last_zero_index = ind
        newN *= array[ind]

    start = K
    prods = [newN]

    # If no zeros, last case if all we need
    while start <= (len(array) - 1):

        # Maintain temporary record of running prod, resetting at each 0
        if array[start] == 0:
            last_zero_index = start
            temp_prod = 1
            prods.append(0)

        # Must be zero, but we keep our temp_prod updated
        elif last_zero_index and (start - last_zero_index) <= (K -1):
            temp_prod *= array[start]
            prods.append(0)

        # All for this tricky case, when we can't divide by the prior zero
        elif last_zero_index and (start - last_zero_index) == K:
            prods.append(temp_prod * array[start])

        else:
            prods.append( (prods[-1] * array[start]) / array[start - K])

        start += 1

    return prods

assert print_products2([4, 3, 2, 0, 4, 2, 2], 3) == [24, 0, 0, 0, 16]
array = [1, 4, 3, 2, 0, 6, 7, 0, 1, 2, 100, 0, 0, 1, 5, 199]
assert print_products1(array, 3) == print_products2(array, 3)


