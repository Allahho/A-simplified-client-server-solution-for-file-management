"""
This module contains the class User, A data model class to store attributes of a user.
"""
class User:
    """
    A simple structure for snake. This is a collection of the block objects that make up snake

    Attributes:
    -----------------
        username: string
            username with which the user logins
        password: string
            password provided when user logins
        privilege: stirng
            the access rights of the user i.e. admin/user
        currentDirectory: stirng
            the directory which the user is currently viewing
        rootDirectory: string
            this is the root os starting directory of a user. the user cannot navigate outside this directory
    Methods:
    -----------------
        __init__():
            intialize the user object
        __repr__():
            returns print friendly representation of user object
    """
    def __init__(self,username):
        """Initialize the user object. The parameters are passed on to the init function of User

        Parameters:
        ------------------------------------------
        username : string
            username as provided at login
        """
        self.username = username
        self.password = ""
        self.privilege = ""
        self.currentDirectory = ""
        self.rootDirectory = ""
    def __repr__(self):
        '''Helper function to get the print fiendly representation of the user object
        Return : string
            returns the user object attributes in json representation
        '''
        return f"User: (username:{self.username},password:{self.password},privilege:{self.privilege},root:{self.rootDirectory})"