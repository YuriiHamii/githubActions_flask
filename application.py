from flask import Flask, request, jsonify


application = Flask(__name__)

  
products = [
    {"id": 1, "name": "CocaCola", "descriprion": "Lime", "price": 1.5, "tax": 0.2},
    {"id": 2, "name": "Pepsi", "descriprion": "Orange", "price": 1.8, "tax": 0.3},
    {"id": 3, "name": "Fanta", "descriprion": None, "price": 2.0, "tax": 0.4, "tags": []},
    {"id": 4, "name": "Bern", "descriprion": "PowerEnergy", "price": 2.5, "tax": 0.5, "tags": [None]}
]
 
   
def _find_next_id():
    return max(product["id"] for product in products) + 1

@application.get("/products")
def get_products():
    return jsonify(products)

@application.post("/products")
def add_product():
    if request.is_json:
        product = request.get_json()
        product["id"] = _find_next_id()
        products.append(product)
        return product, 201
    return {"error": "Request must be JSON"}, 415
    
    




# set FLASK_APP=app.py
# set FLASK_ENV=development
# flask run
if __name__ == "__main__":
    application.run(debug=True)
