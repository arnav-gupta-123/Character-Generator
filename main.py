#function that converts lists to strings
def listtostring(s):   
  str1 = ""  
  for i in s:  
    str1 += i   
  return str1 

#creates a character with a name, class, and a weapon based on the user's choice
def create_char():
  name_char = input("Type your character's name. ").lower()
  print()
  class_char = input("Type your character's class. ").lower()
  print()
  weapon_char = input("Type your character's weapon. ").lower()
  text_file = open("characters.txt", "a")  
  character_list = [name_char, class_char, weapon_char]
  character_str = ";".join(character_list) + ';' + '\n'
  text_file.writelines(character_str)
  text_file.close()

#deletes a character whose name the user inputs. Removes from the characters.txt file
def delete_char():
  file = open("characters.txt", "r")
  rest_of_chars = []
  user_input = input("What character's information would you like to delete? ").lower()
  for line in file:
    if not line.startswith(user_input):
      rest_of_chars.append(line)
  file.close()
  file = open("characters.txt", 'w')
  file.writelines(rest_of_chars)
  file.close()

#displays a character whose name the user inputs. Written as a sentence.
def display_char():
  what_char = input("What character's information would you like to display? ").lower()
  text_file = open("characters.txt", "r")
  read = text_file.readlines()
  i = 0
  while i < len(read):
    x = listtostring(read[i])
    x = x.split(';')
    if what_char == x[0]:
      print()
      print(x[0] + " is a(n) " + x[1] + " and uses a(n) " + x[2] + '.')
    i = i + 1
  text_file.close()

#Displays all the characters in the file. Written as a table.
def display_all_chars():
  text_file = open("characters.txt", "r") 
  x = text_file.readlines() 
  i = 0
  if len(x) > 0:
    print("Name\t\t Class\t\t  Weapon") 
    print("---------------------------------")
  while i < len(x):
    y = listtostring(x[i])
    y = y.split(';')
    i = i + 1
    spaces = "            "
    print((y[0] + spaces)[:12] + " " + (y[1] + spaces)[:12] + " " + (y[2] + spaces)[:12])
  text_file.close()

#Main Game Function. Has a menu for user to choose what to do.
def main():
  StartGame = ''
  while StartGame != "5":
    StartGame = input(" Press 1 to create a character. \n Press 2 to delete a character. \n Press 3 to display a character. \n Press 4 to display all the characters. \n Press 5 to exit. ")
    print()
    if StartGame == "1":
      create_char()
    elif StartGame == "2":
      delete_char()
    elif StartGame == "3":
      display_char()
    elif StartGame == "4":
      display_all_chars()
    print()
    #Accounting for User Error
    while StartGame not in ("1","2","3","4","5"):
        print("Your response is incorrect. Please enter a number from 1-5.")
        print()
        StartGame = input(" Press 1 to create a character. \n Press 2 to delete a character. \n Press 3 to display a character. \n Press 4 to display all the characters. \n Press 5 to exit. ")
        print()
        if StartGame == "1":
          create_char()
        elif StartGame == "2":
          delete_char()
        elif StartGame == "3":
          display_char()
        elif StartGame == "4":
          display_all_chars()
        print()

#calling main function
main() 
