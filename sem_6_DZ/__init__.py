from portfolio import get_most_profitable_stock as gmps, calculate_portfolio_return as cpr, \
    calkulate_portfolio_value as cpv

stoks = {
    "aple": 10,
    "google": 5,
    "MSFT": 8
}
prices = {
    "aple": 155.25,
    "google": 260.75,
    "MSFT": 800.50
}
if __name__ == '__main__':
    print(cpv(stoks, prices))
    print(cpr(100, 150))
    print(gmps(stoks, prices))
