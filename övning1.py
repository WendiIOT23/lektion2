#Be användaren skriva två strängar
#Om de är lika långa, skriv ut ”Lika långa!”
#Om de har samma innehåll, skriv ut ”Samma!”
#----------------------------------
#ask for input
print("Please give two strings")
str1 = input("String 1: ")
str2 = input("String 2: ")

#Check length of strings
if len(str1) == len(str2):
    print("lika långa")
    
#Check if they are the same
if str1 == str2:
    print("samma")
    
  