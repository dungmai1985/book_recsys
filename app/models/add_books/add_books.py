"""
A collection of helper functions for order related operations.
"""


from dataclasses import asdict
import uuid

from google.cloud import firestore

from .data_classes import Book

firestore = firestore.Client()

def add_book(book):
    """
    Helper function for adding an book.

    Parameters:
       book (Book): An Book object.

    Output:
       The ID of the book.
    """

    book_id = uuid.uuid4().hex
    firestore.collection('dataset-book').document(book_id).set(asdict(book))
    return book_id


def get_book(book_id):
    """
    Helper function for getting an book.

    Parameters:
       book_id (str): The ID of the book.

    Output:
       An Book object.
    """

    book_data = firestore.collection('dataset-book').document(book_id).get()
    return Book.deserialize(book_data)
