class LibrarySystem:
    """
    A Mini Library Management System that handles books, members, and borrowing operations.
    Uses dictionaries for books, lists for members, and tuples for genres.
    """

    def __init__(self):
        # Dictionary for books: ISBN -> book details
        self.books = {}

        # List of dictionaries for members
        self.members = []

        # Tuple for valid genres (immutable)
        self.genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Biography")

    def add_book(self, isbn, title, author, genre, total_copies):
        """
        Add a book to the library if ISBN is unique and genre is valid.

        Args:
            isbn (str): Unique ISBN identifier
            title (str): Book title
            author (str): Book author
            genre (str): Book genre (must be in valid genres)
            total_copies (int): Total number of copies

        Returns:
            bool: True if successful, False otherwise
        """
        # Check if ISBN already exists
        if isbn in self.books:
            print(f"Error: Book with ISBN {isbn} already exists.")
            return False

        # Check if genre is valid
        if genre not in self.genres:
            print(f"Error: Invalid genre '{genre}'. Valid genres are: {self.genres}")
            return False

        # Add book to dictionary
        self.books[isbn] = {
            'title': title,
            'author': author,
            'genre': genre,
            'total_copies': total_copies,
            'available_copies': total_copies
        }
        print(f"Successfully added book: '{title}' by {author}")
        return True

    def add_member(self, member_id, name, email):
        """
        Add a member to the library system.

        Args:
            member_id (str): Unique member ID
            name (str): Member name
            email (str): Member email

        Returns:
            bool: True if successful, False otherwise
        """
        # Check if member ID already exists
        for member in self.members:
            if member['member_id'] == member_id:
                print(f"Error: Member with ID {member_id} already exists.")
                return False

        # Add member to list
        self.members.append({
            'member_id': member_id,
            'name': name,
            'email': email,
            'borrowed_books': []  # List of ISBNs
        })
        print(f"Successfully added member: {name} (ID: {member_id})")
        return True

    def search_books(self, search_term, search_by="title"):
        """
        Search books by title or author.

        Args:
            search_term (str): Term to search for
            search_by (str): "title" or "author"

        Returns:
            list: List of matching books
        """
        results = []
        search_term = search_term.lower()

        for isbn, book in self.books.items():
            if search_by == "title" and search_term in book['title'].lower():
                results.append((isbn, book))
            elif search_by == "author" and search_term in book['author'].lower():
                results.append((isbn, book))

        print(f"Found {len(results)} books matching '{search_term}' by {search_by}")
        return results

    def update_book(self, isbn, **kwargs):
        """
        Update book details.

        Args:
            isbn (str): ISBN of book to update
            **kwargs: Fields to update (title, author, genre, total_copies)

        Returns:
            bool: True if successful, False otherwise
        """
        if isbn not in self.books:
            print(f"Error: Book with ISBN {isbn} not found.")
            return False

        book = self.books[isbn]

        for key, value in kwargs.items():
            if key in book:
                if key == 'genre' and value not in self.genres:
                    print(f"Error: Invalid genre '{value}'. Valid genres are: {self.genres}")
                    return False
                book[key] = value
                print(f"Updated {key} to '{value}' for book {isbn}")

        return True

    def update_member(self, member_id, **kwargs):
        """
        Update member details.

        Args:
            member_id (str): Member ID to update
            **kwargs: Fields to update (name, email)

        Returns:
            bool: True if successful, False otherwise
        """
        member = self._find_member(member_id)
        if not member:
            print(f"Error: Member with ID {member_id} not found.")
            return False

        for key, value in kwargs.items():
            if key in member and key != 'member_id' and key != 'borrowed_books':
                member[key] = value
                print(f"Updated {key} to '{value}' for member {member_id}")

        return True

    def delete_book(self, isbn):
        """
        Delete a book only if no copies are borrowed.

        Args:
            isbn (str): ISBN of book to delete

        Returns:
            bool: True if successful, False otherwise
        """
        if isbn not in self.books:
            print(f"Error: Book with ISBN {isbn} not found.")
            return False

        book = self.books[isbn]

        # Check if any copies are borrowed
        if book['available_copies'] < book['total_copies']:
            print(f"Error: Cannot delete book '{book['title']}' - some copies are still borrowed.")
            return False

        del self.books[isbn]
        print(f"Successfully deleted book with ISBN {isbn}")
        return True

    def delete_member(self, member_id):
        """
        Delete a member only if they have no borrowed books.

        Args:
            member_id (str): Member ID to delete

        Returns:
            bool: True if successful, False otherwise
        """
        member = self._find_member(member_id)
        if not member:
            print(f"Error: Member with ID {member_id} not found.")
            return False

        # Check if member has borrowed books
        if member['borrowed_books']:
            print(f"Error: Cannot delete member {member_id} - they still have borrowed books.")
            return False

        self.members.remove(member)
        print(f"Successfully deleted member with ID {member_id}")
        return True

    def borrow_book(self, member_id, isbn):
        """
        Allow a member to borrow a book if available and within limit.

        Args:
            member_id (str): Member ID
            isbn (str): ISBN of book to borrow

        Returns:
            bool: True if successful, False otherwise
        """
        member = self._find_member(member_id)
        if not member:
            print(f"Error: Member with ID {member_id} not found.")
            return False

        if isbn not in self.books:
            print(f"Error: Book with ISBN {isbn} not found.")
            return False

        book = self.books[isbn]

        # Check if member has reached borrowing limit (3 books)
        if len(member['borrowed_books']) >= 3:
            print(f"Error: Member {member_id} has reached the borrowing limit of 3 books.")
            return False

        # Check if book is available
        if book['available_copies'] <= 0:
            print(f"Error: No copies available for '{book['title']}'")
            return False

        # Borrow the book
        member['borrowed_books'].append(isbn)
        book['available_copies'] -= 1

        print(f"Member {member_id} successfully borrowed '{book['title']}'")
        return True

    def return_book(self, member_id, isbn):
        """
        Return a borrowed book.

        Args:
            member_id (str): Member ID
            isbn (str): ISBN of book to return

        Returns:
            bool: True if successful, False otherwise
        """
        member = self._find_member(member_id)
        if not member:
            print(f"Error: Member with ID {member_id} not found.")
            return False

        if isbn not in self.books:
            print(f"Error: Book with ISBN {isbn} not found.")
            return False

        # Check if member has borrowed this book
        if isbn not in member['borrowed_books']:
            print(f"Error: Member {member_id} has not borrowed book with ISBN {isbn}")
            return False

        # Return the book
        member['borrowed_books'].remove(isbn)
        self.books[isbn]['available_copies'] += 1

        print(f"Member {member_id} successfully returned '{self.books[isbn]['title']}'")
        return True

    def _find_member(self, member_id):
        """
        Helper function to find a member by ID.

        Args:
            member_id (str): Member ID to find

        Returns:
            dict or None: Member dictionary if found, None otherwise
        """
        for member in self.members:
            if member['member_id'] == member_id:
                return member
        return None

    def display_books(self):
        """Display all books in the library."""
        print("\n=== ALL BOOKS ===")
        for isbn, book in self.books.items():
            status = "Available" if book['available_copies'] > 0 else "Not Available"
            print(f"ISBN: {isbn}, Title: '{book['title']}', Author: {book['author']}, "
                  f"Genre: {book['genre']}, Available: {book['available_copies']}/{book['total_copies']} - {status}")

    def display_members(self):
        """Display all members and their borrowed books."""
        print("\n=== ALL MEMBERS ===")
        for member in self.members:
            borrowed_books = []
            for isbn in member['borrowed_books']:
                if isbn in self.books:
                    borrowed_books.append(self.books[isbn]['title'])
            print(f"ID: {member['member_id']}, Name: {member['name']}, Email: {member['email']}, "
                  f"Borrowed: {len(borrowed_books)} books: {borrowed_books}")
