# Banking System in C

A simple command-line banking system built with C. This project focuses on practicing structures, pointers, functions, input validation, and basic banking operations.

## Features

- **Account Information:** Display account name, age, and balance.
- **Balance Inquiry:** Check the current account balance.
- **Update Information:** Change account name and age.
- **Deposit:** Add money to the account.
- **Withdraw:** Withdraw money while checking available balance.
- **Input Validation:** Validate user input and reject invalid amounts or ages.
- **Menu System:** Navigate through banking operations using a simple interactive menu.

## Concepts Practiced

- Structures (`struct`)
- Pointers and structure pointers
- Functions and return values
- Boolean values (`stdbool.h`)
- Conditional statements and loops
- Input handling (`scanf`, `fgets`, `getchar`)
- String manipulation (`string.h`)
- Basic input validation

## Requirements

- GCC compiler
- Linux, Windows, or macOS
- Basic C development environment

## Compilation and Execution

Compile the program:

```bash
gcc main.c -o banking
```

Run it:

```bash
./banking
```

## Project Status

**In Development V2**

Planned improvements:

- Support multiple bank accounts.
- Add money transfers between accounts.
- Generate unique account IDs.
- Store account information using text files.
- Implement username and password authentication.
- Add transaction and login logs.
- Implement account suspension after repeated failed login attempts.
- Build a log checker to inspect suspicious login activity.

## Future Direction

The long-term goal is to extend this project with C network programming, allowing multiple clients to communicate with a central banking server using TCP sockets.

---

**Language:** C  