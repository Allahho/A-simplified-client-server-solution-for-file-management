"""
This module contains the class FileManager, 
A utlity class to manage the directory and file operations for the server.
"""
import os


class FileManager:
    """
    A simple directory and file manager. 
    This is a utility class to manage folder navigation ,creation and file management 

    Attributes:
    -----------------
        root: string
            path to the root directory for operation
        currentFolder: string
            path to folder that user is navigated to all files 
            and folders will be created and read from this folder
    Methods:
    -----------------
        __init__():
            intialize the file manager object
        createUserDirectory():
            creates a user root directory if doesnot exists
        createDirectory():
            creates a directory in current Folder if doesnot exists
        writeFile():
            creates a file if doesnot exists and writes the data to the file. 
            If file exists then appends data to the file
        readFile():
            returns the contents of a file
        changeDirectory():
            naviagtion function to change the current folder
        check_file_exits():
            an inner function to check if a file exists
    """

    def __init__(self, root):
        """Initialize the file manager object. 
           The parameters are passed on to the init function of file manager

        Parameters:
        ------------------------------------------
        root : string
            root directory for operations
        """
        self.root = root
        self.currentFolder = root

    def createUserDirectory(self):
        """creates a user root directory if doesnot exists
        """
        path = self.currentFolder
        response = "Directory Exists"
        if not os.path.exists(path):
            os.makedirs(path)
            response = f'User Directory created {path}'
        return response

    def createDirectory(self, name):
        """creates a folder in current folder with specified name

        Parameters:
        ------------------------------------------
        name : string
            name of the folder to create

        Return : string
            success: Directory Create
            failure: Directory Exists
        """
        path = self.currentFolder + '/' + name
        response = ""
        if not os.path.exists(path):
            os.makedirs(path)
            response = 'Directory created'
        else:
            response = 'Directory exists'
        return response

    def listDirectory(self):
        """returns contents of the current folder

        Return : string
            success: list of contents from the current folder
            failure: Directory is empty
        """
        arr = os.listdir(self.currentFolder)
        response = ""
        if len(arr) == 0:
            response = "Directory is empty"
        else:
            response = '\n'.join(arr)
        return response

    def writeFile(self, name, data):
        """If File exists appends to file otherwise create the file and writes data

        Parameters:
        ------------------------------------------
        name : string
            name of the file
        data : string
            data to be written to file

        Return : string
            success: data appended to file | data written to file
        """
        path = self.currentFolder + '/' + name
        response = ""
        if self.check_file_exits(path):
            file = open(path, 'a')
            file.write(data)
            file.close()
            response = 'data appended to file'
        else:
            file = open(path, 'w+')
            file.write(data)
            file.close()
            response = 'data written to file'
        return response

    def readFile(self, name):
        """Returns contents of  a  file

        Parameters:
        ------------------------------------------
        name : string
            name of the file

        Return : string
            success: contents of the file
            failure: File not found
        """
        path = self.currentFolder + '/' + name
        response = ""
        if self.check_file_exits(path):
            file = open(path, 'r')
            data = file.read()
            file.close()
            response = data
        else:
            response = "File not found"
        return response

    def changeDirectory(self, name):
        """Changes the current folder

        Parameters:
        ------------------------------------------
        name : string
            name of the folder ot navigate to | user can pass .. to navigate outside a folder

        Return : string
            success: Directory Changed
            failure: Directory not found | You are at root directory
        """
        path = self.currentFolder
        response = ""
        if name.startswith(".."):
            if self.currentFolder == self.root:
                response = "You are at root directory"
            else:
                arr = name.split('/')
                arr.pop(0)
                if len(arr) > 0:
                    arr2 = path.split('/')
                    arr2.pop(len(arr) - 1)
                    path = '/'.join(arr2)
                    path += '/'.join(arr)
                else:
                    arr2 = path.split('/')
                    arr2.pop(len(arr) - 1)
                    path = '/'.join(arr2)

                if os.path.exists(path):
                    self.currentFolder = path
                    response = "Directory Changed"
                else:
                    response = "Directory not found"
        else:
            path = self.currentFolder + '/' + name
            if os.path.exists(path):
                self.currentFolder = path
                response = "Directory Changed"
            else:
                response = "Directory not found"
        return response

    def check_file_exits(self, filepath):
        """Verifies if a file already exists

        Parameters:
        ------------------------------------------
        filepath : string
            path of the file to verify

        Return : string
            True: File exists
            False: File doesnot exists
        """
        response = False
        if os.path.isfile(filepath):
            response = True
        return response
