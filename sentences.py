import random

def main():
    print (f'{get_prepositional_phrase(1)} {get_determiner(1)} {get_noun(1)} {get_verb(1, "past")}')
    print (f'{get_prepositional_phrase(1)} {get_determiner(1)} {get_noun(1)} {get_verb(1,"present")}')
    print (f'{get_prepositional_phrase(1)} {get_determiner(1)} {get_noun(1)} {get_verb(1,"future")}')
    print (f'{get_prepositional_phrase(2)} {get_determiner(2)} {get_noun(2)} {get_verb(2,"past")}')
    print (f'{get_prepositional_phrase(2)} {get_determiner(2)} {get_noun(2)} {get_verb(2,"present")}')
    print (f'{get_prepositional_phrase(2)} {get_determiner(2)} {get_noun(2)} {get_verb(2,"future")}')
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

def get_proposition():
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    proposition = get_proposition()

    propositional_phrase = (f'{proposition} {determiner} {noun}')
    return propositional_phrase 
main()
