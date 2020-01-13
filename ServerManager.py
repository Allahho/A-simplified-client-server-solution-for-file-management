"""
This module contains the class ServerManager,
this is the controller for server operations.
"""

import os
import inspect
from UserModel import User
from UserManager import UserManager
from FileManager import FileManager


class ServerManager:
    """
    A main class to handle server operations.
    This class utilizes the filemanager and usermanager classes

    Attributes:
    -----------------
        user: User
            user Data class object to handle current user
        usermanager: UserManager
            usermanager object to handle user operations
        absolutePath : stirng
            path to the server directory
        filemanager: FileManager
            filemanager to handle file operations
    Methods:
    -----------------
        __init__():
            intialize the server manager object
        help():
            returns print friendly representation of aviable server commands
        login():
            user signin method
        delete():
            user delete method
        register():
            create a new user
        checkLogin():
            checks if a user is logged in or not
        changeFolder():
            method to navigate between folders
        list():
            returns the content of the current directory
        readFile():
            returns the contents of specified file
        writeFile():
            writes data to a file
        createFolder():
            creates a folder for logged in user
    """

    def __init__(self):
        """Initialize the server manager object.
        The parameters are passed on to the init function of server manager
        """
        self.user = User("")
        self.usermanager = UserManager()
        self.absolutePath = os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.fileManager = FileManager(self.absolutePath)
        super().__init__()

    def help(self):
        """returns the list of available commands
        Return : string
            list of commands
        """
        helper = "Following Commands are available:"
        if self.user.username == "":
            helper += "\n" + \
                "\t login <username> <password> {Signin to the system with credentials}"
            helper += "\n" + \
                "\t register <username> <password> <privileges> {SignUp request to the system with credentials}"
        else:
            helper += "\n" + \
                "\t delete <username> <password> {Deletes the specified user but provide the password for an admin user}"
            helper += "\n" + \
                "\t change_folder <name> {changes the current folder for the logged in user}"
            helper += "\n" + \
                "\t list {lists the contents for the current folder for the logged in user}"
            helper += "\n" + \
                "\t read <file_name> {returns the contents for the specified file}"
            helper += "\n" + \
                "\t write_file <name> <input> {creates file in doesnot exists and writes to file, if file exists then appends to the file, for current directory}"
            helper += "\n" + \
                "\t create_folder <name> {creates a new folder in the current director}"
        return helper

    def login(self, username, password):
        """Calls the user manager to generate the Login request. Then initializes the FileManager for loggedIn user

        Parameters:
        ------------------------------------------
        username : string
            username for the user
        password: stirng
            password for the user
        Return : string
            response from the UserManager class method login
        """
        data = ""
        status = self.checkLogin(username)
        if status == 1:
            data = "Some other user is already logged in. Open another client to user a new login."
            return data
        elif status == 2:
            data = "This user is already logged in."
            return data
        else:
            data = f"Welcome {username}. Use help command to show available commands"
        data = self.usermanager.logIn(username, password)
        self.user = self.usermanager.getUserCredentials(username)
        self.fileManager = FileManager(
            self.absolutePath + self.user.rootDirectory)
        self.fileManager.createUserDirectory()
        return data

    def delete(self, username, password):
        """Calls the user manager to delete the user. Only works if a user is logged in

        Parameters:
        ------------------------------------------
        username : string
            username to delete
        password: stirng
            password for the logged in account
        Return : string
            response from the UserManager class method deleteUser
        """
        data = "login to use this command"
        if self.user.username != "":
            if self.user.privilege == "admin":
                if self.checkLogin(username) == 2:
                    data = "Cannot delete as user currently logged in"
                else:
                    if self.user.password == password:
                        data = self.usermanager.deleteUser(username)
                    else:
                        data = "incorrect password. Provide password for user currently logged in."
            else:
                data = "You do not have privilges to delete a user."
        return data

    def register(self, username, password, privilege):
        """Calls the user manager to create a new user.

        Parameters:
        ------------------------------------------
        username : string
            username to create
        password: string
            password for the user to create
        privilege: string
            privilege of the user to create i.e. admin|user
        Return : string
            response from the UserManager class method registerUser
        """
        data = ""
        data = self.usermanager.registerUser(username, password, privilege)
        return data

    def checkLogin(self, username):
        """Verifies the login status of specified username

        Parameters:
        ------------------------------------------
        username : string
            username to verify
        Return : string
            0: no user is logged in
            2: specified username is logged in
            1: specified username is not logged in
        """
        if self.user.username == "":
            return 0
        elif self.user.username == username:
            return 2
        else:
            return 1

    def changeFolder(self, name):
        """Calls the file manager to change current folder. Only works if a user is logged in

        Parameters:
        ------------------------------------------
        name : string
            folder path to navigate to
        Return : string
            response from the FileManager class method changeDirectory
        """
        data = "login to use this command"
        if self.user.username != "":
            data = self.fileManager.changeDirectory(name)
        return data

    def list(self):
        """Calls the file manager to fetch directory contents. Only works if a user is logged in

        Return : string
            contents for the current directory for the logged in user
        """
        data = "login to use this command"
        if self.user.username != "":
            data = self.fileManager.listDirectory()
        return data

    def readFile(self, name):
        """Calls the file manager to read a file. Only works if a user is logged in

        Parameters:
        ------------------------------------------
        name : string
            path of file to read
        Return : string
            response from the FileManager class method readFile
        """
        data = "login to use this command"
        if self.user.username != "":
            data = self.fileManager.readFile(name)
        return data

    def writeFile(self, name, data):
        """Calls the file manager to write a file. Only works if a user is logged in

        Parameters:
        ------------------------------------------
        name : string
            path of file to write
        data : string
            data to be written to file
        Return : string
            response from the FileManager class method writeFile
        """
        data = "login to use this command"
        if self.user.username != "":
            data = self.fileManager.writeFile(name, data)
        return data

    def createFolder(self, name):
        """Calls the file manager to create a directory. Only works if a user is logged in

        Parameters:
        ------------------------------------------
        name : string
            path of folder to create
        Return : string
            response from the FileManager class method createDirectory
        """
        data = "login to use this command"
        if self.user.username != "":
            data = self.fileManager.createDirectory(name)
        return data
