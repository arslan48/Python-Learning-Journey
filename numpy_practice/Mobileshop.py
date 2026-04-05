import numpy as np

phone_prices = np.array([25000, 45000, 18000, 
                         67000, 32000, 55000,
                         12000, 89000, 43000,
                         71000, 28000, 38000])

def get_states(prices):
    average = np.mean(prices)
    highest = np.max(prices)
    lowest = np.min(prices)
    median = np. median(prices)
    return average,highest,lowest,median


def get_category(prices):
    budget    = len(prices[prices < 30000])
    mid_range = len(prices[(prices >= 30000) & (prices <= 60000)])
    high_end  = len(prices[prices > 60000])
    return budget, mid_range, high_end


def show_rep(prices):
    average,highest,lowest,median = get_states(prices)
    budget, mid_range, high_end = get_category(prices)
    print(f"Average:   {average:.2f}")
    print(f"Highest:   {highest}")
    print(f"Lowest:    {lowest}")
    print(f"Median:    {median}")
    print(f"Budget:    {budget} phones")
    print(f"Mid Range: {mid_range} phones")
    print(f"High End:  {high_end} phones")

phone_prices = np.append(phone_prices, 42000)

show_rep(phone_prices)
    
