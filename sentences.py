import random

def main():
    print (f'{get_determiner(1)} {get_noun(1)} {get_verb(1, "past")}')
    print (f'{get_determiner(1)} {get_noun(1)} {get_verb(1,"present")}')
    print (f'{get_determiner(1)} {get_noun(1)} {get_verb(1,"future")}')
    print (f'{get_determiner(2)} {get_noun(2)} {get_verb(2,"past")}')
    print (f'{get_determiner(2)} {get_noun(2)} {get_verb(2,"present")}')
    print (f'{get_determiner(2)} {get_noun(2)} {get_verb(2,"future")}')
    return 



def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    cap_word = word.capitalize()
    return word


def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1 :
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1 :
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    word = random.choice(words)
    return word

main()
