from operations import LibrarySystem


def test_library_system():
    """Comprehensive test suite for the Library Management System"""

    # Initialize library system
    library = LibrarySystem()

    print("=== STARTING LIBRARY SYSTEM TESTS ===\n")

    # Test 1: Add books with valid and invalid genres
    print("Test 1: Adding books")
    assert library.add_book("1234567890", "Python Programming", "John Doe", "Non-Fiction", 5) == True
    assert library.add_book("0987654321", "Sci-Fi Adventure", "Jane Smith", "Sci-Fi", 3) == True
    assert library.add_book("1234567890", "Duplicate Book", "Author", "Fiction", 2) == False  # Duplicate ISBN
    assert library.add_book("1111111111", "Invalid Genre", "Author", "Romance", 1) == False  # Invalid genre
    print("✓ Test 1 passed: Book addition with validation\n")

    # Test 2: Add members
    print("Test 2: Adding members")
    assert library.add_member("M001", "Alice Johnson", "alice@email.com") == True
    assert library.add_member("M002", "Bob Brown", "bob@email.com") == True
    assert library.add_member("M001", "Charlie Davis", "charlie@email.com") == False  # Duplicate ID
    print("✓ Test 2 passed: Member addition with validation\n")

    # Test 3: Search books
    print("Test 3: Searching books")
    results = library.search_books("Python", "title")
    assert len(results) == 1
    assert results[0][1]['title'] == "Python Programming"

    results = library.search_books("Jane", "author")
    assert len(results) == 1
    assert results[0][1]['author'] == "Jane Smith"

    results = library.search_books("Nonexistent", "title")
    assert len(results) == 0
    print("✓ Test 3 passed: Book search functionality\n")

    # Test 4: Borrow and return books
    print("Test 4: Borrowing and returning books")
    assert library.borrow_book("M001", "1234567890") == True
    assert library.borrow_book("M001", "0987654321") == True
    assert library.borrow_book("M001", "1234567890") == False  # Already borrowed by same member
    assert library.borrow_book("M002", "1234567890") == True  # Different member can borrow same book

    # Test borrowing limit
    assert library.borrow_book("M001", "1234567890") == False  # Already borrowed
    library.add_book("2222222222", "Third Book", "Author", "Fiction", 2)
    assert library.borrow_book("M001", "2222222222") == True  # Third book
    library.add_book("3333333333", "Fourth Book", "Author", "Mystery", 1)
    assert library.borrow_book("M001", "3333333333") == False  # Exceeds limit

    # Test returning
    assert library.return_book("M001", "1234567890") == True
    assert library.return_book("M001", "1234567890") == False  # Not currently borrowed
    print("✓ Test 4 passed: Borrowing and returning with limits\n")

    # Test 5: Update and delete operations
    print("Test 5: Update and delete operations")
    assert library.update_book("1234567890", title="Python Programming Updated") == True
    assert library.books["1234567890"]['title'] == "Python Programming Updated"

    assert library.update_member("M001", name="Alice Smith") == True
    assert library._find_member("M001")['name'] == "Alice Smith"

    # Try to delete book with borrowed copies
    assert library.delete_book("0987654321") == False

    # Return all books first
    library.return_book("M001", "0987654321")
    library.return_book("M001", "2222222222")
    library.return_book("M002", "1234567890")

    # Now delete should work
    assert library.delete_book("0987654321") == True
    assert library.delete_member("M001") == True
    print("✓ Test 5 passed: Update and delete operations\n")

    print("=== ALL TESTS PASSED SUCCESSFULLY ===")


if __name__ == "__main__":
    test_library_system()
