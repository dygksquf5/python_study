import sys


# 최댓값이 되어야 될 부분은 최솟값으로 설정, 최솟값이 되어야 될 부분은 최댓값으로 설정! 왜냐면 언제든 바로 교체 해야 되기 때문!
# 이는 시스템상 가장 최대, 최솟값을 지정해주는 것 !

def max_profit(prices):
    profit = -sys.maxsize
    min_price = sys.maxsize

    for price in prices:
        # 최댓값이 들어있고, 최댓값과 비교해서 들어온 price가 더 작으면 price로 교체해라!
        min_price = min(min_price, price)
        # 최솟값이 들어있고, 최솟값과 비교해서 들어온 price 에다가 최솟값을 뺐을 때, 진행하다가 더 큰 값을 profit 에 넣어라!
        profit = max(profit, price - min_price)

    return profit


a = [7, 1, 5, 3, 6, 4]
print(max_profit(a))

