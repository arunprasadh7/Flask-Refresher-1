# Flask Templates 

from flask import Flask,render_template

app = Flask(__name__)

# home page 
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    list = {'John':1000,'Smith':500,'Mary':800}
    return render_template('dashboard.html',dashboard=list)



if __name__ == '__main__':
    app.run(debug=True)