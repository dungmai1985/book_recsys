from google.cloud import firestore
import pandas as pd

firestore = firestore.Client()

# products = firestore.collection('dataset-book').where(u'Book-Title', u'==', u'Deaf Culture Our Way').get()
products = firestore.collection('dataset-book').where('Publisher', '==', 'Ballantine Books').get()
product_list = [product.to_dict() for product in list(products)]

print(product_list)