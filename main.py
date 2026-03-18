from flask import Flask, request, jsonify

app = Flask(__name__)

temperature = 0
humidity = 0

@app.route("/data")
def data():
    try:
        temp = float(request.args.get("temp", 0))
        hum = float(request.args.get("hum", 0))

        print("Temp:", temp)
        print("Hum:", hum)

        return "OK", 200

    except Exception as e:
        print("Erreur:", e)
        return "Erreur", 500

@app.route("/temperature")
def get_temperature():
    return jsonify({"temperature": temperature})


@app.route("/humidity")
def get_humidity():
    return jsonify({"humidity": humidity})


             
             
