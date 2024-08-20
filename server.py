"""
Accept POST from Ecowitt Weather Station and forward to InfluxDB
"""

import requests
from flask import Flask, request

app = Flask(__name__)

INFLUXDB_URL = "http://data.lan:8086/write?db=weather"


@app.route("/weather", methods=["POST"])
def weather_data():
    """Convert payload to InfluxDB format and send"""
    data = request.form.to_dict()  # Capture the form data sent by the Ecowitt station

    # Convert the received data to InfluxDB line protocol format
    influx_data = []
    for key, value in data.items():
        if key not in [
            "PASSKEY",
            "stationtype",
            "dateutc",
            "freq",
            "model",
            "interval",
        ]:
            influx_data.append(f"{key} value={value}")
    influx_payload = "\n".join(influx_data)

    # Send the data to InfluxDB
    response = requests.post(INFLUXDB_URL, data=influx_payload, timeout=30)

    if response.status_code == 204:
        return {}, 200

    print(f"Failed to write data to InfluxDB: {response.text}")
    return {}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
