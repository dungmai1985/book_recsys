from dataclasses import asdict
import os
import uuid

from google.cloud import firestore

from .data_classes import Product


BUCKET = os.environ.get('GCS_BUCKET')

firestore_client = firestore.Client()


def add_product(product):
    """
    Helper function for adding a product.

    Parameters:
       product (Product): A Product object.

    Output:
       The ID of the product.
    """

    product_id = uuid.uuid4().hex
    firestore_client.collection('book_data').document(product_id).set(asdict(product))
    return product_id

def get_book(book_id):
    """
    Helper function for getting a book.

    Parameters:
       book_id (str): The ID of the book.

    Output:
       A Product object.
    """

    book = firestore_client.collection('book_data').document(book_id).get()
    return Product.deserialize(book)


def list_products():
    """
    Helper function for listing products.

    Parameters:
       None.

    Output:
       A list of Product objects.
    """

    products = firestore_client.collection('book_ratings').order_by('book_id').get()
    product_list = [Product.deserialize(product) for product in list(products)]
    return product_list

def calculate_total_price(product_ids):
    """
    Helper function for calculating the total price of a list of products.

    Parameters:
       product_ids (List[str]): A list of product IDs.

    Output:
       The total price.
    """

    total = 0
    for product_id in product_ids:
        product = get_product(product_id)
        total += product.price
    return total