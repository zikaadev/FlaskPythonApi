from flask import Flask, jsonify

app = Flask(__name__)
print(__name__)



books = [
    {
        'name': 'Green Eggs and Ham',
        'price': 7.99,
        'isbn': 987039400165
    },
    {
        'name': 'The Cat In The Hat ',
        'price':6.99,
        'isbn': 98723710000193
    }
]

#GET books
@app.route('/books')
def get_books():
    return jsonify({'books': books})


@app.route('books/<int:isbn>')
def get_book_by_isbn(isbn):
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                'name': book["name"],
                'price': book["price"]
            }
        return jsonify(return_value)


app.run(port=5000)


# __name__ == "__main__"
#
# __name__ == "modulesName"