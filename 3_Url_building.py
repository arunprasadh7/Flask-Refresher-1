# 3 - flask script using url_for() 
# used to display dynamic feature to the method 

# eg : College details page 

from flask import Flask,url_for,redirect

app = Flask(__name__)

# Admin page 
@app.route('/')
def admin():
    return 'Welcome to Admin Page'

# Employee details page 
@app.route('/employee')
def employee():
    return 'Welcome to Employee details page.'

#Student details page 
@app.route('/student/<name>')
def student(name):
    return 'Hi %s. Welcome to student details page.'%name


# Common re-routing using url_for 
@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    
    elif name == 'employee':
        return redirect(url_for('employee'))
    
    else:
        return redirect(url_for('student',name=name))



if __name__ == '__main__':
    app.run(debug=True)