# 4 - HTTP methods GET, POST 
# GET - to fetch/request data from the server (unsecure)
# POST - to  post data to the server (more secure)

from flask import Flask,request

app = Flask(__name__)

@app.route('/')
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form['userName']
        password = request.form['userPassword']
        
        if name.lower() == 'arun' and password == '1234':
            return f'Login Successfull.\nWelcome {name.capitalize()}'
        else:
            return f'Login failed.Try again.'
        
    else:
        name = request.args.get('userName',default='')
        password = request.args.get('userPassword',default='')
        if name.lower() == 'arun' and password == '1234':
            return f'Login Successfull.\nWelcome {name.capitalize()}'
        else:
            return f'Login failed. Try again.'


if __name__ == '__main__':
    app.run(debug=True)