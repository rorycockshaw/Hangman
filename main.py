import random

nouns = open(r"C:\users\roryc\Documents\nouns.txt").read().split()

play_again = True 
while play_again == True: 
    random_index = random.randint(0,len(nouns))

    word = nouns[random_index]

    length = len(word)

    correct_letters = list()
    for i in range(length): 
        correct_letters.append(word[i]) 

    #print(correct_letters)


    temp_word = ""
    for i in range(length): 
        temp_word += "_ "

    temp_list = list()
    for i in range(length): 
        temp_list.append(temp_word[2 * i])

    incorrects = list()
    str_incorrects = ""

    print(temp_word)

    done = False
    while not done: 
        letter = input("Guess a letter: ")
        while len(letter) != 1 or (letter in temp_list or letter in incorrects): 
            letter = input("Invalid guess. Guess a letter: ")
        
        for i in range(length): 
            if correct_letters[i] == letter: 
                temp_list[i] = letter
            elif letter not in correct_letters and letter not in incorrects:  
                incorrects.append(letter) 
                str_incorrects += letter + " "
                
        
        temp_word = ""
        for i in range(length): 
            temp_word += temp_list[i] + " "
        print(temp_word)
        
        print("Incorrect letters so far: " + str_incorrects + "\n")

        if temp_list == correct_letters:
            print("\n You win!")
            encore = input("Would you like to play again? y/n: ")
            if encore.lower() == "y": 
                play_again = True
            else: 
                print("Thanks for playing!")
                play_again = False
            done = True
            
