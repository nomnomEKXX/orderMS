from flask import Flask, request, jsonify

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
app = Flask(__name__)

@app.route("/orders", methods=["GET"])
def getOrders():
    orders = db.collection('orders').document('f4zxhpSOXnINCmLv7MA3').collection('buyer').document('KVjTkmQqM8BWKhkbFL5m').get()
    return orders.to_dict()

if __name__ == "__main__":
    app.run(port=5000, debug=True)



# @app.route("/orders")
# def get_all():
#     booklist = Book.query.all()
#     if len(booklist):
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "books": [book.json() for book in booklist]
#                 }
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message": "There are no books."
#         }
#     ), 404


# ---------------------------------------------------------------------------

# from flask import Flask, request, jsonify, render_template

# import firebase_admin
# from firebase_admin import firestore
# from firebase_admin import credentials

# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# app = Flask(__name__)

# @app.route("/addbuyer", methods=["POST", "GET"])
# def home():
#     if request.method == "POST":
#         pass
#     return render_template('home.html')
    

# @app.route("/buyers")
# def get_all_buyer():
#     string = ""
#     buyer_doc = db.collection('persons').stream()
#     for doc in buyer_doc:
#         #return jsonify(doc.to_dict()), 200
#         string += str(doc.to_dict())
#         string += "\n"
#     return string
        
    

# @app.route("/add/<string:buyerName>/<string:buyerID>", methods=["POST", "GET"])
# def add_buyer(buyerName, buyerID):
#     db.collection('persons').add({'name':buyerName,'age':buyerID})
#     return "working"


# if __name__ == "__main__":
#     app.run(port=5000, debug=True)






# # import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

# # Fetch the service account key JSON file contents
# cred = credentials.Certificate('nomnom-db-firebase-adminsdk-bhktu-52a40c9f91.json')
# # Initialize the app with a service account, granting admin privileges
# firebase_admin.initialize_app(cred, {
#     'databaseURL': "https://nomnom-db-default-rtdb.asia-southeast1.firebasedatabase.app"
# })

# ref = db.reference('Database reference')
# print(ref.get())
