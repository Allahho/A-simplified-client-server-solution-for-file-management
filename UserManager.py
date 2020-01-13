"""
This module contains the class UserManager,
A utlity class to manage the user database and provide Login and CRUD operations.
"""

import os
import inspect
from UserModel import User


class UserManager:
    """
    A simple users data manager.
    This is a utility class to manage registration, login and deletion of users

    Attributes:
    -----------------
        userDb: string
            path to the csv file containing user records
    Methods:
    -----------------
        __init__():
            intialize the user manager object
        verifyUserExists():
            returns True if a user exists in db
        login():
            verifies a username and password form db
        register():
            creates a new entry in db for username,password,privilege
        delete():
            removes an entry from db for specified username
    """

    def __init__(self):
        """Initialize the user manager object.
        The parameters are passed on to the init function of UserManager

        Parameters:
        ------------------------------------------
        username : string
            username as provided at login
        """
        self.user_db = os.path.dirname(os.path.abspath(inspect.getfile(
            inspect.currentframe()))) + "/DB/UserList.csv"

    def verifyUserExists(self, username):
        """Verifies if a specied user exits in the user db

        Parameters:
        ------------------------------------------
        username : string
            username to verify

        Return : Boolean
            True: if user exists
            False: if user not found
        """
        success = False
        with open(self.user_db, "r") as u_file:
            for cnt, line in enumerate(u_file):
                if cnt > 0:
                    attr = line.split(',')
                    if attr[0] == username:
                        success = True
        return success

    def logIn(self, username, password):
        """Verifies the user credentials to check a username against password.
        Verifies i f the username exists then gets its credentials
        and matches them against the provided password to verify the user login

        Parameters:
        ------------------------------------------
        username : string
            username to verify
        password : string
            password to verify

        Return : string
            success: Login Success
            failure: Unknown User | Password Incorrect
        """
        response = ""
        if self.verifyUserExists(username):
            user = self.getUserCredentials(username)
            if password == user.password:
                response = "Log In Success"
            else:
                response = "Password incorrect"
        else:
            response = "Unknown user"
        return response
    def getUserCredentials(self, username):
        """Get user data for specified username

        Parameters:
        ------------------------------------------
        username : string
            username to fetch data

        Return : User
            returns the User Data Model for the specified username
        """
        user = User(username)
        with open(self.user_db) as u_file:
            for cnt, line in enumerate(u_file):
                if cnt > 0:
                    attr = line.split(',')
                    if attr[0] == username:
                        user.privilege = attr[2].strip("\t\r\n")
                        user.password = attr[1]
                        user.rootDirectory = "/User/"+username
                        user.currentDirectory = user.rootDirectory
                        break
        return user

    def deleteUser(self, username):
        """Delete a user from db

        Parameters:
        ------------------------------------------
        username : string
            username to delete

        Return : string
            Succcess: User deleted
            Failure : User not found
        """
        userlist = []
        success = False
        response = ""
        with open(self.user_db) as u_file:
            for line in enumerate(u_file):
                attr = line.split(',')
                if attr[0] == username:
                    success = True
                else:
                    userlist.append(line)
        with open(self.user_db, 'w') as u_file:
            for user_data in userlist:
                u_file.write(user_data)
        if success:
            response = "User deleted"
        else:
            response = "User not found"
        return response

    def registerUser(self, username, password, privilege):
        """create a new user

        Parameters:
        ------------------------------------------
        username : string
            username of user
        password : string
            password for login
        privilege : string
            access rights i.e. admin or user

        Return : string
            Succcess: User Registered
            Failure : User already exists
        """
        data = ""
        if self.verifyUserExists(username):
            data = "user already exists"
        else:
            with open(self.user_db, 'a') as u_file:
                u_file.write(f"\n{username},{password},{privilege}")
            data = "user registered"
        return data
