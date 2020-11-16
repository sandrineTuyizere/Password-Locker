import unittest # Importing the unittest module
from credential import Credentials # Importing the credentials class
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("twitter","sandy","Tuy","wooow1",) # create credentials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.accname,"twitter")
        self.assertEqual(self.new_credential.first_name,"sandy")
        self.assertEqual(self.new_credential.last_name,"Tuy")
        self.assertEqual(self.new_credential.password,"wooow1")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credential.test_save_credential() # saving the new credentials
        self.assertEqual(len(Credentials.credential_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []


    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple user
            objects to our user_list
            '''
            self.new_credential.test_save_credential()
            test_save_credential = Credentials("instagram","Anny","sea","second") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_credential(self):
        '''
        test_delete_credentials to test if we can remove a credential from our credentials list
        '''
        self.new_credential.save_credential()
        test_credential= Credentials("instagram","Anny","sea","second") # new user
        test_credential.save_credential()

        self.new_credential.delete_credential() # Deleting a contact object
        self.assertEqual(len(Credentials.credential_list),1)


    def test_find_credential_by_password(self):
        '''
        test to check if we can find a credentials by password and display information
        '''

        self.new_credential.save_credential()
        test_credential= Credentials("instagram","Anny","sea","second") 
        test_credential.save_credential()

        found_credential = Credentials.find_by_password("second")

        self.assertEqual(found_credential.last_name,test_user.last_name)


    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns a user that matches that password.

        Args:
            password: Password to search for
        Returns :
            User of person that matches the password.
        '''

        for credential in cls.credential_list:
            if credential.password == password:
                return credential
   


if __name__ == '__main__':
    unittest.main()