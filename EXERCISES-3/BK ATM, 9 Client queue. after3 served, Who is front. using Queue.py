from collections import deque

# Q3: BK ATM Queue Example
queue = deque([1,2,3,4,5,6,7,8,9])
print("Initial queue:", list(queue))

# Serve 3 clients
for _ in range(3):
    queue.popleft()

print("Queue after 3 served:", list(queue))
print("New front client:", queue[0])
