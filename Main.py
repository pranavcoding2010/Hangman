from asyncio import get_child_watcher
import random
a = (input("enter your name ?"))
print("Goodluck ",a)
words = ["tiger","doctor","elephant","programming","hospital","police","ants","football","teacher","construction","tenis","gaming","batman","garden","oceans"]
b = random.choice(words)
print("Guess the character of the word")
c = ''
turn = 12
while (turn > 0):
    failure = 0
    for char in b :
        if char in c:
            print(char)
        else :
            print('_')
            failure +=1
    if failure == 0 :
        print("You win!")
        print("Congratulation")     
        print("The word is",b)    
        break
    guess = input("Guess a character")
    c += guess
    if guess not in b :
        turn -=1
        print("Wrong")
        print("You have so many turns left")
        if  turn == 0 :
            print("You lose")
    

    
