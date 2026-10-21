
def remaining_budget(budget: float, spent: float) -> float:
    if budget < 0 or spent < 0:
        raise ValueError("budget and spent must be non-negative")
    return budget - spent
