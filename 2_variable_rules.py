# 2 Variable rules - used to display dynamic routing 

from flask import Flask

app =  Flask(__name__)

# Variable name - accepts any data type
@app.route('/home/<name>')
def home_page(name):
    return f'Welcome to homepage {name}'

# Specific data types 

#string
@app.route('/name/<string:name>')
def username(name):
    return 'Hello %s'%name


# int variable 
@app.route('/age/<int:age>')
def age(age):
    return 'Your age is %d.'%age

# float value 
@app.route('/grade/<float:cgpa>')
def price(cgpa):
    return 'Your CGPA is %f'%cgpa

if __name__ == '__main__':
    app.run(debug=True)