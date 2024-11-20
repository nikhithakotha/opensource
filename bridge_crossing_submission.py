def calculate_max_mangoes(mango_weight, truck_weight, bridge_capacity):
    max_mangoes = (bridge_capacity - truck_weight) // mango_weight
    return max(0, max_mangoes)
x, y, z = map(int, input().split())
print(calculate_max_mangoes(x, y, z))
