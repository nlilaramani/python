from flask import Flask, request, render_template,jsonify,abort
import userdb

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        result=userdb.login(username,password)
        if result:
            return render_template('user.html',user=result)
        else:
            return render_template('login_form.html',error="Invalid credentials")
    else:
        return render_template('login_form.html')

@app.route('/users/<name>')
def user(name):
    return 'user_'+name+'.html'
    
@app.route('/req_get_params')
def params():
    p1=request.args.get('p1')
    p2=request.args.get('p2')
    return p1+' '+p2
@app.route('/upload',methods=['GET','POST'])
def upload():
    print('upload file')
    f=request.files['file']
    f.save("c:\\data\\"+f.filename)
    return 'Upload successful'

@app.route('/error')
def error():
    abort(401)

@app.route('/products')
def get_products():
    products={'TV':650.00,'Microwave':150.00}
    return products
    
@app.route('/productlist')
def get_product_list():
    products=[{"name":'TV', "price":650.00},{"name":"Microwave", "price":150.00}]
    return jsonify(products)
    
#bp_users=Blueprint('users',__name__,url_prefix='/users')
import users
app.register_blueprint(users.bp)
import errors
app.register_blueprint(errors.bp)
#bp_products=Blueprint('products'__name__,url_prefix='/products')
#app.register_blueprint(bp_products)
