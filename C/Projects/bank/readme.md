# Banking System in C

A command-line banking system built with C. This project focuses on practicing structures, pointers, functions, input validation, file handling, dynamic memory allocation, and basic banking operations.

## Features

- **Account Information:** Display account name, age, and balance.
- **Balance Inquiry:** Check the current account balance.
- **Update Information:** Change account name and age.
- **Deposit:** Add money to the account.
- **Withdraw:** Withdraw money while checking available balance.
- **Account Creation:** Create a new account with age and initial deposit validation.
- **File Storage:** Store account information in a text file.
- **Account Reading:** Read and parse stored account information.
- **Login:** Username-based account login (in development).
- **Input Validation:** Validate user input and reject invalid amounts or ages.
- **Menu System:** Navigate through banking operations using a simple interactive menu.

## Concepts Practiced

- Structures (`struct`)
- Pointers and structure pointers
- Functions and return values
- Dynamic memory allocation (`malloc`)
- File handling (`fopen`, `fprintf`, `fgets`, `rewind`)
- Multidimensional arrays
- Boolean values (`stdbool.h`)
- Conditional statements and loops
- Input handling (`scanf`, `fgets`, `getchar`)
- String manipulation (`string.h`)
- Input validation
- Memory management

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

**In Development – V2**

Current development focuses on supporting multiple accounts using file storage and implementing a username-based login system.

Planned improvements:

- Complete multiple-account management.
- Implement username and password authentication.
- Add money transfers between accounts.
- Generate unique account IDs.
- Persist account modifications to files.
- Add transaction and login logs.
- Implement account suspension after repeated failed login attempts.
- Build a log checker to inspect suspicious login activity.

## Future Direction

The long-term goal is to extend this project with C network programming, allowing multiple clients to communicate with a central banking server using TCP sockets.

---

**Language:** C
