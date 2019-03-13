# This code starts off the story with the "no" branch and offers a retry going a different path.

print(
    "It is a cold spring day in China, during the Han dynasty. Your father is a retired soldier, who fought against many foes. He was the best soldier in the kingdom")

print('\n', "After saving many villages and towns in nearby areas so many years ago, he settled down with his family. ")

print('\n', "He asks if you would be wanting to follow in his footsteps.", '\n')

# This code starts the game off with answering whether you want to play. If not, you get shamed for it. If you do, the game begins.

answer = input("Will you accept the quest of becoming the Middle Kingdom's bravest soldier? ")

if answer == ("no"):
    print("You have brought dishonor to your family due to not accepting your father's offer. A new soldier emerges, however he is not of your family bloodline.")
    print('\n',"Your family shames you for not accepting the offer. ",'\n')
    try_again = input("Would you like too go back and make a different decision? ")
    if try_again == ("yes"):
        print('\n',"Rerun the game and try a new path!")

    elif try_again == ("no"):
        print('\n',"Your fate has been sealed.")

elif answer == ("yes"):
    print("You choose to embark on the quest of serving in your father's place. Your training begins in 2 months.")
    print('\n', "2 months later...")
    print('\n', "Today is training day one. You are taken into a group of 59 other men, making you a group of 60.")

else:
    print('\n',"You need to print yes or no. Try again.",'\n')
    

# This code starts you off with the first day of training, and you need to input how you did. This code will become a new branch, as every layer will become a new branch at some point.

while answer == ("yes"):
    print('\n',"Because you are in the Han dynasty, you need to remember to not back down from fighting. If you fail with training, you fail those who expect greatness in you.")
    print('\n', "You are first taught swordfighting. After many sessions, you are told how you did.",'\n')
    grade = input("How did you do? Print poor/good/: ")
    if grade == ("poor"):
        print("You need to try harder!")
        continue
    elif grade == ("good"):
        print('\n',"Good job!")
        break
    else:
        print("Invalid input. Please say good, great, or poor.",'\n')
        continue

# This if statement is made to clear out extra indents, and makes sure you are on the good path of the story.

if answer == ("yes") and grade == ("good"):
    print("Good job! After a few days of swordfighting, your group moves on to archery.",'\n')
    print("You start off with 4 targets each on top of each other. Put in 4 scores between 0 and 100.",'\n')
    sum = 0
    for i in range(4):
        score = int(input("Enter a score between 0 and 100: "))
        if score > 100:
            print("That score is not achievable. Stay in the range of 0 to 100.",'\n')
        elif score >= 0 and score < 101:
            sum = score + sum
            print("Your total is " + str(sum) + ".")

if sum >= 200 or sum <= 400:
    print("Excellent! You are ready to be classed as a trained soldier!",'\n')

print("You are about to be classed after completing your long time of training.",'\n')


