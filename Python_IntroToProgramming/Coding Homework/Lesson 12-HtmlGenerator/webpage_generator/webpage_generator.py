# This program creates an html file using user inputs
# Inputs:  Name, Description
# Outputs: HTML file
# Jose Gonzalez
# Modified Date: Mar,02,2020

def main():
   Name=input("Enter your name:")
   Description=input("Describe yourself")
   fh= open("my_webpage.html","w")
   fh.write(Name+ '\n')
   fh.write(Description)
   fh.close()

main()

   