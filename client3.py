# Import necessary modules

def getDataPoint(stock_name, bid_price, ask_price):
    # Calculate the price as the average of bid and ask
    price = (bid_price + ask_price) / 2
    # No need to change the return value, as it represents the entire data point
    return (stock_name, bid_price, ask_price, price)

def getRatio(stock1, stock2):
    # Calculate the ratio of the prices of two stocks
    price_a = stock1[3]
    price_b = stock2[3]

    # Handle the case where price_b could be zero to avoid division by zero
    if price_b != 0:
        ratio = price_a / price_b
    else:
        # Set ratio to a default value or handle this case as appropriate for your application
        ratio = float('inf')  # Using infinity as an example

    return ratio

def main():
    # Example stock data
    stocks = [
        ("Stock1", 100, 105),
        ("Stock2", 95, 98),
        # Add more stock data as needed
    ]

    # Store data points in a list
    data_points = []

    # Calculate data points using getDataPoint and store them
    for stock_data in stocks:
        data_point = getDataPoint(*stock_data)
        data_points.append(data_point)

    # Calculate and print the ratio of prices for each pair of stocks
    for i in range(len(data_points)):
        for j in range(i + 1, len(data_points)):
            stock1 = data_points[i]
            stock2 = data_points[j]
            ratio = getRatio(stock1, stock2)

            # Print stock information, prices, and ratio
            print(f"\nStock {i + 1}:")
            print("  Name:", stock1[0])
            print("  Bid Price:", stock1[1])
            print("  Ask Price:", stock1[2])
            print("  Price:", stock1[3])

            print("\nStock {j + 1}:")
            print("  Name:", stock2[0])
            print("  Bid Price:", stock2[1])
            print("  Ask Price:", stock2[2])
            print("  Price:", stock2[3])

            print(f"\nRatio of prices for Stock {i + 1} to Stock {j + 1}:", ratio)

# Call the main function
main()
