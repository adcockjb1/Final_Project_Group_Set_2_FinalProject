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
# Citations: ChatGPT https://chatgpt.com

# Anything else thats relevant: Group name: Myra Fleener

from PIL import Image
import matplotlib.pyplot as plt
#import os

class picturePrinter():

    def display_group_photo(self, image_path):
        """
        Displays photo of group in correct location with movie quote
        @param image_path String: The full path to the image file 
        @return N/A
        """
    
        print("Printing group photo...")
    
        try:
            image = Image.open(image_path)
            plt.imshow(image)
            plt.axis('off')  
            plt.title("Group Photo")
            plt.show()

        except FileNotFoundError:
            print(f"Error: Could not find the image at {image_path}")