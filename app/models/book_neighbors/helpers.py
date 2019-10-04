
import os
import uuid

from google.cloud import bigquery

from .data_classes import Product


BUCKET = os.environ.get('GCS_BUCKET')

client = bigquery.Client()


def get_book(title):
    """
    Helper function for getting a product.

    Parameters:
       product_id (str): The ID of the product.

    Output:
       A Product object.
    """

    query = "SELECT neighbor_title, neighbor_author, book_id, image FROM `book_neighbors.book_neighbor` WHERE target_book LIKE {};".format(repr(title+'%'))

    job = client.query(query)
    return job.result()
    


