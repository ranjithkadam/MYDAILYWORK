# Implementing the Quiz_Game

name = input("Enter Your Name ")

#Greeting the player

print("Welcome to Quiz Game ",name)
print("\nGame Process & Rules :\n"  )
print("-> Total 5 questions each carries 5 points\n")
print("-> All Questions are Multiple-Choice \n")
print("-> Each has 4 options And choice any one\n")
print("-> Your Score Displayed After Completion of Game\n")
decision = input("Are you Ready to Play ?\n")
score = 0
if(decision == "Yes" ):
    
   first=input("Are you for First Question?    (Yes/No)\n")
   if(first == "Yes"):
      print("Question 1:")
      print("Which of the following planets is closest to the Sun?\n")
      print("A) Mars\nB) Venus\nC) Jupiter\nD) Saturn\n")
      choice = input("Enter Your Option ")
      if(choice == "B" or choice== "b"):
         print("Wow...Correct Answer !!!\n\n")
         score=score+5
         print("Your score is ",score,"\n")
      else:
          print("Oo..Oo, Wrong Answer.")
   else:
       print("Thank You For Visiting..")
       exit
       
   second=input("Are you Ready for Second Question?    (Yes/No)\n")
   if(second == "Yes"):
       print("Question 2:\n")
       print("What is the chemical symbol for the element Gold?\n")
       print("A) Au\nB) Ag\nC) Fe\nD) Cu\n")
       choice = input("Enter Your Option ")
       if(choice == "A" or choice== "a"):
          print("Excellent...Correct Answer !!!\n\n")
          score=score+5
          print("Your score is ",score,"\n")
       else:
          print("Oo..Oo, Wrong Answer.\n")   
   else:
       print("Thank You For Visiting..\n")
       exit()

   third = input("Are you Ready for Third Question?    (Yes/No)\n")
   if(third == "Yes"):
       print("Question 3:\n")
       print("Who wrote the play 'Romeo and Juliet'? \n")
       print("A) William Shakespeare\nB) Charles Dickens\nC) Jane Austen\nD) F. Scott Fitzgerald\n")
       choice = input("Enter Your Option ")
       if(choice == "A" or choice== "a"):
          print("Greate...Correct Answer !!!\n\n")
          score=score+5
          print("Your score is ",score,"\n")
       else:
          print("Oo..Oo, Wrong Answer.\n")   
   else:
       print("Thank You For Visiting..\n")
       exit()

   fourth = input("Are you Ready for Fourth Question?    (Yes/No)\n")
   if(fourth == "Yes"):
       print("Question 4:\n")
       print("Which country is the largest by land area?\n")
       print("A) Russia\nB) Canada\nC) China\nD) United States\n")
       choice = input("Enter Your Option ")
       if(choice == "A" or choice== "a"):
          print("Super...Correct Answer !!!\n\n")
          score=score+5
          print("Your score is ",score,"\n")
       else:
          print("Oo..Oo, Wrong Answer.\n")   
   else:
       print("Thank You For Visiting..\n")
       exit()
 
   fifth = input("Are you Ready For Fifth Question?     (Yes/No)\n ")
   if(fifth == "Yes"):
       print("Question 5:\n")
       print("What is the capital city of Australia?\n")
       print("A) Sydney\nB) Melbourne\nC) Canberra\nD) Brisbane\n")
       choice = input("Enter Your Option ")
       if(choice == "C" or choice== "c"):
          print("G O A T...Correct Answer !!!\n\n")
          score=score+5
          print("Your score is ",score,"\n")
       else:
          print("Oo..Oo, Wrong Answer.\n")   
   else:
       print("Thank You For Visiting..\n")
       exit()
   print("Game Over !!!\nYour Score is ",score)
   
else:
    print("Thank You For Visiting.")
