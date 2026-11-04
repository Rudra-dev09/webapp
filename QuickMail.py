from flask import Flask,render_template
import requests

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("QuickMail.html") # this sends that HTML page back to visitors browser

@app.route("/create-inbox",methods=["POST"])
def create_inbox():
    API="https://dummyinbox.com/api/v1"
    response=requests.post(f"{API}/inboxes",timeout=20)
    response.raise_for_status()
    data=response.json()
    email=data["address"]
    web_url=data["webUrl"]
    return render_template("QuickMail.html",email=email,web_url=web_url)

if __name__=="__main__":
    app.run(host="0.0.0.0",port="5000")