
pos = -1

def binary2(list, n):

    lower_bound = 0
    upper_bound = len(list) - 1

    while lower_bound <= upper_bound:

        mid = (lower_bound + upper_bound) // 2

        if list[mid] == n:

            globals() ['pos'] = mid
            return True

        else:

            if list[mid] < n:

                lower_bound = mid + 1

            else:
                upper_bound = mid - 1

    return True


list = [1, 3, 4, 6, 7, 8, 9]
n = 8

if binary2(list, n):
    print('Found at', pos + 1)

else:

    print('Not Respond')

