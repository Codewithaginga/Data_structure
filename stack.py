from collections import deque

#last in first out (LIFO)
stack = deque()

for i in range(0,5):

    stack.appendleft(i)

    print(stack)


print()

for i in range(len(stack)):

    stack.popleft()

    print(stack)
