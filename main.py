from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/signup", methods=['POST'])
def sign_up():
    username = request.form['usrnm']
    password = request.form['pwd1']
    password2 = request.form['pwd2']
    email_addr = request.form['email']
    space = ' '
    email_at = '@'
    email_dot = '.'
    user_error = " Invalid username!"
    pwd1_error = " Password does not meet password requirements!"
    pwd2_error = " Please make sure that the passwords match!"

    if username == '' and password == '' and password2 == '':
        return render_template('signup.html', user_error=user_error, pwd1_error=pwd1_error, pwd2_error=pwd2_error)
    if username == '' or len(username) < 3 or len(username) > 20 or space in username:
        return render_template('signup.html', user_error=user_error, email_addr=email_addr, username=username)
    if password == '' or len(password) < 3 or len(password) > 20 or space in password: 
        return render_template('signup.html', pwd1_error=pwd1_error, username=username, email_addr=email_addr)
    if password2 == '' or password2 != password or space in password2:
        return render_template('signup.html', pwd2_error=pwd2_error, username=username, email_addr=email_addr)
    if email_addr != '':
        if email_addr.count(email_dot) > 1 or email_at not in email_addr or email_addr.count(email_at) > 1 or space in email_addr or len(email_addr) < 3 or len(email_addr) > 20:
            email_error = " Please enter a valid email address or leave blank!"
            return render_template('signup.html', email_error=email_error, username=username, email_addr=email_addr)

    return redirect("/welcome?usrnm={}".format(username))

@app.route("/welcome")
def welcome():
    username = request.args.get('usrnm')
    return render_template('welcome.html', usernm=username)
@app.route("/")
def index():

    return render_template('signup.html')

app.run()