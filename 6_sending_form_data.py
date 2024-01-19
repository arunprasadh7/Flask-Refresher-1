# Sending form data 

from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

# home page 
@app.route('/')
@app.route('/home')
def home():
    return render_template('form_home.html')


# login page 
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        if name.lower() == 'admin' and password == '123':
            return render_template('form_dashboard.html',user=name)
        else:
            return render_template('form_home.html')
    
    else:
        name = request.args.get('name')
        return render_template('form_login.html',name=name)


if __name__ == '__main__':
    app.run(debug=True)