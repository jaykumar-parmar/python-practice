def buy_and_sell_stock_once(prices):
    min_buying_price = prices[0]
    max_profit = 0.00

    for price in prices:
        if price < min_buying_price:
            min_buying_price = price
        
        temp_profit = price - min_buying_price

        if temp_profit > max_profit:
            max_profit = temp_profit
    
    return max_profit