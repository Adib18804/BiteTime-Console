# BiteTime Console 🍔⏱️

A lightweight, console-based food ordering system built with Python. It allows customers to browse a menu, place an order, and see the total cost and preparation time instantly.

## Features

-   **Interactive Menu Display:** Dynamically prints the available menu items and their prices.
-   **Flexible Ordering:** Users can order multiple items in any quantity.
-   **Input Validation:** Handles invalid item names and non-positive quantities gracefully.
-   **Real-time Calculation:** Automatically calculates the total order cost and cumulative preparation time as items are added.
-   **User-Friendly:** Simple text-based interface with clear prompts and feedback.

## How It Works

1.  The program starts by displaying a welcome message and the menu.
2.  The user is prompted to enter an item name or type `done` to finish.
3.  For each valid item, the user specifies a quantity.
4.  The program adds the item's cost (`price * quantity`) to the bill and its preparation time (`prep_time * quantity`) to the timer.
5.  Once the user is done, the program prints the final bill and total preparation time.

## Code Structure

The logic is built around two core dictionaries:

-   `menu`: Stores item names as keys and their prices as values.
-   `prep_time`: Stores item names as keys and their preparation times (in minutes) as values.

The main loop handles user input, validates it, and updates the running totals (`item_price`, `total_time`).

## Installation & Usage

1.  **Prerequisites:** Ensure you have Python 3.x installed on your system.
2.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/biteitme-console.git
    cd biteitime-console
    ```
3.  **Run the application:**
    ```bash
    python takeout_system.py
    ```
    *(or whatever you named your Python file)*

## Example Usage
