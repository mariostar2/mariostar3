from flask import Flask
from flask.templating import render_template
import movie_api as mo
import weader_api as wao

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html",movies=mo.MovieApi(),temp=wao.getTempature()) 
if __name__ =="__main__":
    app.run(debug=True)