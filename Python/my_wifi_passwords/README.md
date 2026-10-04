# Wi-Fi Profile Viewer

A simple Python command-line tool for Windows that lists saved Wi-Fi profiles and displays detailed information about a selected profile using the `netsh` command.

## Features

* List saved Wi-Fi profiles on Windows
* Select a Wi-Fi profile by name
* Display detailed Wi-Fi profile information
* Retrieve saved Wi-Fi passwords where Windows permissions allow
* Simple interactive command-line interface

## Technologies

* **Python**
* **OS module** — Execute Windows system commands
* **Time module** — Add delays to the execution flow
* **Windows `netsh`** — Manage and inspect wireless network profiles

## Requirements

* Windows operating system
* Python 3.10 or newer
* Permission to access the saved Wi-Fi profile information


## Usage

1. Run the script.
2. Enter `1` to start.
3. View the list of saved Wi-Fi profiles.
4. Enter the name of the Wi-Fi profile you want to inspect.
5. View the profile details provided by Windows.

## What I Practiced

This project helped me practice:

* Python classes and methods
* Importing and using built-in modules
* User input and type conversion
* Exception handling
* Executing system commands with `os.system()`
* Basic command-line application structure
* Windows networking commands
* Understanding saved wireless network profiles

## Platform Compatibility

**Windows only**

This script uses the Windows-specific `netsh wlan` command and is not designed to work on Linux or macOS.

## Security Note

This tool is intended for inspecting Wi-Fi profiles saved on your own Windows device or devices you are authorized to administer.

The `key=clear` option may expose saved Wi-Fi passwords in plaintext. Avoid sharing the output or running the tool on devices without authorization.

## Project Status

**Learning project**

This project was created as part of my Python learning journey to explore system commands, Windows networking, and basic automation. It may be improved in the future with better input validation, safer command execution, and cross-platform support.


