class Book:
    def __init__(self, title, page_count, author=None, genre=None):
        self.title = title
        self.author = author
        self.genre = genre
        self._page_count = None  # Initialize _page_count attribute to None
        self.page_count = page_count  # Use the property setter to set the page_count

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            raise TypeError("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    page_count = property(get_page_count, set_page_count)

# Test the Book class
def test_book():
    book = Book("Python Programming", 272, "John Smith", "Programming")
    
    # Test initialization with title, author, genre, and page_count
    assert book.title == "Python Programming"
    assert book.author == "John Smith"
    assert book.genre == "Programming"
    assert book.page_count == 272  # Ensure page_count is set correctly
    
    # Test assigning a page count
    book.page_count = 200
    assert book.page_count == 200
    
    # Test condition before setting page count
    assert book.page_count is not None
    
    # Test setting page count with non-integer value
    try:
        book.page_count = "not an integer"
    except TypeError as e:
        assert str(e) == "page_count must be an integer"
    else:
        raise AssertionError("Expected TypeError was not raised")
    
    print("All tests passed!")

if __name__ == "__main__":
    test_book()
