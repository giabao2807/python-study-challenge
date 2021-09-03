class Book:
    """A class for e-book"""
    
    def __init__(self, 
                 title: str,
                 authors: str = '',
                 publisher: str = '',
                 year: int = 2020,
                 edition: int = 1):
        """Hàm tạo của class"""
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.year = year
        self.edition = edition
        
    def print(self):
        """Print the book infor"""
        print(f"{self.title} by {self.authors}, {self.edition} edition, {self.publisher}, {self.year}")