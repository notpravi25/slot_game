import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}


symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_win(columns, lines, bet, values):
    win = 0
    win_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            win += values[symbol] * bet
            win_lines.append(line + 1)

    return win, win_lines

def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns
                
def print_slot(columns):
    for row in range(len(columns[0])):
        print(" | ".join(column[row] for column in columns))


def deposit():
    while True:
        amount = input("what would u like to deposit? $$")
        if amount.isdigit():
            amount = int (amount)
            if amount > 0:
                break
            else:
                print("amount should be greater than zero")
        else:
            print("enter valid amount")
    return amount

def get_no_line():
    while True:
        lines = input("enter no of lines to bet on (1-"+str(MAX_LINES)+")? ") 
        if lines.isdigit():
            lines = int (lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("enter valid no of lines ")
        else:
            print("enter valid lines")
    return lines

def get_bet():
    while True:
        amount = input("what would u like to bet? $$")
        if amount.isdigit():
            amount = int (amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount should be between ${MIN_BET} AND ${MAX_BET}.")
        else:
            print("enter valid amount")
    return amount
def game(balance):
    lines = get_no_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"you don't have enough balance, your current balance is  ${balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet = ${total_bet}")

    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot(slots)
    win, win_lines = check_win(slots, lines, bet, symbol_values)
    print(f"you won ${win}")
    if win_lines:
        print("you won on lines:", *win_lines)
    else:
        print("no winning lines")

    return win - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        choice = input("press enter to play (q to quit).")
        if choice == "q":
            break
        balance += game(balance)
        print(f"you are left with ${balance}")


main()