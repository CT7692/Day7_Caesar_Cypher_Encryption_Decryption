alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-3: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"
    

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 



#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

##########  Function definitions:

def text_validator(option_a, option_b, prompt):
  correct = True
  user_input = input(prompt).lower()
  
  if (user_input != option_a) and (user_input != option_b):
    correct = False
    while not correct:
      print("Please enter one of the two options and try again.")
      user_input = input(prompt)
      if(user_input == option_a) or (user_input == option_b):
        correct = True
  return user_input


def shift_validator(lower_limit, higher_limit, prompt):
  correct = True
  num = int(input(prompt))

  if(num < lower_limit) or (num > higher_limit):
    correct = False
    while not correct:
      print("Please enter a number between 0 and 26 and try again.")
      num = int(input(prompt))

      if(num > lower_limit) or (num <= higher_limit):
        correct = True
  return num


def caesar(text, shift, option):
  if option == "decode":
    shift *= -1
  
  input_list = list(text)
  new_list = []
  position = 0
  
  for i in input_list:
    if i.isalpha():
      position = alphabet.index(i) + shift
      if position >= len(alphabet):
        position -= len(alphabet)
      i = alphabet[position]
      new_list.append(i)
    else:
      new_list.append(i)

  final_text = ''.join(new_list)
  print(f"The {direction}d text is {final_text}")

##########  End of function definitions.

import art
print(art.logo)

direction_prompt = "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
shift_prompt = "Type the shift number:\n"
repetition_prompt = "\nKeep going? Type 'yes' or 'no'.\n"

keep_going = True
while keep_going:
  direction = text_validator(option_a="encode", option_b="decode", prompt=direction_prompt)
  text = input("Type your message:\n").lower()
  shift = shift_validator(lower_limit=0, higher_limit=25, prompt=shift_prompt)
  caesar(text, shift, direction)
  user_choice = text_validator(option_a="yes", option_b="no", prompt=repetition_prompt)
  if user_choice == "yes":
    keep_going = True
  elif user_choice == "no":
    keep_going = False
    print("\nSee ya!")