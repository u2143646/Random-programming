
from flask import Flask, render_template, request, url_for, redirect, session



# sets username variable that will be displayed on the screen
username = ''
app = Flask(__name__)
# secret key secures session cookies
app.secret_key = 'my_secret_key' 

# keeps track of application data as changes (such as requests) are made
app.app_context().push()

# the two user types, a student login and an admin
users = {
    'WMGSIS-student': 'student_password',
    'WMGSIS-admin': 'admin_password',
}

# preset data to be displayed on the extension requests page
extension_requests_data = {

    'Internet of Things': ['15', '9', 'Sickness'],
    'Software Development Life Cycle': ['14', '8', 'Personal Family Circumstance'],
    'Negotiated Learning': ['7', '6', 'Very Busy at Work'],
    'Information Business Management Processes': ['5', '4', 'Sickness'],
    'Agile Project Management': ['6', '6', 'Struggle with Assignment Workload'],
    'Cyber Risks in Organisations': ['11', '4', 'Sickness'],
    'Applied Maths II': ['5', '3', 'Personal Family Circumstance']
    };

# preset data to be displayed on the module pass rate page
module_pass_rate_data = {

    'Internet of Things': ['35', '5', '40'],
    'Software Development Life Cycle': ['31', '9', '40'],
    'Negotiated Learning': ['38', '2', '40'],
    'Information Business Management Processes': ['33', '7', '40'],
    'Agile Project Management': ['36', '4', '40'],
    'Cyber Risks in Organisations': ['32', '8', '40'],
    'Applied Maths II': ['33', '7', '40']
    };


# preset data to be displayed on the re-sit page
resit_data = {

    'Internet of Things': ['5', 'March'],
    'Software Development Life Cycle': ['9', '1st September'],
    'Negotiated Learning': ['2', '1st September'],
    'Information Business Management Processes': ['7', '1st March'],
    'Agile Project Management': ['4', '1st Sepember'],
    'Cyber Risks in Organisations': ['8', '1st September'],
    'Applied Maths II': ['7', '1st September']
    };


# preset data to be displayed on the grade classifications page
grade_classifications_data = {

    'Internet of Things': ['17', '8', '4', '6'],
    'Software Development Life Cycle': ['8', '6', '9', '8'],
    'Negotiated Learning': ['13', '10', '4', '8'],
    'Information Business Management Processes': ['12', '11', '6', '5'],
    'Agile Project Management': ['7', '15', '6', '5'],
    'Cyber Risks in Organisations': ['12', '16', '7', '2'],
    'Applied Maths II': ['10', '12', '7', '3']
    };







# renders the home page
@app.route('/home')
def home():
    return render_template('home.html')


# renders the login page as the first page when using clicking the URL
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        # if the entered credentials are valid admin or student login then redirect to home page
        if username in users and users[username] == password:

            session['username'] = username
            return redirect(url_for('home'))
        # otherwise keep on login page
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')


# redirects user to the login page when the logout request is made
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))



# renders the extension requests page with POST and GET capabilities
@app.route('/extensionRequests/', methods=['POST', 'GET'])
def extensionRequests():

# checks if user is logged in and whether they have admin rights or not
    if 'username' in session:
        username = session['username']

        if username == 'WMGSIS-admin':
            allow_data_changes = True
        else:
            allow_data_changes = False

        # Handle delete action
        if request.method == 'POST' and 'delete' in request.form:

            module_name = request.form['module_name']
            # removes the table record
            extension_requests_data.pop(module_name, None)

        # Handle update action
        if request.method == 'POST' and 'update' in request.form:

            # saves the data entered by user in order to update the table record

            num_of_requests = request.form['requests_submitted']
            num_of_requests_approved = request.form['requests_approved']
            reason_of_request = request.form['requests-reason']

            module_name = request.form['module_name']

            # updates the record data in the dictionary dataset
            
            extension_requests_data[module_name] = [num_of_requests, num_of_requests_approved, reason_of_request]
        
        # renders the page
        return render_template('extensionRequests.html', allow_data_changes=allow_data_changes, extension_requests_data=extension_requests_data)
    
    # redirects user to login page if there is no username registered in the session 
    else:
        return redirect(url_for('login'))



@app.route('/GradeClassifications/', methods=['POST', 'GET'])
def GradeClassifications():
    # checks if user is logged in and whether they have admin rights or not
    if 'username' in session:
        username = session['username']

        if username == 'WMGSIS-admin':
            allow_data_changes = True
        else:
            allow_data_changes = False

        # Handle delete action
        if request.method == 'POST' and 'delete' in request.form:

            module_name = request.form['module_name']
            # removes the table record
            grade_classifications_data.pop(module_name, None)

        # Handle update action
        if request.method == 'POST' and 'update' in request.form:

            # saves the data entered by user in order to update the table record

            grade_first = request.form['grade_first']
            grade_21 = request.form['grade_21']
            grade_second = request.form['grade_second']
            grade_third = request.form['grade_third']

            module_name = request.form['module_name']

            # updates the record data
            
            grade_classifications_data[module_name] = [grade_first, grade_21, grade_second, grade_third]
        
        # renders the page
        return render_template('GradeClassifications.html', allow_data_changes=allow_data_changes, grade_classifications_data=grade_classifications_data)
    
    # redirects user to login page if there is no username registered in the session 
    else:
        return redirect(url_for('login'))










@app.route('/Re-Sits/', methods=['POST', 'GET'])
def Resits():
    if 'username' in session:
        username = session['username']

        if username == 'WMGSIS-admin':
            allow_data_changes = True
        else:
            allow_data_changes = False

        # Handle delete action
        if request.method == 'POST' and 'delete' in request.form:

            module_name = request.form['module_name']
            # removes the table record
            resit_data.pop(module_name, None)

        # Handle update action
        if request.method == 'POST' and 'update' in request.form:

            # saves the data entered by user in order to update the table record

            num_of_resits = request.form['number_of_resits']
            date_of_resits = request.form['date_of_resits']
            

            module_name = request.form['module_name']

            # updates the record data
            
            resit_data[module_name] = [num_of_resits, date_of_resits]
        
        # renders the page
        return render_template('Re-Sits.html', allow_data_changes=allow_data_changes, resit_data=resit_data)
    
    # redirects user to login page if there is no username registered in the session 
    else:
        return redirect(url_for('login'))






@app.route('/ModulePassRate/', methods=['POST', 'GET'])
def ModulePassRate():
    # checks if user is logged in and whether they have admin rights or not
    if 'username' in session:
        username = session['username']

        if username == 'WMGSIS-admin':
            allow_data_changes = True
        else:
            allow_data_changes = False

        # Handle delete action
        if request.method == 'POST' and 'delete' in request.form:

            module_name = request.form['module_name']
            # removes the table record
            module_pass_rate_data.pop(module_name, None)

        # Handle update action
        if request.method == 'POST' and 'update' in request.form:

            # saves the data entered by user in order to update the table record

            num_of_students_passed = request.form['students_passed']
            num_of_students_failed = request.form['students_failed']
            total_num_of_students = request.form['students_total']

            module_name = request.form['module_name']

            # updates the record data
            
            module_pass_rate_data[module_name] = [num_of_students_passed, num_of_students_failed, total_num_of_students]
        
        # renders the page
        return render_template('ModulePassRate.html', allow_data_changes=allow_data_changes, module_pass_rate_data=module_pass_rate_data)
    
    # redirects user to login page if there is no username registered in the session 
    else:
        return redirect(url_for('login'))







if __name__ == '__main__':
    app.run(debug=True)