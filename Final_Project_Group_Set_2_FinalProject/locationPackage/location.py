# File Name : location.py
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
# Brief Description of the assignment: Solves a scavenger hunt and provides picture proof that we were there


# Brief Description of what this module does: Decrypts the location assigned to our team
# Citations: 

# Anything else thats relevant:

import json

class locationDecrypt():

    def readJSONFile(self, filePath):
        """
        Reads a .json file into Python data structures
        @params filePath String: Path to the file to convert
        @returns data Dictionary: A dictionary of data from the file
        """
        with open(filePath, 'r') as file:
            data = json.load(file)
        return data

    def readTXTFile(self, filePath):
        """
        Reads a .txt file into Python data structures
        @params filePath String: Path to the file to convert
        @params filePath String: 
        @returns data List: A list of data from the file
        """
        with open(filePath, 'r') as file:
            data = [line.strip() for line in file if line.strip()]
        return data

    def getWordsFromNumbers(self, ):
        """
        Make a string of the words translated from the line file
        @params filePath String: Path to the file to convert
        @params filePath String: 
        @returns data List: A list of data from the file
        """
        with open(filePath, 'r') as file:
            data = [line.strip() for line in file if line.strip()]
        return data