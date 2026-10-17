# 🏦 Python Banking System

A simple command-line banking system built with Python to practice Object-Oriented Programming (OOP) and fundamental programming concepts.

## ✨ Features

- 🔐 User authentication
- 👤 View user profile
- 💰 Deposit money
- 💸 Withdraw money
- 🔄 Transfer money between users
- ✏️ Edit username
- 🌍 Edit country
- 📜 Automatic activity logging
- 🛡️ Input validation and security lockout

## 🛠️ Technologies

- Python 3
- Object-Oriented Programming (OOP)
- File Handling
- Logging
- Type Hints

## 🚀 How to Run

### Requirements

- Python 3
- `pip`

### 1. Clone the repository

```bash
git clone https://github.com/JahanamV2/banking-system.git
```

### 2. Navigate to the project directory

```bash
cd banking-system
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the program

```bash
python program.py
```

## 📂 Project Structure

```text
banking-system/
├── program.py
├── models/
│   ├── __init__.py
│   └── user.py
├── utils/
│   ├── __init__.py
│   ├── logs.py
│   ├── utilities.py
│   └── validator.py
├── logs/
│   ├── login_logs.txt
│   ├── logout_logs.txt
│   ├── deposit_logs.txt
│   ├── withdraw_logs.txt
│   ├── edit_country_logs.txt
│   ├── edit_username_logs.txt
│   └── edit_transfer_logs.txt
├── requirements.txt
└── README.md
```

## 📚 What I Learned

- Classes and objects
- Inheritance and encapsulation
- Static methods
- Modular programming
- Exception handling
- File handling and logging
- Input validation
- Dictionaries and functions
- Type hints

## 📜 Logging System

The application records user activities, including:

- Login and logout
- Deposits and withdrawals
- Transfers
- Username and country changes

Log entries include timestamps to help track activity.

## 🔮 Future Improvements

- Store user data in JSON
- Integrate an SQLite database
- Implement password hashing
- Add account creation and deletion
- Add transaction history
- Create an administrator panel
- Write unit tests
