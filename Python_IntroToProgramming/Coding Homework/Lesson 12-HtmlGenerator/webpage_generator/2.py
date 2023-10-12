# This program creates an html file using user inputs
# Inputs:  Name, Description
# Outputs: HTML file
# Jose Gonzalez
# Modified Date: Mar,02,2020

def main():
    Name= input("Enter your name:")
    Description= input('Describe yourself:')

    web_page= open('my_webpage.html','w')
    page= """<html>
    <head>
     
    <title> + Name + </title>
    </head>
    <body>
    <center>
    <h1>+ Name + </h1>
    </center>
    <hr/>
    Description
    <hr/>
    </html>"""

    web_page.write(page)

    web_page.close
main()

   