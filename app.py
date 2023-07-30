
from flask import Flask, request, jsonify

app = Flask(__name__)

brands = [
    "Nokia",
    "Apple",
    "Samsung",
    "Google",
    "Huawei",
    "Xiaomi",
    "OnePlus",
    "Sony",
    "LG",
    "Motorola",
    "HTC",
    "BlackBerry",
    "Lenovo",
    "Asus",
    "Oppo",
    "Vivo",
    "Realme",
    "ZTE",
    "Alcatel",
    "Tecno"
]

os_platforms = [
    "Android",
    "iOS",
    "BlackBerry OS",
    "Windows Phone"
]

mobile_store = [
    {
        "name" : "Spark",
        "brand" :  "Tecno",
        "year_of_release" : 2020,
        "os_platform" : "Android"
    },
]

mobile_store.clear()

# -> Write in Pythonic way

def exists(obj):
    for x in mobile_store:
        if x['name'] == obj['name'] and x['brand'] == obj['brand']:
            return True
    return False

def is_valid(obj):
    return len(obj['name']) > 0 and obj['brand'] in brands and int(obj['year_of_release']) >= 2000 and int(obj['year_of_release']) <= 2023 and obj['os_platform'] in os_platforms 

@app.route("/")
@app.route('/phone_store', methods=['GET', 'POST'])
def phone_store():
    if request.method == 'GET':
        if len(mobile_store) > 0:
            return jsonify(mobile_store)
        return jsonify({"message": "404 Nothing found"}), 404

    if request.method == 'POST':
        
        try:
            name = request.form['name']
            brand = request.form['brand'] 
            year_of_release = request.form['year_of_release']
            os_platform = request.form['os_platform']
            id =  mobile_store[-1]['id'] + 1 if len(mobile_store) > 0 else 1

            new_object = {
                "id" : id,
                "name" : name,
                "brand" :  brand,
                "year_of_release" : year_of_release,
                "os_platform" : os_platform
            }
            
            if not is_valid(new_object):
                return jsonify({"message": "422 Unprocessable Entity"}), 422

            if exists(new_object):
                return jsonify({"message": "409 Conflict"}), 409

            mobile_store.append(new_object)
            
            return jsonify(new_object), 201
        except Exception as e:
            return jsonify({"message": f'400 Bad Request {e}'}), 400

@app.route('/phone_store/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_mobile_phone(id):
    if request.method == 'GET':
        try:
            for mobile in mobile_store:
                if mobile['id'] == id:
                    return jsonify(mobile), 200
            return jsonify({"message": "404 Not Found"}), 404
        except Exception as e:
            return jsonify({"message": f'400 Bad Request {e}'}), 400
    
    if request.method == 'PUT':
        try:
            for mobile in mobile_store:
                if mobile['id'] == id:
                    mobile['name'] = request.form['name']
                    mobile['brand'] = request.form['brand']
                    mobile['year_of_release'] = request.form['year_of_release']
                    mobile['os_platform'] = request.form['os_platform']

                    update_mobile = {
                        "id" : id,
                        "name" : mobile['name'],
                        "brand" :  mobile['brand'],
                        "year_of_release" : mobile['year_of_release'],
                        "os_platform" : mobile['os_platform']
                    }

                    return jsonify(mobile_store), 200
            return jsonify({"message": "404 Not Found"}), 404
        except Exception as e:
            return jsonify({"message": f'400 Bad Request {e}'}), 400
        
    if request.method == 'DELETE':
        try:
            for i, mobile in enumerate(mobile_store):
                if mobile['id'] == id:
                    mobile_store.pop(i)
                    return jsonify({"message": "204"}), 204
            return jsonify({"message": "404 Not Found"}), 404
        except Exception as e:
            return jsonify({"message": f'400 Bad Request {e}'}), 400

if __name__ == '__main__':
    app.run(debug=True)