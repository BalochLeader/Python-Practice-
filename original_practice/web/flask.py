from flask  import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
@app.route("/diwas")
def hello_diwas():
    return "<input> Enter : </input> "

app.run()