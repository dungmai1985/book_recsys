# For more info: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    """
    Data class for products.
    """
    name: str
    author: str
    book_id: int
    id: str = None


    @staticmethod
    def deserialize(document):
        """
        Helper function for parsing a Firestore document to a Product object.

        Parameters:
           document (DocumentSnapshot): A snapshot of Firestore document.

        Output:
           A Product object.
        """
        data = document.to_dict()
        if data:
            return Product(
                id=document.id,
                name=data.get('book_title'),
                author=data.get('book_author'),
                book_id=data.get('book_id')
                
            )
        return None
