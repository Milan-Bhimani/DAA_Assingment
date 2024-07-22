def min_days_to_survive(N, S, M):
    total_food_required = S * M
    if total_food_required > N * (S - 1):
        return -1  
    else:
        return -(-total_food_required // N)  