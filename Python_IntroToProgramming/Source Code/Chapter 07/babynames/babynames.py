# This program determines if a name is in the top 200
# Inputs:  Female/ Male Name or 'N'=none
# Outputs: Message indicating whether the names were among top 200
# Modified by:  Jose Gonzalez
# Modified Date: Mar 09,2020


def main():
 #Reads Girl name Text file and transforms it into a list/variable

   Girl_Name= open('GirlNames.txt','r')
   GirlName= Girl_Name.readlines()
   Girl_Name.close

  #Formats List
   index=0
   while index <len(GirlName):
         GirlName[index]= GirlName[index].rstrip('\n')
         index +=1

#Reads Boys Name Text file and Transforms it into a List/Variable

   Boy_Name= open('BoyNames.txt','r')
   BoyName= Boy_Name.readlines()
   Boy_Name.close

   #Formats List
   index=0
   while index <len(BoyName):
         BoyName[index]= BoyName[index].rstrip('\n')
         index +=1

   #Start of Inputs/ Outputs
   try:
       #Boys
        InputB= input("Enter a boy's name or N for nothing:")
        if InputB in BoyName:
            print(InputB,"is one of the most popular boy's name")
        elif InputB == ('N') :
            print("You chose to not answer")
        else:
            print(InputB,"is not a popular boy's name")

        #Girls
        InputG= input("Enter a Girl's name or N for Nothing:")
        if InputG in GirlName:
            print(InputG,"is one of the most popular girl's name")
        elif InputG == ('N') :
            print("You chose to not answer")
        else:
            print(InputG,"is not a popular girl's name")

   except IOError:
       print("Please check your files")
main()

