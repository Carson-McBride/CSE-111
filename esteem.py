

def main(): 
    total_score = 0 
    score = 0 

    print ("I feel that I am a person of worth, at least on an equal plane with others.")
    score = positive_score()
    total_score = score_calculator(score, total_score)

    print ("I feel that I have a number of good qualities.")
    score = positive_score()
    total_score = score_calculator(score, total_score)
    print ("All in all, I am inclined to feel that I am a failure.")
    score = negative_score()
    total_score = score_calculator(score, total_score)
    print ("I am able to do things as well as most other people.")
    score = positive_score()
    total_score = score_calculator(score, total_score)
    print ("I feel I do not have much to be proud of.")
    score = negative_score()
    total_score = score_calculator(score, total_score)
    print ("I take a positive attitude toward myself.")
    score = positive_score()
    total_score = score_calculator(score, total_score)
    print ("On the whole, I am satisfied with myself.")
    score = positive_score()
    total_score = score_calculator(score, total_score)
    print ("I wish I could have more respect for myself.")
    score = negative_score()
    total_score = score_calculator(score, total_score)
    print ("I certainly feel useless at times.")
    score = negative_score()
    total_score = score_calculator(score, total_score)
    print ("At times I think I am no good at all.")
    score = negative_score()
    total_score = score_calculator(score, total_score)

    print(f'your score is {total_score}')
    return 

def positive_score():
    answer = input("Enter D, d, a, or A: ")
    if answer == "D":
        score = 0 
    elif answer == "d":
        score = 1 
    elif answer == "a":
        score = 2
    elif answer == "A":
        score = 3 
    float (score)
    return score

def negative_score():
    answer = input("Enter D, d, a, or A: ")
    if answer == "A":
        score = 0 
    elif answer == "a":
        score = 1 
    elif answer == "d":
        score = 2
    elif answer == "D":
        score = 3 
    float (score)
    return score 

def score_calculator(score, total_score):
    new_score = score + total_score 

    return new_score

main() 