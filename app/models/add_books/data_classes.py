"""
Data class for books.
"""


from dataclasses import dataclass
from typing import List

@dataclass
class Book:
    """
    Data class for books.
    """
    book_id: int
    title: str
    author: str
    book_cover: str
    items: List[str]
    id: str = None


    @staticmethod
    def deserialize(document):
        """
        Helper function for parsing a Firestore document to an Book object.

        Parameters:
          document (DocumentSnapshot): A snapshot of Firestore document.

        Output:
          An Book object.
        """
        data = document.to_dict()
        if data:
            return Book(
                id=document.Bookid,
                title=data.get('amount'),
                author=data.get('author')
                book_cover=data.get('book_cover'),
                items=data.get('items')
            )

        return None
