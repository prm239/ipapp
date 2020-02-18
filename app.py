import socket
from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def index():
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip
app.run(host="0.0.0.0",port="8080")
