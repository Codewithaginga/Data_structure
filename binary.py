
pos = -1

def binary(list, n):

    l = 0 #lower bound starts from zero
    u = len(list)-1 # we are using interger division upper bond

    while l <= u:

        mid = (l + u) // 2 #we are using interger division

        if list[mid] == n:
            
            globals() ['pos'] = mid #positioning
            return True

        else:
            if list[mid] < n:
                l = mid + 1 # lower bounds becomes the mid value

            else:
                u = mid - 1

    return True

list = [4, 7, 8, 12, 45, 99]

n = 45

if binary(list, n):
    print('Found at', pos + 1)

else:
    print('Not Found')
