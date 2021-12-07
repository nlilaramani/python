from flask import Flask,jsonify, render_template,request
import userdb

app=Flask(__name__)

@app.route("/hello")
def hello_world():
    return render_template("hello.html")
@app.route("/hello/<name>")
def greet_user(name):
    return render_template("hello.html",name=name)
@app.route("/users")
def hello_users():
    return "<html><body><h1>Hello users!</h1><a href='#'>Click to get user list</a></body></html>"
@app.route("/error")
def error():
    return "<h1>error</h1>"
@app.route("/")
def homepage():
    return "index.html"
@app.route("/user/<userid>")
def display_user(userid):
    return "userprofile_"+userid+".html"
@app.route("/products")
def get_products():
    # database call to get all the products
    # list/dictionary object to poplulate
    # send response back
    products={"TV":650.00,"Microwave":150.00}
    return products
@app.route("/productlist")
def get_product_list():
    products=[{"name":"TV","price":650.00},{"name":"Microwave","price":150.00}]
    return jsonify(products)
@app.route("/req_get_params")
def params():
    p1=request.args.get('p1')
    p2=request.args.get('p2')
    return p1+", "+p2
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login_form.html")
    else:
        uname=request.form['username']
        pwd=request.form['password']
        #call database function
        user=userdb.login(uname,pwd)
        if user is not None:
            return render_template('user.html',user=user)
        else:
            return render_template('login_form.html')
    
    
 
