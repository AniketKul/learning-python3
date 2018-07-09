'''
Double-ended queues or deques are list-like objects that support
thread-safe, memory efficient appends.
Deques are mutable and support some of the operations of lists such as indexing.
Deques can be assigned by index. e.g: dq[1] = z
However, we cannnot direclty slice deques. (results in TypeError)

Major Advantage: Inserting items at the beginnning of a deque is much
faster than inserting at the beginning of a list.
Although, inserting an item at the end of deque is very slightly slower
than the equivalent operation on a list.

Deques are thread-safe and can be serialized using the pickle module.
'''

from collections import deque

dq = deque('abc') #creates deque(['a','b','c'])
dq.append('d')  #adds the value 'd' to the right
dq.appendleft('z') #adds the value 'z' to the left
dq.extend('efg') #adds multiple items to the right
dq.extendleft('yxw') #adds multiple items to the left
dq.pop()    #returns and removes an item from the right
dq.popleft()    #returns and removes an item from the left

#rotate(n) method is used to move and rotate all items of n steps to the
#right for positive values of the integer n, or left for negative values of n the left,
#using positive integers as the argument. For example,

dq.rotate(2)    #rotates all items 2 steps to the right
dq.rotate(-2)   #rotates all items 2 steps to the left


'''
A simple way to return a slice of deque, as a list.
'''
list(itertools.islice(dq, 3, 9))

'''
A useful feature of deque is they support a maxlen optional parameter that restricts
the size of the deque. This makes it ideally suited to a data structure
known as a circular buffer. This is a fixed-size structure that is effectively
connected end to end and they are typically used fr buffering data streams.
e.g:
'''

dq2 = deque([], maxlen = 3)
for i in range(6):
    dq2.append(i)
    print(dq2)
