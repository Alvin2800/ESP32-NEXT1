from flask import Flask, request, jsonify

app = Flask(__name__)

temperature = 0
humidity = 0

@app.route("/data")
def data():
    global temperature, humidity

    temperature = float(request.args.get("temp", 0))
    humidity = float(request.args.get("hum", 0))

    print("Température :", temperature)
    print("Humidité :", humidity)

    return "OK", 200

@app.route("/temperature")
def get_temperature():
    return jsonify({"temperature": temperature})


@app.route("/humidity")
def get_humidity():
    return jsonify({"humidity": humidity})


             
             
