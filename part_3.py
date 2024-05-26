# Dynamic Programming Approach

# Define the items with their respective weights, values, and priceless attribute
items = [
    {"name": "Sceptre of Eternal Power", "value": float("inf"), "weight": 5, "priceless": True},
    {"name": "The Eye of Horus Pendant", "value": 2_000_000, "weight": 0.5, "priceless": False},
    {"name": "The Ankh of Immortality", "value": 5_000_000, "weight": 1.5, "priceless": False},
    {"name": "The Scarab Amulet of Fortune", "value": 1_500_000, "weight": 0.2, "priceless": False},
    {"name": "The Golden Mask of Osiris", "value": 10_000_000, "weight": 2, "priceless": False},
    {"name": "The Crown of the Pharaohs", "value": 15_000_000, "weight": 3, "priceless": False},
    {"name": "The Emerald Scarab of Transformation", "value": 3_000_000, "weight": 2, "priceless": False}
]

# Capacity of the bag
capacity = 10

# Initialize variables
remaining_capacity = capacity
included_items = []

# Select the priceless items first
priceless_items = [item for item in items if item['priceless']]
for item in priceless_items:
    if item['weight'] <= remaining_capacity:
        included_items.append(item)
        remaining_capacity -= item['weight']

# Items with value (excluding priceless ones)
valuable_items = [item for item in items if not item['priceless']]

# Number of valuable items
n = len(valuable_items)

# Initialize the DP table
dp = [[0 for _ in range(int(remaining_capacity * 10) + 1)] for _ in range(n + 1)]

# Fill the DP table
for i in range(1, n + 1):
    for w in range(int(remaining_capacity * 10) + 1):
        if valuable_items[i-1]["weight"] * 10 <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - int(valuable_items[i-1]["weight"] * 10)] + valuable_items[i-1]["value"])
        else:
            dp[i][w] = dp[i-1][w]

# Find the items to include in the knapsack for valuable items
w = int(remaining_capacity * 10)
for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        included_items.append(valuable_items[i-1])
        w -= int(valuable_items[i-1]["weight"] * 10)

# Calculate the total value and weight of the included items
total_value = sum(item["value"] for item in included_items)
total_weight = sum(item["weight"] for item in included_items)

# Output the result
print(f"Total Value: {'∞' if any(item['priceless'] for item in included_items) else f'${total_value:,}'}")
print(f"Total Weight: {total_weight} kg")
print("Items to include in the knapsack:")
for item in included_items:
    value_display = "∞" if item["priceless"] else f"${item['value']:,}"
    print(f"{item['name']} (Value: {value_display}, Weight: {item['weight']} kg)")


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Brute Force Approach

def knapsack_brute_force(items, capacity):
    def knapsack_recursive(index, remaining_capacity):
        if index == len(items) or remaining_capacity == 0:
            return 0, []

        # Exclude the current item
        exclude_value, exclude_items = knapsack_recursive(index + 1, remaining_capacity)
        
        # Include the current item if it fits
        include_value = 0
        include_items = []
        if items[index]["weight"] <= remaining_capacity:
            next_value, next_items = knapsack_recursive(index + 1, remaining_capacity - items[index]["weight"])
            include_value = items[index]["value"] + next_value
            include_items = [items[index]] + next_items

        # Return the combination with higher value
        if include_value > exclude_value:
            return include_value, include_items
        else:
            return exclude_value, exclude_items

    return knapsack_recursive(0, capacity)

# Define the items with their respective weights and values
items = [
    {"name": "Sceptre of Eternal Power", "value": float("inf"), "weight": 5},
    {"name": "The Eye of Horus Pendant", "value": 2_000_000, "weight": 0.5},
    {"name": "The Ankh of Immortality", "value": 5_000_000, "weight": 1.5},
    {"name": "The Scarab Amulet of Fortune", "value": 1_500_000, "weight": 0.2},
    {"name": "The Golden Mask of Osiris", "value": 10_000_000, "weight": 2},
    {"name": "The Crown of the Pharaohs", "value": 15_000_000, "weight": 3},
    {"name": "The Emerald Scarab of Transformation", "value": 3_000_000, "weight": 2}
]

# Capacity of the bag
capacity = 10

# Solve the Knapsack Problem using brute force
total_value, included_items = knapsack_brute_force(items, capacity)

# Output the result
print(f"Total Value: {'∞' if total_value == float('inf') else f'${total_value:,}'}")
print(f"Total Weight: {sum(item['weight'] for item in included_items)} kg")
print("Items to include in the knapsack:")
for item in included_items:
    value_display = "∞" if item["value"] == float('inf') else f"${item['value']:,}"
    print(f"{item['name']} (Value: {value_display}, Weight: {item['weight']} kg)")







