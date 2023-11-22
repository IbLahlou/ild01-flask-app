
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
app = Flask(__name__)


# Route 1 : Home page

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



# Route 2 : Feedback page

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    lname = request.form.get('Lname')
    fname = request.form.get('fname')
    email = request.form.get('email')
    date = request.form.get('date')
    feedback = request.form.get('comments')
    satisfied = request.form.get('satisfied')
    df = pd.DataFrame([[lname, fname, email, date, feedback, satisfied]], columns=['Lname', 'fname', 'email', 'date', 'feedback', 'satisfied'])
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
