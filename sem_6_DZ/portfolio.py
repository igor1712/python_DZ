def calkulate_portfolio_value(stok: dict, price: dict) -> float:
    global _stok_sum
    _stok_sum = {k: v1 * v2 for (k, v1), (_, v2) in zip(stok.items(), price.items())}
    result = 0
    for value in _stok_sum.values():
        result += value
    return float(result)


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return (current_value - initial_value) / initial_value * 100


def get_most_profitable_stock(stok: dict, price: dict) -> str:
    resulst = {k: v1 - v2 for (k, v1), (_, v2) in zip(_stok_sum.items(), price.items())}
    max_val = (max(resulst.values()))
    for key, value in resulst.items():
        if value == max_val:
            return key
