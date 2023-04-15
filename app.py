from flask import Flask, render_template, url_for, request, session, redirect , send_file
from flask_session import Session
from sql_queries import fetch_investor_details, insert_investor_details

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/welcome')
def welcome_fxn():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login_fxn():
    if request.method == 'POST':
        result = fetch_investor_details.get_investor_details(request.form.get("investorEmail"))
        # successful authentication
        if result[0] == 1:

            if(result[1][0][0]==request.form.get("investorPassword")):
                session["investorEmail"] = request.form.get("investorEmail")
                return redirect(url_for('home_fxn'))
            
            else:
                return render_template('login_fail.html', result=result)
                
        else:
            return render_template('login_fail.html', result=result)

        # return render_template('home_template.html')
    else:
        return render_template('login_template.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup_fxn():
    if request.method == 'POST':
        result = insert_investor_details.insert_investor_into_db(request.form.get("investorName"),request.form.get("investorEmail"),request.form.get("investorPassword"),request.form.get("investorBudget"),request.form.get("investorMobileNo"),request.form.get("investorAddress"),request.form.get("investorAge"),request.form.get("investmentObjectiveId"))                    

        return render_template('signup_success_fail.html', result=result)

    else:
        return render_template('signup_template.html')


@app.route("/logout")
def logout_fxn():
    session["investorEmail"] = None
    return redirect("/welcome")

@app.route("/home")
def home_fxn():
    if not session.get("investorEmail"):
        return redirect("/welcome")

    return render_template("home.html")

@app.route("/home/contact")
def contact_fxn():
    return render_template("contact.html")

@app.route('/home/profile')
def profile_fxn():
    return render_template("profile.html")