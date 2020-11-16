import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("sandy","Tuy","wooow1",) # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"sandy")
        self.assertEqual(self.new_user.last_name,"Tuy")
        self.assertEqual(self.new_user.password,"wooow1")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []


    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Anny","sea","second") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Anny","sea","second") # new user
        test_user.save_user()

        self.new_user.delete_user() # Deleting a contact object
        self.assertEqual(len(User.user_list),1)


    def test_find_user_by_password(self):
        '''
        test to check if we can find a user by password and display information
        '''

        self.new_user.save_user()
        test_user = User("Anny","sea","second") 
        test_user.save_user()

        found_user = User.find_by_password("second")

        self.assertEqual(found_user.last_name,test_user.last_name)


    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns a user that matches that password.

        Args:
            password: Password to search for
        Returns :
            User of person that matches the password.
        '''

        for user in cls.user_list:
            if user.password == password:
                return user
   


if __name__ == '__main__':
    unittest.main()