# File Name : groupImage.py
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


# Brief Description of what this module does: Creates a class to display our teams group picture
# Citations: ChatGPT

# Anything else thats relevant: Group name: Myra Fleener

from PIL import Image
import matplotlib.pyplot as plt
import os

class picturePrinter():

    def groupImagepyCheck(self):
        """
        Prints to confirm the class and function work
        @params self Self: No params
        @returns N/A
        """
        check = "groupImage.py works"
        print(check)

    def display_group_photo():
        """
        Displays photo of group with sign
        @param image_path: str: The full path to the image file 
        @return None
        """
    
        image_path = os.path.join("Data", "group_photo.jpg")
    
    try:
        image = Image.open(image_path)
        plt.imshow(image)
        plt.axis('off')  
        plt.title("Group Photo")
        plt.show()

    except FileNotFoundError:
        print(f"Error: Could not find the image at {image_path}")