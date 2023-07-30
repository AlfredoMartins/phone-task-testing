
from flask import Flask, request, jsonify

app = Flask(__name__)

brands = [
    "Nokia",
    "Apple",
    "Tecno"
]

os_platforms = [
    "Android",
    "iOS",
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

@app.route('/phone_store', methods=["GET", "POST"])
def phone_store():

    print("home")
    print(request.method)

    if request.method == "POST":
        print("inside post")
        print(request.method)

        print(request.form)

        name = request.form['name']
        """
        brand = request.form['brand'] 
        year_of_release = int(request.form['year_of_release'])
        os_platform = request.form['os_platform']
        """
        new_object = {
            
        }

        return jsonify(new_object), 201

if __name__ == '__main__':
    app.run(debug=True)