#Step 1 
import random
import assets


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = assets.words[random.randint(0,len(assets.words)-1)]
chosen_word_guess = []
lives = 6
for var in chosen_word:
  chosen_word_guess.append("_")

while True:

  for var in chosen_word_guess:
    print(var, end ="")
  print("\n")
  player_input = input("Choose a letter: ")

  if len(player_input) > 1:
    print("Invalid input")
  else:
    if player_input in chosen_word:
      if(player_input in chosen_word_guess):
        print("You already guessed that one :), try a different letter")
      else:
        counter = 0
        for var in chosen_word:
          if player_input == var:
            chosen_word_guess[counter] = var
          counter+=1
          
        if "_" not in chosen_word_guess:
          print (assets.HANGMANPICS[len(assets.HANGMANPICS)-lives-1])
          print ("You win ;)")
          
          break
        print (assets.HANGMANPICS[len(assets.HANGMANPICS)-lives-1])

    else:
      lives-=1
      if lives == 0:
        print (assets.HANGMANPICS[len(assets.HANGMANPICS)-lives-1])
        print ("Game Over :(")
        break
      print("Wrong, you loose a life")
      print (assets.HANGMANPICS[len(assets.HANGMANPICS)-lives-1])

    
      
    