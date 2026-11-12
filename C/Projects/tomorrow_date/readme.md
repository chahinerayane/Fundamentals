# Tomorrow Date

A simple C program that calculates and displays the next calendar date based on a user-provided date.

## Features

- Accepts dates in `DD/MM/YYYY` format.
- Validates the input format.
- Checks whether the entered date is valid.
- Handles months with 30 and 31 days.
- Detects leap years using the Gregorian calendar rules.
- Correctly handles transitions between months and years.
- Displays the next date in `DD/MM/YYYY` format.

## Concepts Practiced

- C programming fundamentals
- Variables and data types
- Conditional statements (`if`, `else`)
- `switch` statements
- Functions
- Enumerations (`enum`)
- Pointers and `scanf()`
- Input validation
- Leap year calculation
- Calendar logic

## How to Run

**1. Clone the repository**

```bash
git clone <your-repository-url>
cd tomorrow-date
```

**2. Compile the program**

```bash
gcc tomorrow_date.c -o tomorrow_date
```

**3. Run it**

```bash
./tomorrow_date
```

## Example

```text
Enter day/month/year in same format : 31/12/2026
01/01/2027
```

Another example:

```text
Enter day/month/year in same format : 28/02/2028
29/02/2028
```

## Notes

This project was created as a C programming practice project to improve my understanding of date validation, conditional logic, functions, and calendar calculations.

---

**Language:** C  
**Compiler:** GCC