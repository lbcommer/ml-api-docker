import flask
import dill as pickle

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

    with open('./model/model.pkl', 'rb') as file:
        model = pickle.load(file)

    if (params != None):
        text = params.get("msg")
        data["response"] = text
        data["personality"] = model.predict([text])[0]
        data["success"] = True

    # return a reponse in json format
    return flask.jsonify(data)

# start the flask app, allow remote connections
app.run(host='0.0.0.0')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
