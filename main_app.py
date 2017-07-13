import flask
app = flask.Flask(__name__)

@app.route("/")

def index():
    #do whatevr here...
    return "Helloz there is a Instagram Bot working in the background."

