# Dynamic programming: 주어진 문제를 작고 겹치는 하위 문제로 나누어서 하위 문제의 값을 기억하고 재사용하여 문제를 해결한다.(중복된 계산이 일어나는 것을 방지)
# Greedy algorithm: 각 단계에서 의사 결정을 전체 문제/미래의 결과 등을 고려하지 않고 최적의 결정하는 알고리즘

# Knapsack problem(배낭문제)
# 배낭의 무게 제한을 초과하지 않으면서 배낭에 item의 가치를 최대화하는 item의 조합을 찾아라

# W: 배낭 무게 한도, wt: 각 보석의 무게, val: 각 보석의 가격, n: 보석의 수
def KnapSack(W, weight, val, n, memo):
    if n == 0 or W == 0:
        return 0, []
    if memo[n][W] != None:
        return memo[n][W], []

    if weight[n - 1] > W:
        memo[n][W], items = KnapSack(W, weight, val, n - 1, memo)
        return memo[n][W], items
    else:
        val1, items1 = KnapSack(W - weight[n - 1], weight, val, n - 1, memo)
        val1 = val1 + val[n-1]
        val2, items2 = KnapSack(W, weight, val, n - 1, memo)
        if val1 > val2:
            memo[n][W] = val1
            return val1, items1 + [n - 1]
        else:
            memo[n][W] = val2
            return val2, items2


def Fractional_KnapSack(capacity, weights, values):
    items = [(values[i] / weights[i], weights[i], i)
             for i in range(len(values))]
    items.sort(reverse=True)
    total_value = 0
    knapsack_items = []
    for item in items:
        value_ratio, weight, index = item
        if capacity >= weight:
            total_value = total_value + (weight * value_ratio)
            capacity -= weight
            knapsack_items = knapsack_items + [(index, 1)]
        else:
            fraction = capacity / weight
            total_value = total_value + (fraction * weight * value_ratio)
            knapsack_items = knapsack_items + [(index, fraction)]
    return total_value, knapsack_items


W = 50
val = [60, 100, 120]
weight = [10, 20, 30]
n = len(val)
memo = [[None] * (W + 1) for _ in range(n + 1)]
# 가방에 담긴 value, 가방에 담긴 item 개수

print("algorithm_6 output\n")
print("1. dynamic programming algorithm")
print("value sum, item index = {}\n".format(KnapSack(W, weight, val, n, memo)))
print("2. greedy algorithm")
print("value sum, item index = {}\n".format(
    Fractional_KnapSack(W, weight, val)))
