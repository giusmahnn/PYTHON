# This is a code on multiplication quiz
# a random module is used to select a random number to multiply with another random number
# a time module creates a pause before the next question and also times each question
# a number of 3 question is given and the answer is defined at 0, if the user gets an answer correct it increases by 1.
# a while statement is used to loop over each code untill its condition is met.
# each question has a max of 3 chances before counting it as wrong and also revealing the answer.
# at the end the correct questions over the number of questions is printed out.




import random, time

numberOfQuestion = 3
answers = 0
for qstnum in range(numberOfQuestion):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    qst = num1*num2
    print('#%s: %s * %s = ' % (qstnum, num1, num2))
    Answer = int(input())
    chances = 1
    
    while Answer != qst:
        print('Try again')
        Answer = int(input())
        if Answer != qst:
            chances += 1
        if chances == 3:
            print('Out of chances')
            print('The answer is: ' + str(qst))
            break
    else:
            print('Correct')
            answers += 1
            time.sleep(1)
print('Your score: %s / %s' %(answers, numberOfQuestion))