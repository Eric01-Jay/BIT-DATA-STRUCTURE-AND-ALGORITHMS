# Q1: MoMo Stack Example
stack = []

# Push operations
stack.append("StepA")
stack.append("StepB")
stack.append("StepC")
print("Stack after pushing:", stack)

# Undo two (pop twice)
stack.pop()
stack.pop()
print("Stack after undoing two:", stack)

# Remaining top
print("Remaining top element:", stack[-1])
