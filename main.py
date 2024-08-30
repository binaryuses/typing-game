import random
import time

score = 0

timer = 2.5

def loadWordsFromFile(filename):
    with open(filename, 'r') as file:
        words = set(line.strip() for line in file)
    return words

words = loadWordsFromFile("words.txt") 

def getWord():
    return random.choice(list(words))

def newWord():
    global score
    current_word = getWord()
    start_time = time.perf_counter()
    print("New Word: [" + current_word + "]")
    msg = input("---> ")
    end_time = time.perf_counter()

    elasped = end_time - start_time
    if msg.lower() == current_word.lower() and elasped < timer:
        score += 1
        print("+1 score")
        return newWord()
    elif elasped >= timer:
        print("You ran out of time :( Here's your score: " + str(score))
    else:
        print("Whoops, you lost! Here's your score: " + str(score))
        msg = input("would you like to play again (Y/N): ")
        if msg.lower() == "y":
         for x in range(4):
             count -= 1
             time.sleep(1)
             print("Starting in.. " + str(count))
         newWord()  
        else:
            print("Goodbye")

startingPrompt = input('"Start" to play typing game: ')
if startingPrompt.lower() == "start":
    count = 4
    for x in range(4):
        count -= 1
        time.sleep(1)
        print("Starting in.. " + str(count))
    newWord()     
else: 
    print("Goodbye")