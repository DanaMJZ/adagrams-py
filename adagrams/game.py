from random import randint
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
# wave_01:
# we need to create function that select 10 letters randomly.
# make sure to return letters as list of strings.
# draw_letter() letter selected no  ore times that its available.
# test3 was not passing so I looked up chatgt to see why, went over it with Mikelle to understand.

def draw_letters():
    letter_list = [] # store letters based on their frequancy
    for letter, count in LETTER_POOL.items(): # we used .items() because we need to return a dict with letters:key, count:value
        for i in range(count):
            letter_list.append(letter)
    print(letter_list)


    pulled_letters = [] # pull random letters
    for i in range(10): # max 10 letters
        random_index = randint(0, len(letter_list) - 1) # randint generates random int between 2 values.
        random_letter = letter_list.pop(random_index) # used pop method with help of Mikelle in office hours :)
        pulled_letters.append(random_letter) # adds random letter to the list pulled letter with 

    return pulled_letters

    

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass