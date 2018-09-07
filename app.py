import flask
from sklearn.externals import joblib

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route("/predict", methods=["GET","POST"])
def predict():
    data = {"success": False}

    params = flask.request.json
    if (params == None):
        params = flask.request.args

    # if parameters are found, echo the msg parameter

    if (params != None):
        text = params.get("msg")
        data["response"] = text
        data["personality"] = model.predict([text])[0]
        data["success"] = True

    # return a reponse in json format
    return flask.jsonify(data)

if __name__ == '__main__':
    model = joblib.load('./model/model.pkl')
    app.run(debug=True,host='0.0.0.0')
