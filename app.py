import decimal

from flask import Flask, render_template, url_for, request, session, redirect , send_file , flash
from flask_session import Session
from sql_queries import fetch_all_companies, fetch_customer_details, fetch_customer_pass_for_auth, insert_customer_details, fetch_investment_options, fetch_calculator_tools , create_budget_entry , fetch_budget, update_budget, get_count_expense, fetch_total_expense_cost,fetch_expenses_of_user,insert_expense,delete_expense , remove_all_expenses_prg, fetch_all_registerd_users, calculate_expense_by_budget_ratio

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
    ratio = calculate_expense_by_budget_ratio.get_budget_details(session.get("customerEmail"))

    count = get_count_expense.get_count_customer_expense(session.get("customerEmail"))
    if count > 0:
        if float(ratio) >= 0.9:
            flash("Caution : Your Budget is about to get exhausted")

    return render_template("home.html")

@app.route("/home/explore")
def explore_fxn():
    if not session.get("customerEmail"):
        return redirect("/welcome")


    flash("")
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

        count = get_count_expense.get_count_customer_expense(session.get("customerEmail"))
        # count is zero means there are no expenses till now
        if count == 0:
            # give a flash message of budget getting updated in the home page

            flash("Your budget has been successfully updated !!! 😇")
            update_budget.update_budget_prg(session.get("customerEmail"),request.form.get("budgetCost"))
            return redirect(url_for("home_fxn"))
        else:

            totalExpense = fetch_total_expense_cost.get_total_expense_cost(session.get("customerEmail"))
            if int(request.form.get("budgetCost")) >= totalExpense:
                flash("Your budget has been successfully updated !!! 😇")
                update_budget.update_budget_prg(session.get("customerEmail"),request.form.get("budgetCost"))
                return redirect(url_for("home_fxn"))

            else:

                flash("New Budget is lower than your current expense , please try again later 🥲")
                return redirect(url_for("home_fxn"))





    budget = fetch_budget.get_budget_details(session.get("customerEmail"))
    return render_template("budget_tracking.html",budget=budget)

# @app.route("/home/edit_budget_tracking")
# def edit_budget_fxn():
#     if not session.get("customerEmail"):
#         return redirect("/welcome")


@app.route("/home/expense_tracking")
def expense_tracking_fxn():
    if not session.get("customerEmail"):
        return redirect("/welcome")

    return render_template('expense_tracking.html')

@app.route("/home/expense_tracking/view_expenses")
def view_expenses_fxn():
    if not session.get("customerEmail"):
        return redirect("/welcome")

    count = get_count_expense.get_count_customer_expense(session.get("customerEmail"))
    if count == 0:
        flash("You Don't have any Expenses to be Viewed !!!")
        return redirect(url_for('expense_tracking_fxn'))

    result = fetch_expenses_of_user.get_customer_expenses(session.get("customerEmail"))
    totalExpense = fetch_total_expense_cost.get_total_expense_cost(session.get("customerEmail"))
    budget = fetch_budget.get_budget_details(session.get("customerEmail"))
    budgetBalance = budget-totalExpense
    return render_template('view_expenses.html',result=result,totalExpense=totalExpense,budgetBalance=budgetBalance)

@app.route("/home/expense_tracking/add_new_expenses",methods=['GET', 'POST'])
def add_new_expenses_fxn():
    if not session.get("customerEmail"):
        return redirect("/welcome")

    if request.method == 'POST':


        result = fetch_expenses_of_user.get_customer_expenses(session.get("customerEmail"))
        list_of_expense_names = []
        for expense in result:
            list_of_expense_names.append(expense[0])

        if request.form.get("expenseName") in list_of_expense_names:
            flash("The given expense already exists !!!")
            return redirect(url_for('expense_tracking_fxn'))

        budget = fetch_budget.get_budget_details(session.get("customerEmail"))
        totalExpense = fetch_total_expense_cost.get_total_expense_cost(session.get("customerEmail"))
        count = get_count_expense.get_count_customer_expense(session.get("customerEmail"))

        if count == 0:
            if float(request.form.get("expenseCost")) > float(budget):
                # flash message displayed in expense_tracking.html that on adding new expense, the budget will excede
                flash("Unable to add the given expense in your list as total expense is exceeding your budget 😅")
                return redirect(url_for('expense_tracking_fxn'))

            else:
                insert_expense.insert_customer_expense(session.get("customerEmail"),request.form.get('expenseName'),request.form.get('expenseType'),request.form.get('expenseCost'))
                #         flash message displaying that successfully inserted
                flash("Expense has been successfully updated !!! 💵")
                return redirect(url_for('expense_tracking_fxn'))

        if decimal.Decimal(totalExpense+decimal.Decimal((request.form.get("expenseCost")))) > decimal.Decimal(budget):
            # flash message displayed in expense_tracking.html that on adding new expense, the budget will excede
            flash("Unable to add the given expense in your list as total expense is exceeding your budget 😅")
            return redirect(url_for('expense_tracking_fxn'))

        else:
            insert_expense.insert_customer_expense(session.get("customerEmail"),request.form.get('expenseName'),request.form.get('expenseType'),request.form.get('expenseCost'))
    #         flash message displaying that successfully inserted
            flash("Expense has been successfully updated !!! 💵")
            return redirect(url_for('expense_tracking_fxn'))



    totalExpense = fetch_total_expense_cost.get_total_expense_cost(session.get("customerEmail"))
    budget = fetch_budget.get_budget_details(session.get("customerEmail"))
    if totalExpense == budget:
        # give a flash message on the expense_tracking.html that the budget is already equal to the expense
        flash("Unable to add the given expense in your list as your total expense is equal to your budget !!! 😅 ")
        return render_template(url_for('expense_tracking_fxn'))

    return render_template('add_new_expenses.html')

@app.route('/home/expense_tracking/remove_expense', methods=['GET', 'POST'])
def remove_expense_fxn():
    if not session.get("customerEmail"):
        return redirect("/welcome")

    if request.method == "POST":
        result = fetch_expenses_of_user.get_customer_expenses(session.get("customerEmail"))
        list_of_expense_names = []
        for expense in result:
            list_of_expense_names.append(expense[0])

        if request.form.get("expenseName") in list_of_expense_names:
            flash("Expense Successfully Deleted")
            delete_expense.delete_expense_prg(session.get("customerEmail"), request.form.get("expenseName"))

        else:
            flash("Given Expense Name does not exist in your Expenses List !!!")

        return redirect(url_for('expense_tracking_fxn'))

    count = get_count_expense.get_count_customer_expense(session.get("customerEmail"))
    if count == 0:
        flash("You Don't have any Expenses to be deleted !!!")
        return redirect(url_for('expense_tracking_fxn'))

    return render_template('remove_expense.html')

@app.route('/home/expense_tracking/remove_all_expenses')
def remove_all_expenses_fxn():
    if not session.get("customerEmail"):
        return redirect("/welcome")

    remove_all_expenses_prg.remove_all_responses_from_db_for_given_customerEmail(session.get("customerEmail"))
    flash('All your Expenses have been successfully deleted !!!')
    return redirect(url_for('expense_tracking_fxn'))

# real life example of successful reflection attack :
# @app.route("/home/view_registered_users")
# def view_registered_users_fxn():
#     result = fetch_all_registerd_users.get_customer_details(session.get("customerEmail"))
#     result_str = result[5][0]
#     print(result_str)
#     html = "<html> <body>" + result_str +  " body..</body></html>"
#     return html

