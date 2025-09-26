import array

# -------------------------
# Integers
# -------------------------
visits = [15, 20, 12, 18, 25, 30]  # number of clinic visits in different weeks

total_visits = sum(visits)
avg_visits = total_visits / len(visits)
min_visits = min(visits)
max_visits = max(visits)

print("---- Integers ----")
print(f"Total Visits: {total_visits}")
print(f"Average Visits: {avg_visits}")
print(f"Minimum Visits: {min_visits}")
print(f"Maximum Visits: {max_visits}\n")

# -------------------------
# Strings
# -------------------------
report = f"Veterinary Clinic Report:\nTotal = {total_visits}, Average = {avg_visits:.2f}"
summary = f"Highest = {max_visits}, Lowest = {min_visits}"

print("---- Strings ----")
print(report)
print(summary, "\n")

# -------------------------
# Booleans
# -------------------------
threshold = 18
if avg_visits > threshold and max_visits > 20:
    print("---- Booleans ----")
    print("Above Standard\n")
else:
    print("---- Booleans ----")
    print("Below Standard\n")

# -------------------------
# Lists
# -------------------------
pets = ["dog", "cat", "rabbit", "parrot"]
print("---- Lists ----")
print("Before:", pets)

# Add a new pet
pets.append("hamster")

# Remove one based on condition
if "rabbit" in pets:
    pets.remove("rabbit")

# Sort the list
pets.sort()
print("After:", pets, "\n")

# -------------------------
# Arrays
# -------------------------
arr_visits = array.array('i', visits)
arr_sum = sum(arr_visits)

print("---- Arrays ----")
print("Array Sum:", arr_sum)
print("List Sum:", total_visits, "\n")

# -------------------------
# Dictionaries
# -------------------------
records = [
    {"id": 1, "name": "dog", "value": 10},
    {"id": 2, "name": "cat", "value": 15},
    {"id": 3, "name": "parrot", "value": 8},
]

print("---- Dictionaries ----")
# Update one record
records[0]["value"] = 12

# Delete one record
records = [r for r in records if r["id"] != 3]

# Compute total value
total_value = sum(r["value"] for r in records)

print("Updated Records:", records)
print("Total Value:", total_value)
