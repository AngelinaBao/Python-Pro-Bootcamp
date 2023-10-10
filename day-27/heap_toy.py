import heapq

portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "AAPL", "shares": 50, "price": 543.22},
    {"name": "FB", "shares": 200, "price": 21.09},
    {"name": "HPQ", "shares": 35, "price": 31.75},
    {"name": "YHOO", "shares": 45, "price": 16.35},
    {"name": "ACME", "shares": 75, "price": 115.65},
]

cheap = heapq.nsmallest(3, portfolio, key=lambda d: d["price"])
expensive = heapq.nlargest(3, portfolio, key=lambda d: d["price"])

# print(f"The 3 cheapest: {cheap}")
# print(f"The 3 most expensive: {expensive}")


# nums = [1, 23, -8, 18, 2, 45, -30]
# heapq.heapify(nums)
# print(nums)
# nums.sort()  # sort the heap
# print(nums)
# heapq.heappush(nums, -40)
# print(nums)
# # pop the n smallest numbers
# for _ in range(3):
#     heapq.heappop(nums)
#     print(nums)


def greeting():
    print("Hello")


def bye():
    return "Bye"


h = []
heapq.heappush(h, (1, greeting))
heapq.heappush(h, (2, bye))
print(heapq.heappop(h))
print(h)
