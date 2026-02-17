from book_class import Book
from library_system import Book as BaseBook, EBook, PrintBook, Library

def demo_book_class():
    print("=== Demo: book_class ===")
    my_book = Book("1984", "George Orwell", 1949)

    print(my_book)          # Uses __str__
    print(repr(my_book))    # Uses __repr__

    del my_book             # Triggers __del__


def demo_library_system():
    print("\n=== Demo: library_system ===")
    my_library = Library()

    classic_book = BaseBook("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()


if __name__ == "__main__":
    demo_book_class()
    demo_library_system()
