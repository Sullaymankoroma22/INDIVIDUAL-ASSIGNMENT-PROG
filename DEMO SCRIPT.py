from operations import LibrarySystem


def demo_library_system():
    """
    Demonstration script showing the complete functionality
    of the Mini Library Management System.
    """

    print("=== MINI LIBRARY MANAGEMENT SYSTEM DEMO ===\n")

    # Initialize the library system
    library = LibrarySystem()

    # Step 1: Add books to the library
    print("1. ADDING BOOKS TO LIBRARY")
    print("-" * 30)
    library.add_book("9780134853987", "Clean Code", "Robert Martin", "Non-Fiction", 4)
    library.add_book("9780201633610", "Design Patterns", "Gamma et al.", "Non-Fiction", 3)
    library.add_book("9780451524935", "1984", "George Orwell", "Fiction", 5)
    library.add_book("9780345339683", "The Hobbit", "J.R.R. Tolkien", "Fiction", 2)
    library.add_book("9780441013593", "Dune", "Frank Herbert", "Sci-Fi", 3)
    print()

    # Step 2: Add members
    print("2. ADDING MEMBERS")
    print("-" * 30)
    library.add_member("MEM001", "John Smith", "john.smith@email.com")
    library.add_member("MEM002", "Sarah Johnson", "sarah.j@email.com")
    library.add_member("MEM003", "Mike Davis", "mike.davis@email.com")
    print()

    # Step 3: Display current state
    library.display_books()
    library.display_members()

    # Step 4: Search for books
    print("\n3. SEARCHING FOR BOOKS")
    print("-" * 30)
    print("Searching for books with 'Design' in title:")
    results = library.search_books("Design", "title")
    for isbn, book in results:
        print(f"  - {book['title']} by {book['author']}")

    print("\nSearching for books by 'Orwell':")
    results = library.search_books("Orwell", "author")
    for isbn, book in results:
        print(f"  - {book['title']} by {book['author']}")
    print()

    # Step 5: Borrow books
    print("4. BORROWING BOOKS")
    print("-" * 30)
    print("John borrowing books:")
    library.borrow_book("MEM001", "9780134853987")  # Clean Code
    library.borrow_book("MEM001", "9780345339683")  # The Hobbit

    print("\nSarah borrowing books:")
    library.borrow_book("MEM002", "9780451524935")  # 1984
    library.borrow_book("MEM002", "9780441013593")  # Dune

    print("\nMike trying to borrow when copies are limited:")
    library.borrow_book("MEM003", "9780345339683")  # The Hobbit - should fail
    print()

    # Step 6: Display current state after borrowing
    library.display_books()
    library.display_members()

    # Step 7: Update operations
    print("\n5. UPDATING INFORMATION")
    print("-" * 30)
    library.update_book("9780134853987", total_copies=6)  # Increase copies
    library.update_member("MEM001", email="john.newemail@email.com")
    print()

    # Step 8: Return books
    print("6. RETURNING BOOKS")
    print("-" * 30)
    library.return_book("MEM001", "9780134853987")
    library.return_book("MEM002", "9780451524935")
    print()

    # Step 9: Delete operations
    print("7. DELETING RECORDS")
    print("-" * 30)
    # Add a temporary book and member to delete
    library.add_book("9999999999", "Temporary Book", "Temp Author", "Mystery", 1)
    library.add_member("MEM999", "Temp Member", "temp@email.com")

    print("Trying to delete book with borrowed copies:")
    library.delete_book("9780345339683")  # Should fail

    print("\nDeleting temporary records:")
    library.delete_book("9999999999")
    library.delete_member("MEM999")
    print()

    # Final state
    print("8. FINAL STATE OF LIBRARY")
    print("-" * 30)
    library.display_books()
    library.display_members()

    print("\n=== DEMO COMPLETED SUCCESSFULLY ===")


if __name__ == "__main__":
    demo_library_system()
