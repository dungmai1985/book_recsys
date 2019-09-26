"""
A collection of helper functions for order related operations.
"""


from dataclasses import asdict
import uuid

from google.cloud import firestore
import pandas as pd

firestore = firestore.Client()

books = pd.read_csv("./dataset/book_id.csv", low_memory=False)
books = books.to_dict(orient ='records')
for book in books[:5]:
   book_id = uuid.uuid4().hex
   firestore.collection('dataset-book').document(book_id).set(book)


