# File Name : main.py
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


# Brief Description of what this module does: Solves the scavenger hunt and prints a picture of our success
# Citations: ChatGPT https://chatgpt.com

# Anything else thats relevant: Group name: Myra Fleener

from locationPackage.location import*
from moviePackage.movie import*
from groupImagePackage.groupImage import*

def main():
    path = "Data/"
    encryptedGroupHintsFile = path + "EncryptedGroupHints Spring 2025.json"
    teamsAndEncryptedMessagesForDistributionFile = path + "TeamsAndEncryptedMessagesForDistribution.json"
    englishFile = path + "UCEnglish.txt"
    groupPic = path + "group_photo.jpg"
    teamName = "Myra Fleener"


    # -- Decrypt the location from the three files given --
    locationDecrypter = locationDecrypt()

    # Creates Dict
    hints = locationDecrypter.readJSONFile(encryptedGroupHintsFile)
    # Creates List
    english = locationDecrypter.readTXTFile(englishFile)

    hintWords = locationDecrypter.translateNumbersToWords(hints[teamName], english)
    locationDecrypter.translateListToWords(hintWords)
    

    # -- Decrypt the movie using the fernet algorithm here --
    movieDecrypter = movieDecrypt()

    key = b"___325px9Qm4Sq1OrAgutpUHzAj49W0J9oHrRVhS2yg=" 
    teamsAndEncryptedMessages = locationDecrypter.readJSONFile(teamsAndEncryptedMessagesForDistributionFile)
    ourToken = teamsAndEncryptedMessages[teamName][0]
    decryptedMovieInfo = movieDecrypter.fernetEncript(key,ourToken)
    

    # -- Display the image of our success here --
    printer = picturePrinter()
    
    printer.display_group_photo(groupPic)

if __name__ == "__main__":
    main()