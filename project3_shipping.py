weight = 41.5
costs = {}

# Ground Shipping
if weight <= 2:
  costg = weight * 1.5 + 20
elif weight <= 6:
  costg = weight * 3 + 20
elif weight <= 10:
  costg = weight * 4 + 20
else:
  costg = weight *10 + 20

costs[costg] = "Ground Shipping"

# Ground Shipping Premium
costgs = 125
costs[costgs] = "Ground Shipping Premium"

# Drone Shipping
if weight <= 2:
  costd = weight * 4.5
elif weight <= 6:
  costd = weight * 9
elif weight <= 10:
  costd = weight * 12
else:
  costd = weight * 14.25

costs[costd] = "Drone Shipping"

# Find minimum cost
min_cost = min(costs.keys())
# Display cheapest method
print(f"The cheapest method is {costs[min_cost]}; it costs ${min_cost}")
