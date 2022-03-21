from flask import Flask, request, jsonify

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from flask_cors import CORS, cross_origin 

# Use the application default credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
app = Flask(__name__)
CORS(app)

# this is not dynamic yet 
@app.route("/orders", methods=["GET"]) 
@cross_origin()
def getOrders():
    orders = db.collection('orders').document('Qt1UfT9hExtldgn2qsxl').get()
    return orders.to_dict()

# this creates a empty document first newOrderDoc, then fills up the details with the orderData params 
@app.route("/order", methods=["GET","POST"])
@cross_origin()
def createOrder():
    orderData = request.get_json() 
    newOrderDoc = db.collection('orders').document()
    newOrderDoc.set(
        {   
    # "buyerID" : orderData['buyerID'],
    # "sellerID" : orderData['sellerID'],
    # "status": orderData['status'],
    # "cart" : orderData['cart'],
    # "collectionTime" : orderData['collectionTime']

    "status": orderData['status'],
    "uid" : orderData['UID'],
    "subtotal": orderData['subtotal'],
    "storeID" : orderData['storeID'],
    "collectionTime" : orderData['collectionTime'],
     "cart" : {
        orderData['foodName']: {
        "counter" : orderData['counter'],
        "foodDesc" : orderData['foodDesc'],
        "foodName" : orderData['foodName'],
        "image": orderData['image'],
        "oldPrice": orderData['oldPrice'],
        "price": orderData['newPrice'],
        "quantity": orderData['quantity'],
        "shopKey": orderData['storeID'] 
        }
    }
}
    )
    return 'order added to firebase successfully'

# this updates the orders by taking in the orderID and the new status to update 
@app.route("/orderUpdate", methods=["GET","POST"])
@cross_origin()
def updateOrder():
    orderToUpdate = request.get_json()
    order = db.collection('orders').document(orderToUpdate['orderID'])
    order.update({
        'status': orderToUpdate['status']
    })
    return "order status updated successfully"


if __name__ == "__main__":
    app.run(port=5000, debug=True)







