# Password Manager

A simple command-line password manager built with **Python** that allows you to securely store and retrieve passwords for different websites. When a saved password is retrieved, it is automatically copied to the clipboard for quick and convenient use.

## Features

* Save passwords for different websites
* Retrieve saved passwords instantly
* Automatic clipboard copy using `pyperclip`
* Lightweight and easy to use
* No external database required (uses a local text file)

## Example

```text
1. Save Password
2. Get Password
3. Exit

Choose an option: 1
Enter website: github
Enter password: MySecurePass123

Choose an option: 2
Enter website: github
Password copied to clipboard!
```

## Technologies Used

* Python
* `pyperclip`
* File handling

## Project Structure

```text
password-manager/
├── password_manager.py
├── passwords.txt
└── README.md
```

## How to Run

1. Install the required dependency:

```bash
pip install -r requirements.txt
```

2. Run the program:

```bash
python password_manager.py
```

## What I Learned

* Reading and writing files in Python
* Organizing a menu-driven command-line application
* Working with external libraries (`pyperclip`)
* Basic data storage and retrieval logic
* Improving usability with clipboard automation

## Note

This project stores passwords in a plain text file and is intended for **learning purposes only**. A future version could use encryption and a master password for improved security.

## Author

**Revanth Bhanu**

A practical Python utility created as part of my programming and automation learning journey.
