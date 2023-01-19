from flask import Flask, render_template, request
from searchquery import s_search
import requests


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',response=None)

@app.route('/search',methods=["POST"])



def search():
    res = []
    if(request.method == "POST"):
        query = request.form['query']
        res = s_search(query)
        #print(res)
 
    return render_template('index.html',response=res)
 
if __name__ == '__main__':
    app.DEBUG = True
    app.run()