
from flask import Flask, render_template, request, url_for, redirect, session




app = Flask(__name__)
# secret key secures session cookies
app.secret_key = 'my_secret_key' 

# keeps track of application data as changes (such as requests) are made
app.app_context().push()

# the two user types, a student login and an admin




# sets username variable that will be displayed on the screen
username = ''






class WMGSIS_Authentication:

    def __init__(self):
        self.username = ''
        self.password = ''
        self.WMGSIS_users = {

            'WMGSIS-student': 'student_password',
            'WMGSIS-admin': 'admin_password',
        }
        self.incorrect_login = False

    
    def Authenticate_login(self, username, password):
        # class variables set the username and password passed in as arguments
        self.username = username
        self.password = password
        # if username is a recognised username
        if self.username in self.WMGSIS_users:
           
            # if the entered username corresponds with the password in the dictionary object
            if self.WMGSIS_users[self.username] == self.password:
                
                # stores inputted username and password in browser server
                session['username'] = self.username
                session['password'] = self.password
                # return True so we know that the login credentials are valid in global scope
                return True
        # otherwise keep on login page as username isn't recognised
            else:
                return render_template('login.html', incorrect_login = True)
    




# renders the home page
@app.route('/home')
def home():
    return render_template('home.html')


# renders the login page as the first page when using clicking the URL
@app.route('/', methods=['GET', 'POST'])
def login():
    # if the browser method is POST (entering data)
    if request.method == 'POST':

        # get the username and password from client-to-server request
        username = request.form.get('username')
        password = request.form.get('password')
        
        # create object of the class
        WMGSIS_verify_user = WMGSIS_Authentication()

        # if the login method inside the class has identified a valid login and returned True
        if WMGSIS_verify_user.Authenticate_login(username, password) is True:

            # then direct to home page
            return redirect(url_for('home'))

        # if login method doesn't return true then remain on login page 
        # incorrect_login set to true, used to display error message
        else: 
            return render_template('login.html', incorrect_login = True)
    
    return render_template('login.html')


# redirects user to the login page when the logout request is made
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))



# renders the extension requests page with POST and GET capabilities
@app.route('/extensionRequests/', methods=['POST', 'GET'])
def extensionRequests():

    # checks if user is logged in and whether they have admin rights or not
    if 'username' in session:
        username = session['username']
        # set the false by default
        allow_data_changes = False

        if username == 'WMGSIS-admin':
            # becomes true if admin authentication is true
            allow_data_changes = True
        # renders the page
        return render_template('ExtensionRequests.html', allow_data_changes=allow_data_changes)
    # redirects user to login page if there is no username registered in the session 
    else:
        return redirect(url_for('login'))






@app.route('/GradeClassifications/', methods=['POST', 'GET'])
def GradeClassifications():
    # checks if user is logged in and whether they have admin rights or not
    if 'username' in session:
        username = session['username']
        # set the false by default
        allow_data_changes = False

        if username == 'WMGSIS-admin':
            # becomes true if admin authentication is true
            allow_data_changes = True
        # renders the page
        return render_template('GradeClassifications.html', allow_data_changes=allow_data_changes)
    # redirects user to login page if there is no username registered in the session 
    else:
        return redirect(url_for('login'))





@app.route('/Re-Sits/', methods=['POST', 'GET'])
def Resits():
    # checks if user is logged in and whether they have admin rights or not
    if 'username' in session:
        username = session['username']
        # set the false by default
        allow_data_changes = False

        if username == 'WMGSIS-admin':
            # becomes true if admin authentication is true
            allow_data_changes = True
        # renders the page
        return render_template('Re-Sits.html', allow_data_changes=allow_data_changes)
    # redirects user to login page if there is no username registered in the session 
    else:
        return redirect(url_for('login'))






@app.route('/ModulePassRate/', methods=['POST', 'GET'])
def ModulePassRate():
    # checks if user is logged in and whether they have admin rights or not
    if 'username' in session:
        username = session['username']
        # set the false by default
        allow_data_changes = False

        if username == 'WMGSIS-admin':
            # becomes true if admin authentication is true
            allow_data_changes = True
        # renders the page
        return render_template('ModulePassRate.html', allow_data_changes=allow_data_changes)
    # redirects user to login page if there is no username registered in the session 
    else:
        return redirect(url_for('login'))



# ensures this file is executed when run and no when imported
if __name__ == '__main__':
    app.run(debug=True)