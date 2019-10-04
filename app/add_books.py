"""
A collection of helper functions for order related operations.
"""


from dataclasses import asdict
import uuid

from google.cloud import firestore
import pandas as pd

firestore = firestore.Client()

books = pd.read_csv("./dataset/books_ratings.csv", low_memory=False)
books = books.to_dict(orient ='records')
for book in books[:3000]:
   book_id = uuid.uuid4().hex
   firestore.collection('book_ratings').document(book_id).set(book)


