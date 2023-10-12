# This program calculates butterfly population estimates
# Inputs:  males, estimated number of male butterflies
#          females, estimated number of female butterflies
# Outputs: total butterflies, sex ratio, variance, Gender Difference, Mating pairs
# Written by: C. Conner
# Modified by:  Jose Gonzalez
# Modified Date: Feb 03, 2020

 # I have the very unfortunate habbit of random capitalization so this is just a precaution :/
Print= print

#Start
print("Butterfly Estimator\n")

#Input

Males= int(input("What is the Estimated male Population?:"))
Females= int(input("What is the Estimated Female Population?:"))

# Perform Calculations
Total_Butterflies = Males + Females
Sex_Ratio = Males // Females
Ratio_Variance = Males % Females
Gender_Difference = abs(Males-Females)
Mating_Pairs = Males * Females

# Output Ressults
print("\nTotal Butterflies: ", Total_Butterflies)
print("Sex Ratio          :", Sex_Ratio)
print("Variance           :", Ratio_Variance)
print("Gender Difference  :", Gender_Difference)
print("\nAnd lastly...\nMating Pairs       :", Mating_Pairs)

