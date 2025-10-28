# Mini Library Management System

A Python-based library management system that handles books, members, and borrowing operations using fundamental data structures.

## Features

- **Book Management**: Add, search, update, and delete books
- **Member Management**: Add, update, and delete members
- **Borrowing System**: Borrow and return books with limits (max 3 books per member)
- **Validation**: ISBN uniqueness, genre validation, borrowing limits
- **Search Functionality**: Search books by title or author

## Data Structures Used

- **Dictionary**: For storing books (ISBN as key, book details as value)
- **List**: For storing members (list of dictionaries)
- **Tuple**: For storing valid genres (immutable collection)

## Files Structure

- `operations.py` - Main library system implementation
- `test.py` - Comprehensive test suite with assertions
- `demo.py` - Demonstration script showing all features
- `README.md` - This documentation file

## How to Run

### Running Tests
```bash
python test.py
<img width="468" height="378" alt="image" src="https://github.com/user-attachments/assets/87d95b05-0d40-42c4-a49f-a2e0fb0475c4" />

