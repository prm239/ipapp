from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def index():
	return request.remote_addr

app.run(host="0.0.0.0",port="8000")
