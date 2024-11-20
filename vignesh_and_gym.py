def check_gym_options(gym_cost, trainer_cost, budget):
    if budget < gym_cost:
        return 0
    if budget >= (gym_cost + trainer_cost):
        return 2
    return 1
gym_cost, trainer_cost, budget = map(int, input().split())
print(check_gym_options(gym_cost, trainer_cost, budget))
