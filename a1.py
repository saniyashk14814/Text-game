#Guess the word.
#The code asks you for a genre and a difficulty level and then gives you 10 guesses to guess the WORD based on the genre.

#importing random to use random.choice() later
import random

#creating a function to get a random word from all the categories
def word():
  #creating a netsed dictionary for different genres
  categories = {
    #'animals[0]' storing 3 lettered animals name
    #'animals[1]' storing 5 lettered animals name
    #'animals[2]' storing 10 lettered animals name
    'animals': [['Ant', 'Bat', 'Cow', 'Fox', 'Hen', 'Pig', 'Owl', 'Bee', 'Elk', 'Emu'],
                ['Panda', 'Eagle', 'Koala', 'Lemur', 'Tiger', 'Zebra', 'Rhino', 'Sheep', 'Whale', 'Bison'],
                ['Rhinoceros', 'Woodpecker', 'Chinchilla', 'Swordtails', 'Salamander', 'Earthworms', 'Crocodiles',
                 'Chameleons', 'Kingfisher', 'Armadillos']],
    #'things[0]' storing 3 lettered things name
    #'things[1]' storing 5 lettered things name
    #'things[2]' storing 10 lettered things name
    'things': [['Pen', 'Cup', 'Hat', 'Car', 'Key', 'Box', 'Bag', 'Fan', 'Rug', 'Bed'],
               ['Chair', 'Table', 'Clock', 'Knife', 'Plate', 'Shoes', 'Flask', 'Plant', 'Radio', 'Brush'],
               ['Helicopter', 'Toothpaste', 'Microphone', 'Sunglasses', 'Smartphone', 'Calculator', 'Microscope',
                'Skateboard', 'Paintbrush', 'Binoculars']],
    #'names[0]' storing 3 lettered names
    #'names[1]' storing 5 lettered names
    #'names[2]' storing 10 lettered names
    'names': [['Amy', 'Ben', 'Eva', 'Jay', 'Zoe', 'Mia', 'Dan', 'Max', 'Leo', 'Ava'],
              ['Ethan', 'Grace', 'Maria', 'Kevin', 'Sarah', 'David', 'Laura', 'Jacob', 'Emily', 'Chloe'],
              ['Jacqueline', 'Washington', 'Antonietta', 'Montserrat', 'Alessandra', 'Anastasios', 'Cornelious',
               'Guillotine', 'Maximilian', 'Alessandra']]
    }

  #giving genre choice to user
  print("Choose one genre from the following")
  print("Enter 1 for animals")
  print("Enter 2 for things")
  print("Enter 3 for names")
  #inputing user's genre choice
  choice1 = input("Enter your choice: ")

  #if the choice is invalid then exiting
  if choice1 not in ['1', '2', '3']:
    print("Invalid choice. Exiting.")
    exit()

  #giving user difficulty choice
  print("Enter 1 for easy: 3 letter word")
  print("Enter 2 for medium: 5 letter word")
  print("Enter 3 for hard: 10 letter word")
  #inputing user's difficulty choice
  choice2 = input("Enter your choice: ")

  #if the choice is invalid then exiting
  if choice2 not in ['1', '2', '3']:
    print("Invalid choice. Exiting.")
    exit()

  #returing a random word using "random.choice()"
  return random.choice(categories['animals' if choice1 == '1' else 'things' if choice1 == '2' else 'names'][int(choice2) - 1]).upper()

#creating a function "game" to do the main work
def game(word):
  print("You have 10 guesses")
  
  #creating a list to store all the guessed letter
  guessed_letters = []
  
  #this statement stores underscores based on user's choice(3,5,10 underscores according to the difficulty level choosen)
  correct_guesses = ['_' for _ in word]

  #having a "cnt" variable to count the number of tries it takes for user to guess the word
  cnt=0

  #running loop till the break statement
  while True:
    #incrementing "cnt" value each time while is true
    cnt=cnt+1

    #printing how much the user has guessed
    print(" ".join(correct_guesses))#joining all the elements, by space, of correct_guesses into a string and pronting it
    
    #asking the user to guess the letter
    guess = input("Guess a letter of the word: ").upper()
  
    #priting "You already guessed that letter." if that letter is already guessed by user
    if guess in guessed_letters:
      print("You already guessed that letter.")
      continue

    #adding all the guessed letters to a list
    guessed_letters.append(guess)

    #checking if the letter guessed by user is in the word
    if guess in word:
      #enumerate saves the index of letter in "i" and letter in "letter"
      for i, letter in enumerate(word):
        #if the guessed letter is equal to guessed letter than storing it in "correct_guesses"
        if letter == guess:
          correct_guesses[i] = guess
      #if there are no underscore in the word then printing appropriate message and the full word
      if '_' not in correct_guesses:
        #joining all the elements of correct_guesses into a string and printing it
        print(" ".join(correct_guesses))
        print("YAYY!!! YOU GOT THE WORD IN ", cnt, " GUESSES!! HAVE A NICE DAY")
        #once the word is guessed exiting the loop
        break

    #if the guess is not correct then printing "Incorrect guess!"
    else:
        print("Incorrect guess!")

    #if the user fails to guess the word in 10 tries then printing "Sorry, you didn't guess the word. Better luck next time!"
    if len(guessed_letters) >= 10:
      print("Sorry, you didn't guess the word. Better luck next time!")
      #breaking out of loop if user fails to guess the word
      break

#calling the function "word()" and storing the random word in "word" variable
word = word()

#calling the "game" function and passing the random word recieved from "word" function
game(word)

# Name: Saniya Shaikh

