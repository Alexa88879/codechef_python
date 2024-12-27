test=int(input())
for _ in range(test):
    no_stock,stock_cost,stock_sell=map(int,input().split())
    profit=no_stock*(stock_sell-stock_cost)
    print(profit)