from flask import Flask, render_template, url_for, request, session, redirect , send_file
from flask_session import Session

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
        result = fetch_student_details.get_student_details(request.form.get("studentId"))
        # successful authentication
        if result[0] == 1:

            if(result[1][0][3]==request.form.get("studentPassword")):
                session["studentId"] = request.form.get("studentId")
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
        result = insert_student.insert_student_into_db(request.form.get("studentId"), request.form.get("studentName"),
                                                       request.form.get("studentEmail"),
                                                       request.form.get("studentPassword"),
                                                       request.form.get("studentCurrentSem"))

        return render_template('signup_success_fail.html', result=result)

    else:
        return render_template('signup_template.html')


@app.route("/logout")
def logout_fxn():
    session["studentId"] = None
    return redirect("/welcome")