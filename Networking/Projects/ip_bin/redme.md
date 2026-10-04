# IPv4 Binary Converter

A simple Python command-line tool that converts IPv4 addresses between dotted-decimal and dotted-binary notation.

This project was created as part of my Python and networking learning journey to practice input validation, functions, loops, exception handling, and IPv4 binary representation.

## Features

* Convert IPv4 addresses from decimal to binary
* Convert IPv4 addresses from binary to decimal
* Validate IPv4 octet ranges
* Validate binary octets
* Ensure binary octets contain exactly 8 bits
* Handle invalid IPv4 input
* Simple command-line interface

## Example

### Decimal to Binary

```text
Input:
192.168.1.1

Output:
11000000.10101000.00000001.00000001
```

### Binary to Decimal

```text
Input:
11000000.10101000.00000001.00000001

Output:
192.168.1.1
```

## Technologies

* **Python**
* Python standard library

## Requirements

* Python 3.10 or newer

## Usage

Run the program and enter an IPv4 address:

```text
=> : 192.168.1.1

11000000.10101000.00000001.00000001
```

Or provide an IPv4 address in binary notation:

```text
=> : 11000000.10101000.00000001.00000001

192.168.1.1
```

## What I Practiced

This project helped me practice:

* Python functions
* Lists and list comprehensions
* Loops
* Conditional statements
* String manipulation
* `try` / `except`
* Input validation
* Binary and decimal conversion
* IPv4 structure
* IPv4 octets
* Working with the Python `bin()` function
* Command-line input
* Basic program structure

## Networking Concepts

This project reinforces several IPv4 concepts:

* IPv4 addresses contain **4 octets** 
* Each decimal octet ranges from **0 to 255**
* Each binary octet contains **8 bits**
* An IPv4 address contains **32 bits** in total
* Each decimal octet corresponds to one binary octet

For example:

```text
192.168.1.1

192      168      1        1
11000000 10101000 00000001 00000001
```

## Project Status

**Completed — Learning Project**

This project was created during my Python and networking learning journey. It may be improved in the future with stronger IPv4 validation, better error handling, automated tests, and additional networking functionality.


