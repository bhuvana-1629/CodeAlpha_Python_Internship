stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150
}

total = 0

n = int(input("Enter number of stocks: "));

for i in range(n):
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if name in stocks:
        investment = stocks[name] * quantity
        total += investment
        print("Investment value:", investment);
    else:
        print("Stock not found");

print("Total Investment Value:", total);