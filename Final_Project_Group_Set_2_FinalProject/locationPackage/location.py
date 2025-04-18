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
# Brief Description of the assignment: Solves a scavenger hunt and provides picture proof of solution


# Brief Description of what this module does: Creates a class to decrypt the location assigned to our team
# Citations: 

# Anything else thats relevant: Group name: Myra Fleener

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

    def translateNumbersToWords(self, numbers, english):
        """
        Make a list from the numbers translated using the english file
        @params numbers List: The list containing all of the numbers
        @params english List: The list of UC english words
        @returns englishList List: A list of translated words
        """
        englishList = []
        
        i = 0
        while i < len(numbers):
            currentNumberString = numbers[i]
            currentNumber = int(currentNumberString)
            currentNumberInEnglish = english[currentNumber]

            englishList.append(currentNumberInEnglish)

            i += 1
        return englishList

    def translateListToWords(self, untranslatedList):
        """
        Make a string from a list of words
        @params untranslatedList List: The list containing all of the numbers
        @returns translatedString String: The string derived from the given list
        """
        translatedString = ""

        i = 0
        for word in untranslatedList:
            if i == 0:
                word = word.capitalize()
                translatedString = word + " "
            elif i == len(untranslatedList) - 1:
                translatedString = translatedString + word + "."
            else:
                translatedString = translatedString + word + " "

            i = i + 1
        return translatedString