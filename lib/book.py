# Inside book.py

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count


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

class Shoe:
    def __init__(self, brand, size, material):
        self.brand = brand
        self.size = size  
        self.material = material

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            raise TypeError("size must be an integer")
    
    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

# Test the Book class
def test_book():
    book = Book("Python Programming", 272, "John Smith", "Programming")
    
    # Test initialization with title, author, genre, and page_count
    assert book.title == "Python Programming"
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

# Test the Shoe class
def test_shoe():
    shoe = Shoe("Nike", 9, "leather")
    
    # Test initialization with brand, size, and material
    assert shoe.brand == "Nike"
    assert shoe.size == 9  # Ensure size is set correctly
    assert shoe.material == "leather"
    
    # Test setting size
    shoe.size = 10
    assert shoe.size == 10
    
    # Test condition before setting size
    assert shoe.size is not None
    
    # Test setting size with non-integer value
    try:
        shoe.size = "not an integer"
    except TypeError as e:
        assert str(e) == "size must be an integer"
    else:
        raise AssertionError("Expected TypeError was not raised")
    
    print("All tests passed!")

if __name__ == "__main__":
    test_book()
    test_shoe()
