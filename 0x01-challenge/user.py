#!/usr/bin/python3
""" 
Contains a User class
"""

class User():
    """ Represents a user with an email """

    def __init__(self):
        """ Initializes a new instance """
        self.__email = None

    @property
    def email(self):
        """ Getter and setter pair for the email property """
        return self.__email

    @email.setter
    def email(self, value):
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value
   
    
if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
