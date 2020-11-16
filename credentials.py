class Credential :
         """
         Class that generates new instances of credential
         """ 
         credential_list = []# Empty user list

    def __init__(self,accname,first_name,last_name, password):
         """
         user credentials to be stored
         """
         self.accname = accname
         self.first_name= first_name
         self.last_name= last_name
         self.password = password
    
    
    def save_credential(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Credentials.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Credentials.credential_list.remove(self)

    @classmethod
    def find_credential(cls,accname):
        '''
        Method that takes in an account_name and returns credentials that matches that name.
        '''

        for credential in cls.credential_list:
            if credential.accname == accname:
                return credential


    @classmethod
    def credential_exist(cls,accname):
        '''
        Method that checks if a credential exists from the credential list.
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for credential in cls.credential_list:
            if credential.accname == accname:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list

    @classmethod
    def copy_password(cls,accname):
        credential_found = Credentials.find_credential(accname)
        pyperclip.copy(credential_found.password)