################ Function Definitions ################
# import module to use the average funtion
import statistics

# Shows the user what options they have
def displayMenu():
  
  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")
  
  # This option will end the program
  print("6. Quit")

  # This promt will take users input for the option selection as a number
  option = input("Please select the number for options to work on: ")
  
  return option

  
# Prompts the user to enter a numeric grade
  
# This function works, and ensures the user entered a valid float for the grade
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val

# This funtion will take the average grade and return a letter grade
def getLetterGrade(average):
  if average >= 90:
   letter = "A"
  elif 79 < average < 89:
   letter = "B"
  elif 69 < average < 79:
    letter = "C"
  elif 59 < average < 69:
    letter = "D"
  elif 49 < average < 59:
    letter = "E"
  elif average < 49:
    letter = "F"
  else:
    letter = "unknown"
    
  return letter
  
################ Main Program ################
# Initiate the variable for option selection
option = "0"
# Create an empty list to hold student grades
studentGrades = []
# Create an empty string to hold student names
name = ""
# Create an empty dictionary to hold name and grade list
studentDict = {name : studentGrades}

# Application Loop will run unless option 6 is selected
while(option != "6"):

  # Prompt the user to select an option
  print()
  option = displayMenu()
  # Control flow to evaluate which option is selected and appropriate funtions/code block is ran
  if option == "1":
    name = input("Enter student name: ")
    studentDict[name] = []
  elif option == "2":
    name = input("Enter student name: ")
    # When name is expected as an input it will be checked using control flow for existance in the list
    if name in studentDict:
      studentDict.pop(name)
    else:
      print("Name does not exist.")
  elif option == "3":
    name = input("Enter student name: ")
    if name in studentDict:
      numGrade = getNumberGradeFromUser()
      # Add the numeric float to the student list value
      studentDict[name].append(numGrade)
      print(f"Added {numGrade} to {name}'s quizzes.")
    else:
      print("Name does not exist.")
  elif option == "4":
    name = input("Enter student name: ")
    if name in studentDict:
      print(f"{name}'s Quizzes: ")
      for grades in studentDict[name]:
        print(grades)
    else:
      print("Name does not exist.")
  elif option == "5":
    name = input("Enter student name: ")
    if name in studentDict:
      # This code block uses the mean funtion to average the student numaric grades in the list
      avgGrade =  statistics.mean(studentDict[name])
      # getLetterGrade funtion is used with the average numerical value as an input, it return a letter grade, which is held in the letterGrade variable
      letterGrade = getLetterGrade(avgGrade)
      print(f" {name}'s current grade is {letterGrade}")
    else:
      print("Name does not exist.")

