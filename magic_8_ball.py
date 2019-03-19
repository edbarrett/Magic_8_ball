import random
import importlib
from array import *
from check_profanity import checkProfanity

#def magic():


def m8Ball():

    #Get the question
    print("What is your question?")
    question = input()
    #TODO
    #remove the \n from input text before storing in the text file.

    #TODO
    #Implement profanity checker here
    checker_answer = checkProfanity(question)
    #print(type(checker_answer))
    #print(checker_answer)
    if checker_answer is True:
        print("You are bad!")


    #Store the question
    F_question = open('questions.txt', 'a', encoding = 'UTF-8')
    F_question.write(question + '\n')
    F_question.close()

    #Generating a random number 1 -> 20
    answer_number = random.randrange(1,20)

    #Giving the user their answer
    F_answer = open('possibleAnswers.txt', 'r')
    answer = F_answer.readlines()
    print(answer[answer_number])
    F_answer.close()


def main():
    #Call the 8Ball function
    m8Ball()

if __name__ == '__main__':
    main()
