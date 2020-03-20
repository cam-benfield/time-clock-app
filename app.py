# -*- coding: utf-8 -*-

"""Application Docstring.

Application intended to build a time clock for small businesses to minimize
cost paid out to outside companies.
"""


from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'  # TODO: Change password later
app.config['MYSQL_DB'] = 'MyDB'

def employee_num(details):



@app.route('/', methods=['GET', 'POST'])
def index():
    """Home page module.

    Returns:
        index template for homepage
        """
    return render_template('index.html')


@app.route('/employee_add', methods=['GET', 'POST'])
def employee_update():
    """Employee update page module.

    Returns:
        employee update page
        """

    if request.method == 'POST':
        details = request.__format__
        # details is dict and has'fname','lname','email','phone','birthdate'
        emp_id = lower(details['fname'][0]+details['lname'])+mon_num+yr_num

        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO Employees(
                        empID,
                        firstName,
                        lastName,
                        emailAdd,
                        phoneNum,
                        birthDate)
                    VALUES(
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
        );""")

    return render_template('employee_update.html')


if __name__ == '__main__':
    app.run()
