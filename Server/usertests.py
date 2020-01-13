"""Tests for `UserManager.py`."""
import unittest
from datetime import datetime
from UserManager import UserManager


class UserManagerTestCase(unittest.TestCase):
    """Tests for `UserManager.py`."""
    username = "TestUser"+datetime.now().strftime("%Y%m%d%H%M%S")

    def test1_register_user(self):
        """Checks if a user is created"""
        umanager = UserManager()
        response = umanager.registerUser(
            self.username+"1", "Root@123", "admin")
        self.assertEquals(response, "user registered")

    def test2_register_user_exists(self):
        """Checks if a user is created when same username already exists"""
        umanager = UserManager()
        response = umanager.registerUser(
            self.username+"2", "Root@123", "admin")
        response = umanager.registerUser(self.username+"2", "Root@123", "user")
        self.assertEquals(response, "user already exists")

    def test3_login_user(self):
        """Checks if a user login is successful"""
        umanager = UserManager()
        response = umanager.registerUser(
            self.username+"3", "Root@123", "admin")
        response = umanager.logIn(self.username+"3", "Root@123")
        self.assertEquals(response, "Log In Success")

    def test4_login_username_false(self):
        """Checks if a user login is successful with wrong username"""
        umanager = UserManager()
        response = umanager.registerUser(
            self.username+"4", "Root@123", "admin")
        response = umanager.logIn(self.username+"789", "Root@123")
        self.assertEquals(response, "Unknown user")

    def test5_login_password_false(self):
        """Checks if a user login is successful with wrong password"""
        umanager = UserManager()
        response = umanager.registerUser(
            self.username+"5", "Root@123", "admin")
        response = umanager.logIn(self.username+"5", "Root123")
        self.assertEquals(response, "Password incorrect")

    def test6_delete_user(self):
        """Checks if a user is deleted successfully"""
        umanager = UserManager()
        response = umanager.registerUser(
            self.username+"6", "Root@123", "admin")
        response = umanager.deleteUser(self.username+"6")
        self.assertEquals(response, "User deleted")

    def test6_delete_user_false(self):
        """Checks if a user is deleted successfully with wrong username"""
        umanager = UserManager()
        response = umanager.deleteUser(self.username)
        self.assertEquals(response, "User not found")


if __name__ == '__main__':
    unittest.main()
