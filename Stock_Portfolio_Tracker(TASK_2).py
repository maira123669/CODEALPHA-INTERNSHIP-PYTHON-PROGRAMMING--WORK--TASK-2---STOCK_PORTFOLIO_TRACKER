def stock_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "MSFT": 420,
        "GOOGL": 175,
        "AMZN": 185
    }
    
    portfolio = {}
    print("--- Stock Portfolio Tracker ---")
    print("Available stocks and prices:", stock_prices)
    
    while True:
        symbol = input("\nEnter stock symbol to add (or type 'done' to finish): ").upper().strip()
        if symbol == 'DONE':
            break
            
        if symbol not in stock_prices:
            print(" Stock not found in system. Please choose from available stocks.")
            continue
            
        try:
            quantity = int(input(f"Enter number of shares for {symbol}: "))
            if quantity <= 0:
                print(" Quantity must be greater than 0.")
                continue
            
            # Update portfolio (adds to existing quantity if entered twice)
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        except ValueError:
            print(" Invalid quantity. Please enter a whole number.")

    if not portfolio:
        print("\nPortfolio is empty. Exiting.")
        return

    # Calculate values and generate report
    total_portfolio_value = 0
    report_lines = ["=== YOUR STOCK PORTFOLIO ==="]
    
    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]
        total_value = quantity * price
        total_portfolio_value += total_value
        report_lines.append(f"{symbol}: {quantity} shares @ ${price} each = ${total_value}")
        
    report_lines.append(f"=============================")
    report_lines.append(f"Total Investment Value: ${total_portfolio_value}")

    # Print to console
    print("\n" + "\n".join(report_lines))

    # Save to file
    try:
        with open("portfolio_summary.txt", "w") as file:
            file.write("\n".join(report_lines))
        print("\nPortfolio saved successfully to 'portfolio_summary.txt'!")
    except IOError:
        print("\nError saving portfolio to file.")

if __name__ == "__main__":
    stock_tracker()