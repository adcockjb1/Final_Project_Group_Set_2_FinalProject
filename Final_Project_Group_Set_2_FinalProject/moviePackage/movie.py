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
# Citations: ChatGPT

# Anything else thats relevant: Group name: Myra Fleener

from cryptography.fernet import Fernet

class movieDecrypt():

    def fernetEncript(self, key, ourToken):
        """
        Decripte messtage encripted with Fernet encryption scheme
        @param key String: The fernet key
        @param token String: The encripted file
        @return String: The decripted message
        """
        f = Fernet(key)

        plaintext = f.decrypt(ourToken)
        decryptedMovieInfo = plaintext.decode()
        print(decryptedMovieInfo)

        return decryptedMovieInfo
