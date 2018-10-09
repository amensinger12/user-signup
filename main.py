from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

#return redirect("/?error=" + error) use this to redirect to homepage

def char_length(x):
    if len(x) > 3 and len(x) < 20:
        return True
    else:
        return False

def empty(x):
    if x:
        return True
    else:
        return False

def email_symbol(x):
    if x.count('@') == 1:
        return True
    else:
        return False

def email_period(x):
    if x.count('.') == 1:
        return True
    else:
        return False

@app.route("/error", methods=["POST"])
def confirmation():

    username = request.form["username"]
    password = request.form["password"]
    password_valid = request.form["password_valid"]
    email = request.form["email"]

    username_error = ''
    password_error = ''
    password_valid_error = ''
    email_error = ''

    require_field_error = "Required Field"
    char_count_error = " must be between 3 and 20 characters long"
    spaces_error =  " cannot contain any spaces"

#username validation
    if not empty(username):
        username_error = require_field_error
        password = ''
        password_valid = ''
    elif not char_length(username):
        username_error = "Username" + char_count_error
        password = ''
        password_valid = ''
    else:
        if " " in username:
            username_error = "Username" + spaces_error
            password = ''
            password_valid = ''

#password validation
    if not empty(password):
        password_error = require_field_error
        password = ''
        password_valid = ''
    elif not char_length(password):
        password_error = "Password" + char_count_error
        password = ''
        password_valid = ''
    else:
        if " " in password:
            password_error = "Password" + spaces_error
            password = ''
            password_valid = ''

#password_valid validation
    if password_valid == "":
        password_valid_error = require_field_error
        password = ''
        password_valid = ''
    else:
        if password != password_valid:
            password_valid_error = "Passwords must match"
            password_error = "Passwords must match"
            password = ''
            password_valid = ''

#email validation
    if empty(email):
        if not char_length(email):
            email_error = "Email" + char_count_error
            password = ''
            password = ''
        elif not email_symbol(email):
            email_error = "Email must contain only one @ in your email"
            password = ''
            password_valid = ''
        elif not email_period(email):
            email_error = "Email must contain only one ."
            password = ''
            password_valid = ''
        else:
            if " " in email:
                email_error = "Email" + spaces_error
                password = ''
                password_valid = ''

#no errors, welcome new user
    if not username_error and not password_error and not password_valid_error and not email_error:
        return redirect('/welcome?username=' + username)
    else:
        return render_template("homepage.html", username_error=username_error, username=username, password_error=password_error, password=password, password_valid_error=password_valid_error, password_valid=password_valid, email_error=email_error, email=email)

@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template('welcome.html', username=username)

@app.route("/")
def user_signup_form():
    return render_template('homepage.html')

app.run()