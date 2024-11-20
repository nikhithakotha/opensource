def calculate_notebooks(pulp_kg):
    return pulp_kg * (1000 // 100)
pulp = int(input())
print(calculate_notebooks(pulp))
