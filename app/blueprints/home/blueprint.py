
from flask import Blueprint, render_template, request

from models import product_catalog
from models import book_neighbors

from middlewares.auth import auth_optional

home_page = Blueprint('home_page', __name__)


@home_page.route('/', methods = ['POST', 'GET'])
@auth_optional
def display(auth_context):
    """
    View function for displaying the home page.

    Parameters:
       auth_context (dict): The authentication context of request.
                            See middlewares/auth.py for more information.
    Output:
       Rendered HTML page.
    """
    
    if request.method == 'GET':

      products = product_catalog.list_products()
      
      return render_template('home.html',
                              products=products,
                              auth_context=auth_context,
                              bucket=product_catalog.BUCKET)
    else:

      # products = product_catalog.list_products()

      title = request.form['title']
      query_books = book_neighbors.get_book(title)

      products = [{'title':book[0], 'author':book[1], 'id':book[2], 'image':book[3]} for book in query_books]
      
      print(title, products)

      # products = []
      # for book in books:
      #    products.append(product_catalog.get_book(book['id']))

      return render_template('home.html',
                              products=products,
                              # books=books,
                              auth_context=auth_context,
                              bucket=product_catalog.BUCKET)