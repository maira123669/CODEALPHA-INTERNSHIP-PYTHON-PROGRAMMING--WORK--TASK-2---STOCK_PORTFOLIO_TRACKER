#  Stock Portfolio Tracker (Python)

##  Project Description

The **Stock Portfolio Tracker** is a simple Python command-line application that allows users to create and manage a basic stock portfolio. Users can enter stock symbols and the number of shares they own, and the program calculates the total investment value based on predefined stock prices. It also generates a portfolio summary and saves it to a text file.

This project demonstrates the use of Python dictionaries, loops, functions, file handling, exception handling, and user input validation.

---

##  Features

- Displays available stock symbols and their prices.
- Allows users to add multiple stocks to their portfolio.
- Validates stock symbols and user input.
- Updates quantities if the same stock is entered multiple times.
- Calculates the value of each stock holding.
- Calculates the total portfolio value.
- Displays a detailed portfolio report.
- Saves the portfolio summary to a **portfolio_summary.txt** file.

---

##  Technologies Used

- Python 3
- File Handling
- Dictionaries
- Exception Handling

---

##  Project Structure

```
Stock-Portfolio-Tracker/
│── stock_tracker.py
│── portfolio_summary.txt   (Generated after running)
│── README.md
```

---

##  How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python stock_tracker.py
```

---

##  How It Works

1. The program displays a list of available stocks and their prices.
2. Enter a valid stock symbol (e.g., **AAPL**, **TSLA**, **MSFT**).
3. Enter the number of shares you own.
4. Repeat the process to add more stocks.
5. Type **done** when finished.
6. The program calculates the total investment value.
7. A portfolio summary is displayed and saved to **portfolio_summary.txt**.

---

##  Available Stocks

| Stock Symbol | Price (USD) |
|--------------|------------:|
| AAPL | $180 |
| TSLA | $250 |
| MSFT | $420 |
| GOOGL | $175 |
| AMZN | $185 |

---

##  Concepts Used

- Functions
- Dictionaries
- Loops
- Conditional Statements
- User Input
- Exception Handling (`try-except`)
- File Handling
- String Formatting

---

##  Future Improvements

- Load stock prices from an API.
- Support buying and selling shares.
- Store portfolio data permanently using a database.
- Add profit/loss calculations.
- Create a graphical user interface (GUI).
- Display charts for portfolio performance.

---

##  Author

**Maira Masood**

BS Computer Science (BSCS)

---

##  License

This project is created for learning and educational purposes.
