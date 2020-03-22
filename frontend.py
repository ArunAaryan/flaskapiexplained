from flask import Flask, request
app = Flask(__name__, static_url_path='/Users/arunaaryan/Desktop/flaskapi/flaskapi/static')
@app.route('/')
def hello():
    
    return app.send_static_file('home.html')

@app.route('/add',methods=['GET'])
def sendpage():
    # return "get"
    return app.send_static_file('add.html')
    
@app.route('/home')
def sendhome():
    return app.send_static_file('home.html')

@app.route('/show',methods=['GET'])
def sendpageshow():
    return app.send_static_file('show.html')


if __name__ == '__main__':
    app.run(debug=True,port=3001)