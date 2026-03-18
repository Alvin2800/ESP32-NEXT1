import flask as Flask, requests, jsonify
app=flask(_name_)

@app.route("/data")
           def data():
             global temperature, humidity
             r=float(requests.args.get("temp",0))
             r2=float(reqests.args.get("hum",0))
             print("temperature")
             println(temperature)
             print("humidité")
             println(humidity)
             return "ok", 200
@app.route("/temperature")
def temperature():
  return jsonify({"temperature":temperature)
@app.route("/humidity")
def humidity():
  return jsonify({"humidity":humidity)


             
             
