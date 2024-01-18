from flask import Flask 

app = Flask(__name__)


# Routing in flask 


# 1 - Routing using decorators 

@app.route('/')
def login_page():
    return 'Welcome to login page!!'

@app.route('/home')
def home_page():
    return 'Welcome to home page.'



# 2 - Routing without using decorators

# app.add_url_rule('/','login',login_page)
# app.add_url_rule('/home_page','home_page',home_page)


if __name__ == '__main__':
    app.run(debug=True)