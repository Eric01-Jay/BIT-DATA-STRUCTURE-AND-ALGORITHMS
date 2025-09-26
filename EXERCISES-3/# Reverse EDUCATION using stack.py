# Reverse EDUCATION using stack
word = "EDUCATION"
stack = []

# Push each character
for ch in word:
    stack.append(ch)

# Pop to reverse
reversed_word = ""
while stack:
    reversed_word += stack.pop()

print("Original word:", word)
print("Reversed word:", reversed_word)
