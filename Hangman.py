import random
from words import words_list
import string

#function to get words from list
def get_valid_words(words):

    secret_word=random.choice(words)
    while ' ' in secret_word or '-' in secret_word:
        secret_word=random.choice(words)
    
    return secret_word.upper()

def hangman():
    lives=6
    word= get_valid_words(words_list)
    word_set= set(word) #letters in the word
    alphabet = set(string.ascii_uppercase) 
    used_letters = set() #used letters by the user

    while len(word_set)>0 and lives>0:#while the wordset is 0 that means all the letters have been guessed. Lives are taken for each wrong guess
        #letters used
        print('You have used these letters {} '.format(''.join(used_letters)))
        
        word_list  = [i if i in used_letters else '-' for i in word]
        print('Current Word:\t', ''.join(word_list))

        user_input = input('Guess a letter:').upper()
        if user_input in alphabet-used_letters:
            used_letters.add(user_input)
            if user_input in word_set:
                word_set.remove(user_input)#if the user input is in the word then the word is starting to be popped of letters to complete logic.
            else:    
                lives-=1 #if user input not in word the hangman is starting to be drawn?
                print('Letter not in word')
        elif user_input in used_letters:
            print('You have already used these letters')

        else:
            print('Invalid character please try again')
    if lives==0:
        print('You have been hanged')
    else:
        print('You guessed the word{}'.format(word))
hangman()
    #gets here when word_set becomes empty i.e the word is guessed