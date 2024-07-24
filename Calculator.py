# Program for Implementing a Simple Calculator

print("\n\n***WELCOME to Calculater ***\n")
# Reading Input Numbers from User
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

 
while(True):
   # Reading Arthmetic operator from User
   print("\nEnter, What Arthmetic Operation You want ?\n""1. Addition \n2. Substraction \n3. Multiplication"+
        " \n4. Division or \n5.Modulous Division")
   operator = input("Please , Enter your Choice ")

   #Performing Operations According to User Input
   if(operator == "1" or operator == "Addition"):
      s = a + b
      print("\n\nAddition of ",a," and ",b,"is " ,s,"\n\n")
      
   elif(operator == "2" or operator == "Substraction"):
      s = a - b
      print("\n\nSubstraction of ",a," and ",b,"is " ,s,"\n\n")
      
   elif(operator == "3" or operator == "Multiplication" ):
      s = a * b
      print("\n\nMultiplication of ",a," and ",b,"is " ,s,"\n\n")
      
   elif(operator == "4" or operator == "Division" ):
      s = a // b
      print("\n\nDivision of ",a," and ",b,"is " ,s,"\n\n")
      
   elif(operator == "5" or operator == "Modulous Division"):
      s = a % b
      print("\n\nModulous Division of ",a," and ",b,"is " ,s,"\n\n")

   else:
       print("\n\nEntered Invalid Option...\n\n")
       break
