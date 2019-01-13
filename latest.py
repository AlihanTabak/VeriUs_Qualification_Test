from flask import Flask
from sklearn.externals import joblib

import os

my_best_model = joblib.load("latest_model.pkl")

app = Flask(__name__)

@app.route("/submit", methods=['POST'])


#define predict method with json format control.
def predict():
    try:
        request_data = request.get_json()
        message = request_data['text']
    except TypeError:
        return make_response("Invalid JSON format or request CONTENT-TYPE JSON", 400)
    else:
        pred_result = my_best_model.predict([message])
        answer = int(pred_result[0])

        return jsonify({ 'result': "Non-abusive" if answer == 0 else "Abusive" }), 200

if __name__ == "__main__":
     server = os.environ.get('SERVER_VeriUs')
     if server is not None:
        app.run(host='0.0.0.0', port=5000)
     else:
        app.run(port=5000)