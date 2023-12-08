import sqlite3

conn = sqlite3.connect('bank.db')

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY AUTOINCREMENT,  full_name TEXT NOT NULL,  phone_number TEXT NOT NULL,  balance REAL NOT NULL)")


def register_client(full_name, phone_number):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clients (full_name, phone_number, balance) VALUES (?, ?, 0)", (full_name, phone_number))
    conn.commit()

def find_clients(query):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients WHERE full_name LIKE ? OR phone_number LIKE ?",('%' + query + '%', '%' + query + '%'))
    result = cursor.fetchall()

    return result

def deposit_money(client_id, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE clients SET balance = balance + ? WHERE id = ?", (amount, client_id))
    conn.commit()

def withdraw_money(client_id, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM clients WHERE id = ?", (client_id,))
    current_balance = cursor.fetchone()[0]
    if current_balance >= amount:
        cursor.execute("UPDATE clients SET balance = balance - ? WHERE id = ", (amount, client_id))
        conn.commit()
        return True
    else:
        conn.close()
    return False

def view_balance(client_id):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM clients WHERE id = ?", (client_id,))
    balance = cursor.fetchone()[0]
    return balance

def calculate_deposit(client_id, duration_months):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM clients WHERE id = ?", (client_id,))
    balance = cursor.fetchone()[0]

    interest_rate = 0.05

    if duration_months == 12:
        total_amount = balance * (1 + interest_rate)
    elif duration_months == 24:
        total_amount = balance * (1 + 2 * interest_rate)
    elif duration_months == 36:
        total_amount= balance * (1 + 3 * interest_rate)
    else:
        total_amount = balance

    return total_amount
def personal_account(client_id):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
    result = cursor.fetchone()
    return result