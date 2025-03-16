import random

# binary search will take log2 n steps to solve for worst case


def binary_search(the_list: list[int], searched_item: int):
    iter_count = 0

    low = 0
    high = len(the_list) - 1

    while low <= high:
        iter_count += 1
        mid = (low + high) // 2

        # try the middle
        guess = the_list[mid]

        # if found, return it
        if guess == searched_item:
            print(f"found in {iter_count} steps")
            return guess

        # if guess is too high, set highest to the middle, minus 1
        if guess > searched_item:
            high = mid - 1

        # otherwise set the low to the middle, plus 1
        else:
            low = mid + 1

    return None


my_list = list(range(100))
item = my_list[random.randint(0, 99)]

print(binary_search(my_list, item))

# 128 sorted items would take maximum of log(2) 128 steps, i.e. 7 steps
# doubling the list to 256, it would take max log(2) 256, i.e. 8 steps
