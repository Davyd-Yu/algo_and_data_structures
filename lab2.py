def optimal_purchase(prices, discount):
    prices.sort(reverse=True)

    n = len(prices)

    num_discounted = min(n // 3, n)

    for i in range(num_discounted):
        prices[i] *= (1 - discount / 100)

    total_cost = sum(prices)

    return total_cost



# Приклади використання функції з вашого опису

# Приклад 1
prices_1 = [50, 20, 30, 17, 100]
discount_1 = 10
result_1 = optimal_purchase(prices_1, discount_1)
print(result_1)  # Очікуваний результат: 207.00

# Приклад 2
prices_2 = [1, 2, 3, 4, 5, 6, 7]
discount_2 = 100
result_2 = optimal_purchase(prices_2, discount_2)
print(result_2)  # Очікуваний результат: 15.00

# Приклад 3
prices_3 = [1, 1, 1]
discount_3 = 33
result_3 = optimal_purchase(prices_3, discount_3)
print(result_3)  # Очікуваний результат: 2.67
