print("Welcome to my computer quiz!")

score = 0
playing = input("Do you want to play ")

if playing.lower() !="yes":
 print("Okay, Thank you")
 quit()

print ("Okay, lets play :)")

answer=input("How many days are in a week ")
if answer.lower() != "7":
 print("Incorrect")
if answer == "7":
 print("Correct :D")
 score += 1 

answer=input("Is Amazon a big company? ")
if answer.lower() == "yes":
 print("Correct :D")
 score += 1 
else:
  print("Incorrect")

answer=input("Is the earth round? ")
if answer.lower() == "yes":
 print("Correct :D")
 score += 1 
else:
  print("Incorrect")

answer=input("Is the guitar a musical instrument? ")
if answer.lower() == "yes":
 print("Correct :D")
 score += 1 
else:
  print("Incorrect")

print("you got " + str(score) + " questions correct")
print("you got " +str((score/4)*100) +"% correct")