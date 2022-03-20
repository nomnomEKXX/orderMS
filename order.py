from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/buyers")
def get_all():
	pass

# this one needs to be changed 
@app.route("/book/<string:isbn13>")
def find_by_isbn13(isbn13):
	pass

# this one needs to be changed to depending on how we want to filter the orders 
@app.route("/book/<string:isbn13>", methods=['POST'])
def create_book(isbn13):
	pass

if __name__ == '__main__':
    app.run(port=5000, debug=True)
