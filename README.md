# CPSC-4240-Project
Our Canary Token Project for CPSC 4240
# Description 
The purpose of this script is to parse files, and check to see if the files the user specifies have been opened recently
This will allow the user to detect if someone other than them has entered the system recently and can help the catch them
Should the scipt find the files have been opened they will alert the user via email. 

# How to use/run 
1. Download the file
2. If you do not have Python installed you can install it here: https://www.python.org/downloads/source/
3. Open the file with whatever editor you have 
4. Add the name of your files you want to check into the files list, they should be comma seperated. ex files = ["1.txt","2.docs"]
5. Replace the text in the string user_email with your email address 
6. Save the file and exit 
7. Run the Script from the command line with the command Python Canary.py 
8. If it ran successfully the text "Script ran successfully email sent to *your email*" 

# Future plans 
1. In the future this script should be able to run as a process on the machine and not manually 
