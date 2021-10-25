
INTRODUCTION = ''' 
************************************************************************
                           Matchmaker 1.0
            Helping singles finding their other half since 2021
                          Lovefinder,Inc. 
************************************************************************
Are you dreaming of finding a true love but you are constantly finding 
wrong partners. Are you tired of going on a disastrous dates? Me too! 
By answering 5 questions this program will find out if we are meant to 
be together. To each question answer:
5 if you strongly agree, 
4 if you agree, 
3 if you neither agree or disagree, 
2 if you disagree, and 
1 if you strongly disagree. 

Well, let's see if our personalities match to each other!

Enter a number between 1 and 5

'''

QUESTION = [
    'I love camping!', 
    'People should travel at least once a year.',
    'I hate strawberries!',
    'I prefer dogs over cats.',
    'I like to watch horror movies.'
]


DESIRED_REPONSE = [
    5, # strongly agree
    5, # strongly agree
    1, # strongly disagree 
    5, # Strongly agree
    2  # Agree 
]


MAX_SCORE = 5 * len(QUESTION)

print(INTRODUCTION)

response = []
compatibility = []

# Ask all the questions.
def requestAValidNumberBetween1And5():
    for i in range(len(QUESTION)): 
        userResponse = int(input(QUESTION[i]))
        # Todo: Validate response and ask question again if necessary. 
        response.append(userResponse)
        

        questionCompatability = 5 - abs(userResponse - DESIRED_REPONSE[i])
        compatibility.append(questionCompatability)

        # String formatting with parameters and placeholders
        print('Question %d compatibility: %d\n' % (i+1, questionCompatability))

    totalCompatibility = 0
    for c in compatibility:
        totalCompatibility += c

    totalCompatibility *= 100 / MAX_SCORE
    print('Total Compatibility: %d\n\n' % (totalCompatibility))



    userResponseString = str(input("Enter an number between 1 and 5.\n"))
    print("You entered: " + userResponseString) 

    print(userResponseString.isnumeric())

    if not userResponseString.isnumeric():
        print("This is not a number!")
        return False
    else:
        # print("This is a valid number")
        userResponse2Int = int(userResponseString)
        if (userResponse2Int < 1) or (userResponse2Int > 5):
            print("\nThis is not a number between 1 and 5.")
            return False
        else:
            print("\nThis is a nuber between 1 and 5. Great job!")
            return True

userHasEnteredANumberBetween1And5 = False
while  not userHasEnteredANumberBetween1And5:
    userHasEnteredANumberBetween1And5 = requestAValidNumberBetween1And5()
    print(userHasEnteredANumberBetween1And5) 
    if not userHasEnteredANumberBetween1And5:
        print("Please try again.")