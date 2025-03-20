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

# wave_02:
# we need to check if word uses only letter from letter bank.
# we need to keep in ind frequancies of each letter in both word and letter bank.
# return True if all letters in word are in letter bank.
# return False if word letter not in letter bank or word use letter more than it appears in letter bank.


def uses_available_letters(word, letter_bank):

    word = word.upper()
    word_freq = {} # counting frequancy for each letter in word
    for letter in word:
        if letter in word_freq:
            word_freq[letter] += 1
        else:
            word_freq[letter] = 1
    
    letter_bank_freq = {} # Count the frequency of each letter in the letter_bank
    for letter in letter_bank:
        letter = letter.upper()  
        if letter in letter_bank_freq:
            letter_bank_freq[letter] += 1
        else:
            letter_bank_freq[letter] = 1
    
    for letter in word_freq:
        if letter not in letter_bank_freq or word_freq[letter] > letter_bank_freq[letter]:
            return False
    
    return True


score_chart =  {"A":1,
                "B":3,
                "C":3,
                "D":2,
                "E":1,
                "F":4,
                "G":2,
                "H":4,
                "I":1,
                "J":8,
                "K":5,
                "L":1,
                "M":3,
                "N":1,
                "O":1,
                "P":3,
                "Q":10,
                "R":1,
                "S":1,
                "T":1,
                "U":1,
                "V":4,
                "W":4,
                "X":8,
                "Y":4,
                "Z":10
                }
# wave_03 :
# we need to create dict that store letter scores.
# then we calculate score that add corresponding freuancy to its letter.
# return total score.

def score_word(word):
    word = word.upper() # change to upper case to compare with score chart.
    total_score = 0

    word_dict = {} # count how many times letter appears.
    for letter in word: #loop through each letter in word.
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1    

    for letter, frequancy in word_dict.items(): # loop each letter to find its frequancy and score and sum scores up.
      total_score += score_chart[letter] * frequancy
    if len(word) >= 7: # extra 8 points apply when word length >7
        total_score += 8
    return total_score




def get_highest_word_score(word_list):
    pass