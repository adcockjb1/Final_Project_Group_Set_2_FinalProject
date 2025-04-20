# File Name : movie.py
# Group name : Final Project Group Set 2
# Student Name: Joseph Adcock
#               Kengo Ishizuka
#               Omar Alkhawaga
# email: adcockjb@mail.uc.edu
#        ishizuko@mail.uc.edu
#        alkhawoe@mail.uc.edu
# Assignment Number: Final Project
# Due Date:   04/30/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Solves a scavenger hunt and provides picture proof of solution


# Brief Description of what this module does: Creates a class to decrypt the movie assigned to our team
# Citations: 

# Anything else thats relevant: Group name: Myra Fleener

from cryptography.fernet import Fernet

class movieDecrypt():

    def moviepyCheck(self): # What is this code for?
        """
        Prints to confirm the class and function work
        @params self Self: No params
        @returns check String: A string stating that it works
        """
        check = "movie.py works"
        return(check)

    def fernetEncript(self, key, ourToken):
        """
        Decripte messtage encripted with Fernet encryption scheme
        @param key : The fernet key
        @param token : The encripted file
        @return String: The decripted message
        """
        f = Fernet(key)
        token = ourToken

        plaintext = f.decrypt(token)
        decriptedMovieInfo = plaintext.decode()
        print(plaintext.decode())

        return decriptedMovieInfo
