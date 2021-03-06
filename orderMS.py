# from audioop import cross
from pydoc import doc
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Use the application default credentials

cred = credentials.Certificate(
    {
        "type": "service_account",
        "project_id": "orderms-c7faa",
        "private_key_id": "14091f0e79b1fc081f64a7842d32669fe1fed8ad",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC48ADOL8/RJvIJ\nkU+tMSRP/Sio3JJfZFLjW2W0PaWfYbL+UGzI70hOQEPMwSx34uL21vsuqaKvZlb2\n360FO76PxkwHJ/eShgcJb5p1H1ia7LrkpB0Z+TB5yPfHTYSMX1NGrRCK8tk906Rj\nMtUpelgdZVbpXGublMZ/Ljc8jm/ASVD0jm2M1fUcy3S0Td87bRzuyDXFvr7eP4PY\nfn12n+2cFl4KlvYrXultJIVtC/tbMOyJikni9KB29w2K3IFHooeS47xdv4OltZ97\nWGIxbkT0SJInnKmsC979E1BHtqKtsPVJqvl0CsV56G6aDCXtUU8GyMDqvVLB0rgz\nTiyVkW6PAgMBAAECggEAVBrN+vcSd0dTZpd/mT+SiJAUqCrbpGc/LOeZaq1of4HS\ngca4mm77vp6KVvl5DDKSTni5deCuvD76CL7zdEBV6xPe6pg6BphOZfOr1l0Bkj9b\nxXR/SZsieRg02x49TAtkF23IarCDrJLuHTD2cS0TGpdGPc2KoJA574folfEfEF5g\n0FxmQJhLTkaTjHQJzK4IgB+sPonSNHmycGBE2XDVqjxA4AqWm6meCwoGgi/DvRlg\n9qFmLBTkCEzQoWGwIZUM0QftCFhc5FOWpWTBvlLaFViP5dhSeleyLEsKAzl9rdSA\nx/O2cxlfHGDA4SO2a4pzD+ocNK6GqaunWtw3UNbl8QKBgQDsLKZLKTEAlsEjbf6v\nGNPhnIZo9Snu18pUkBI44Ke5iggQo3eLUnfYIGm6WmqZfcXizXFbZ4bPWJspwC2H\n5fhcvcOCNXgk175srm95IydUWjgfHhcMPtK2dK3ldJzpCwvq00v3na79FM5+a3rY\n7RTlpoy55m+G/01XX3Ks0T9pkQKBgQDIdkffwxRqSEr0GhUNrWG4xn+5zgi0vjfd\nyo2tqmSxq96dEx+4lA6wM1fndoEn5ZgY1JP+BTa7j+TKhBke5bPIrouAtj1NN2DI\nYQq1R1tFg5W0wTlOBXnQb8k1oyndgpZ8Ps16uZB9QOchV/42cpCosXL+X5syDXFc\nUoX4NKZGHwKBgQDWmHd9oe8JpvHVnJOnTDryLEShR+sTP/Zzwfkcv10HpNlRLQdp\ni8SjmEgZcSCdWYAeZihTMo13B/7s/9cfPaHfuvnT7Xu+ll5L6HAXtQ5+gf+unqu4\nj7js2rZL4RrWUhhBBj9nvlqLUYWTr1uPklTDmwMRw8Wg94eyFWNgjj09UQKBgGOg\nfUoVDwFfWnkEuW/puoZ1iKcUYblKTEObVlx4McEndOTFy18VnlMtwUNU3w2wCq5U\ngBSgDLqc4g1QJ5f2eyqCrOxUJhVJL32G1SaRByh+JBoIae1/xTG1TN+ubrEbJKUt\nJTwYG1pUtkoZDEuNFp3wSwFnDJ+MlMlYbiKUMArrAoGAZqT4XOKKjRbLUeOkmzAX\nz58snQrr3/aXGmQB77DTsfEaqbCpIZpcocFUAR9xjse2VDau2oxI6u4ClX9VfUaL\n5Zu391JGRFDjbiLICRlvT8PqayK85tJ2/9iP/4xVMn9E3bEdDrFpJ3Bky/yzc2RN\nNn/HZZ7K1Uc+Ze6H6DE4WBs=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-pdf77@orderms-c7faa.iam.gserviceaccount.com",
        "client_id": "104133511923619539128",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-pdf77%40orderms-c7faa.iam.gserviceaccount.com"
    }

)
firebase_admin.initialize_app(cred)

db = firestore.client()
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def testContainer():
    return 'welcome to orderMS!!!!!'

# this is not dynamic yet 
@app.route("/getOrderById", methods=["GET","POST"]) 
@cross_origin()
def getOrders():
    orderData = request.get_json()
    orderID = orderData["orderID"]
    orders = db.collection('orders').document(orderID).get()
    if orders: 
        return orders.to_dict()
    else: 
        return jsonify({"code": 404, "message": "Order not found"})

# this creates a empty document first newOrderDoc, then fills up the details with the orderData params 
@app.route("/createNewOrder", methods=["GET","POST"])
@cross_origin()
def createOrder():
    data = request.get_json()
    orderData = data['order']
    newOrderDoc = db.collection('orders').document()

    cart_array = []
    for order in orderData['cart']:
        counter = order['counter']
        foodDesc = order['foodDesc']
        foodName = order['foodName']
        image = order['image']
        oldPrice = order['oldPrice']
        price=  order['price']
        quantity=  order['quantity']
        cart_array.append(
            {
                "counter" : counter,
                "foodDesc" : foodDesc,
                "foodName" : foodName,
                "image": image,
                "oldPrice": oldPrice,
                "price": price,
                "quantity": quantity,
                "shopKey": orderData['storeID'] 
                }
        )
       
    #  loop through the cart that you receive
    #  take each object in the array and map it's values to a temp object
    #  push this temp object into the array
    try:
        newOrderDoc.set(
        {   

            "status": orderData['status'],
            "uid" : orderData['uid'],
            "subtotal": orderData['subtotal'],
            "storeID" : orderData['storeID'],
            "collectionTime" : orderData['collectionTime'],
            "cart" : cart_array
                }
            )
        return jsonify(
            {
                "code": 201,
                "message": "Order added to firebase successfully",
                "order" : {   
                    "orderID" : newOrderDoc.id,
                    "status": orderData['status'],
                    "uid" : orderData['uid'],
                    "subtotal": orderData['subtotal'],
                    "storeID" : orderData['storeID'],
                    "collectionTime" : orderData['collectionTime'],
                    "cart" : cart_array
                }
            })
  
    except:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured when creating order",
                
            }), 
        
    

# this updates the orders by taking in the orderID and the new status to update 
@app.route("/orderUpdate", methods=["GET","POST","PUT"])
@cross_origin()
def updateOrder():
    orderToUpdate = request.get_json()
    order = db.collection('orders').document(orderToUpdate['orderID'])
    try:
        order.update({
        'status': orderToUpdate['status']
    })
    except:
        return jsonify({"code": 404, "message": "Error occured when updating order status"})
            
    return jsonify({"code": 200, "message": "Order status updated successfully"})

@app.route("/getAllOrders", methods=["GET","POST"])
@cross_origin()
def getAllOrders():
    orderResults = {}
    docs = db.collection(u'orders').stream()

    for doc in docs:
        orderResults[doc.id] = doc.to_dict()
        # return(f'{doc.id} => {doc.to_dict()}')

    if len(orderResults)!= 0 : 
        return orderResults

    else:
        return jsonify(
            {
                "code": 404,
                "message": "There are no orders."
            }
        )
    

@app.route("/deleteOrder", methods=["DELETE"])
@cross_origin()
def deleteOrder(): 
    orderToDelete = request.get_json()
    order = db.collection('orders').document(orderToDelete['orderID'])

    try: 
       order.delete()
       return jsonify({"code": 200, "message": "Successfully deleted order"})
   
    except:
        return jsonify({"code": 404, "message": "Error occured when deleting order"})
        
        

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5300, debug=True)


# docs = db.collection(u'cities').stream()

# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')




