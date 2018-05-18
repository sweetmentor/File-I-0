def printMenu():
    print("Options:")
    print("1. Ask Questions")
    print("2. Add a Question")
    print("3. Exit Game")

    options = input("Please choose an option from (1-3): ")
    
    score = 0
    
    if options == "1":
        f = open('questions.1.txt', 'r')
        lines = f.read().split('\n')
        f.close()

        number_of_questions= len(lines)
 
        for line in lines:
            question, answer = line.split('|')
            guess = input(question + ': ').lower()
            if answer == guess:
                print("right!")
                score += 1
                print(score)
            else:
                print("wrong")
                print(score)
        print("You got {0} correct out of {1}".format(score, number_of_questions))
        printMenu()     
    
    elif options == "2": 
        print("Add your question")
        f = open('questions.1.txt', 'a')
        questions = input("Enter the question: ")
        question = str(f.write('\n' + questions + '|'))
        answers = input("Enter the answer: ")
        question = str(f.write(answers))
        printMenu() 
    
    elif options == "3": 
        print("So you're done playing?")
        return None 
    
    else: 
        print("That's not an option. Please try again.")
        printMenu()
    
        
printMenu()