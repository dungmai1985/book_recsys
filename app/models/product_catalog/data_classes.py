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
    publisher: str
    # labels: List[str]
    image: str
    year: str
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
                name=data.get('Book-Title'),
                author=data.get('Book-Author'),
                publisher=data.get('Publisher'),
                image=data.get('Image-URL-S'),
                year = data.get('Year-Of-Publication')
            )
        return None
