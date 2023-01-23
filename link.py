my_list = list(range(0,10))

my_list.append(10)

my_list.insert(2, 34)

#print(my_list)

#deque

from collections import deque

linked_list = deque()

linked_list.append(0)
linked_list.append(2)

linked_list.appendleft(1)

linked_list.popleft()
#print(linked_list)

queue = deque()

for i in range(0, 5):
    queue.append(i)
    #print(queue)

for i in range(len(queue)):

    queue.popleft()

    print(queue)