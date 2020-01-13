"""Tests for `FileManager.py`."""
import unittest
import os
import inspect
from datetime import datetime
from FileManager import FileManager


class FileManagerTestCase(unittest.TestCase):
    """Tests for `FileManager.py`."""
    username = "TestUser"+datetime.now().strftime("%Y%m%d%H%M%S")

    def test1_create_user_directory(self):
        """Checks if a user directory is created, checking for a user folder called TestUser"""
        absolutepath = os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe())))
        userRoot = absolutepath+"/User/" + self.username
        fmanager = FileManager(userRoot)
        fmanager.createUserDirectory()
        self.assertTrue(os.path.exists(userRoot))

    def test2_create_directory(self):
        """Checks if a user directory is created, checking for a user folder called TestUser"""
        absolutepath = os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe())))
        absolutepath += "/User/" + self.username + "/"
        testFolder = "testfolder"
        userRoot = absolutepath+testFolder
        fmanager = FileManager(absolutepath)
        if os.path.exists(userRoot):
            response = fmanager.createDirectory(testFolder)
            self.assertEqual(response, "Directory exists")
        else:
            response = fmanager.createDirectory(testFolder)
            self.assertEqual(response, "Directory created")

    def test3_list_directory_empty(self):
        """Checks folder called TestFolder2 when its empty"""
        absolutepath = os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe())))
        absolutepath += "/User/" + self.username + "/"
        testFolder = "testfolder2/"
        userRoot = absolutepath+testFolder
        fmanager = FileManager(absolutepath)
        fmanager.createDirectory(testFolder)
        fmanager = FileManager(userRoot)
        response = fmanager.listDirectory()
        self.assertEqual(response, "Directory is empty")

    def test4_list_directory_contents(self):
        """Checks folder called TestUser and get its contents"""
        absolutepath = os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe())))
        absolutepath += "/User/" + self.username + "/"
        testFolder = "testfolder/"
        userRoot = absolutepath+testFolder
        fmanager = FileManager(userRoot)
        fmanager.createDirectory("innerFolder")
        fmanager.createDirectory("innerFolder2")
        fmanager.createDirectory("innerFolder3")
        response = fmanager.listDirectory()
        self.assertEqual(response, "innerFolder\ninnerFolder2\ninnerFolder3")

    def test5_write_file_new(self):
        """Checks a file called TestFile.txt in TestUser/testfolder and verify it is created"""
        absolutepath = os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe())))
        absolutepath += "/User/" + self.username + "/"
        testFolder = "testfolder/"
        userRoot = absolutepath+testFolder
        fmanager = FileManager(userRoot)
        response = fmanager.writeFile("TestFile.txt", "This is a test file")
        self.assertEqual(response, "data written to file")

    def test6_write_file_append(self):
        """Checks a file called TestFile.txt in TestUser/testfolder and append to it"""
        absolutepath = os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe())))
        absolutepath += "/User/" + self.username + "/"
        testFolder = "testfolder/"
        userRoot = absolutepath+testFolder
        fmanager = FileManager(userRoot)
        response = fmanager.writeFile("TestFile2.txt", "This is a test file")
        response = fmanager.writeFile("TestFile2.txt", "This is a test file")
        self.assertEqual(response, "data appended to file")

    def test7_read_file(self):
        """Checks a file called TestFile.txt and reads its contents"""
        absolutepath = os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe())))
        absolutepath += "/User/" + self.username + "/"
        testFolder = "testfolder/"
        userRoot = absolutepath+testFolder
        fmanager = FileManager(userRoot)
        fmanager.writeFile("TestFile.txt", "This is a test file")
        response = fmanager.readFile("TestFile.txt")
        self.assertIn("This is a test file", response)

    def test8_change_directory_inner(self):
        """Checks navigation to a folder with change directory"""
        absolutepath = os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe())))
        absolutepath += "/User/" + self.username + "/"
        testFolder = "testfolder/"
        userRoot = absolutepath+testFolder
        fmanager = FileManager(userRoot)
        fmanager.createDirectory("cFolder")
        response = fmanager.changeDirectory("cFolder")
        self.assertEqual(response, "Directory Changed")

    def test9_change_directory_outer(self):
        """Checks folder navigation outside a folder"""
        absolutepath = os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe())))
        absolutepath += "/User/" + self.username + "/"
        testFolder = "testfolder"
        userRoot = absolutepath+testFolder
        fmanager = FileManager(userRoot)
        fmanager.createDirectory("cOFolder")
        fmanager.changeDirectory("cOFolder")
        response = fmanager.changeDirectory("..")
        self.assertEqual(response, "Directory Changed")

    def test9_change_directory_root(self):
        """Checks folder navigation outside root"""
        absolutepath = os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe())))
        absolutepath += "/User/" + self.username + "/"
        fmanager = FileManager(absolutepath)
        response = fmanager.changeDirectory("..")
        self.assertEqual(response, "You are at root directory")


if __name__ == '__main__':
    unittest.main()
