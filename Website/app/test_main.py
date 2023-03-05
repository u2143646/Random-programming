import pytest

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
                # return True so we know that the login credentials are valid in global scope
                return True
        # otherwise keep on login page as username isn't recognised
        return False
                

def test_WMGSIS_Authentication():
    test_WMGSIS_verify_user = WMGSIS_Authentication()
    assert test_WMGSIS_verify_user.Authenticate_login('WMGSIS-tutor', 'tutor_password')
