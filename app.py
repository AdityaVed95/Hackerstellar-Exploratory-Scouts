from flask import Flask, render_template, url_for, request, session, redirect , send_file
from flask_session import Session
from sql_queries import fetch_all_companies, fetch_customer_details, fetch_customer_pass_for_auth, insert_customer_details, fetch_investment_options, fetch_calculator_tools , create_budget_entry , fetch_budget

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
        result = fetch_customer_pass_for_auth.get_customer_details(request.form.get("customerEmail"))
        # successful authentication
        if result[0] == 1:

            if(result[1][0][0]==request.form.get("customerPassword")):
                session["customerEmail"] = request.form.get("customerEmail")
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
        result = insert_customer_details.insert_customer_into_db(request.form.get("customerName"), request.form.get("customerEmail"),request.form.get("customerMobileNo"),  request.form.get("customerAddress"),request.form.get("customerPassword"),  request.form.get("customerAge"))

        if result[0] == 1:
            create_budget_entry.insert_customer_into_db(request.form.get("customerEmail"))

        return render_template('signup_success_fail.html', result=result)

    else:
        return render_template('signup_template.html')


@app.route("/logout")
def logout_fxn():
    session["customerEmail"] = None
    return redirect("/welcome")

@app.route("/home")
def home_fxn():
    if not session.get("customerEmail"):
        return redirect("/welcome")

    return render_template("home.html")

@app.route("/home/explore")
def explore_fxn():
    if not session.get("customerEmail"):
        return redirect("/welcome")

    result = fetch_all_companies.get_all_company_details()
    return render_template("company.html", result=result)

@app.route("/home/contact")
def contact_fxn():
    if not session.get("customerEmail"):
        return redirect("/welcome")
    return render_template("contact.html")

@app.route('/home/profile')
def profile_fxn():
    if not session.get("customerEmail"):
        return redirect("/welcome")
    result = fetch_customer_details.get_customer_details(session.get("customerEmail"))
    return render_template("profile.html",result=result[0])

@app.route('/home/investment_option')
def investment_option_fxn():
    if not session.get("customerEmail"):
        return redirect("/welcome")
    result = fetch_investment_options.get_investment_options_details()
    return render_template('investment_options.html',result=result)

# @app.route('/home/<companyId>/<investmentOptionId>')
# def company_investment_details_fxn(companyId,investmentOptionId):
#     if not session.get("customerEmail"):
#         return redirect("/welcome")
    
@app.route('/home/calculator_tools')
def calculator_tools_fxn():
    if not session.get("customerEmail"):
        return redirect("/welcome")
    result = fetch_calculator_tools.get_calculator_details()

    return render_template('calculator_tools.html',result=result)

@app.route('/home/budget_tracking', methods=['GET', 'POST'])
def budget_tracking_fxn():


    if not session.get("customerEmail"):
        return redirect("/welcome")

    if request.method == 'POST':
        

    budget = fetch_budget.get_budget_details(session.get("customerEmail"))
    return render_template("budget_tracking.html",budget=budget)

# @app.route("/home/edit_budget_tracking")
# def edit_budget_fxn():
#     if not session.get("customerEmail"):
#         return redirect("/welcome")



