# Q4: Airtel Queue Example
queue = deque(["Client1", "Client2", "Client3", "Client4", "Client5"])
print("Initial queue:", list(queue))

# First served
first_served = queue.popleft()
print("First client served:", first_served)
