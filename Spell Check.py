# Spellchecker program
# Group 5

import string

# read words from file, encoding: take into account all character
def words():
    with open('ukdictionary.txt', 'r', encoding='cp437') as word:
        W = [wordlist.strip() for wordlist in word.readlines()]
        W = set(W)
    return W


# check words in dictionary or not, if not call error
def check(s, w):
    if s in w:
        print('Your word: ' + s + ' was spelled correctly!')
        repeat()
    else:
        #print('Did you mean(put number to answer): ')
        giveSuggestion(s, w)


# find the error when it does not match in dictionary
def findError(s):

    # split the string
    split = []#(['t','rash'],['tr','ash'] ...)
    for i in range(len(s) + 1):
        split_word = (s[:i], s[i:])
        split.append(split_word)

    # delete a character
    delete = []#['rash', 'tash', 'trsh', 'trah', 'tras']
    for left, right in split:
        if right:
            delete.append(left + right[1:])

    # swap character
    swap = []
    for left, right in split:
        if len(right) > 1:
            swap.append(left + right[1] + right[0] + right[2:])

    # replace character
    replace = []
    alphabet = string.ascii_lowercase
    for left, right in split:
        if right:  #at start, everything is on the right
            for letters in alphabet:
                replace.append(left + letters + right[1:])
    # add one character
    insert = []
    for left, right in split:
        if right:
            for letters in alphabet:
                insert.append(left + letters + right)

    # set the similar suggested word with the input by user
    # give suggestion and try to swap replace delete and split the word to see the words
    return delete + swap + replace + insert


def giveSuggestion(s, w):
    # finding all possible word
    suggestion2 = []
    for sugg1 in findError(s):
        for sugg2 in findError(sugg1):
            suggestion2.append(sugg2)

    # finding the suitable possible word
    suggestions = findError(s) or suggestion2 or [s]
    real_suggestions = []
    for Word in suggestions:
        if Word in w:
            real_suggestions.append(Word)
    real_suggestions = list(set(real_suggestions))




    # check if possible word is there or not
    # print all the possible word suggestion
    # ask user to put which word do they mean and print it out
    if len(real_suggestions) == 0:
        print("Your word is completely misspelled.")
    else:
        print('Did you mean(choose number to answer): ')
        for i in range(len(real_suggestions)):
            print(str(i + 1) + ". " + str(real_suggestions[i]))
        chosen_word = int(input('Choice: '))
        if chosen_word in range(1, len(real_suggestions) + 1):
            print("Your word is finally correct! It is: " +
                  real_suggestions[(chosen_word - 1)])
        else:
            while chosen_word not in range(1, len(real_suggestions) + 1):
                chosen_word = input(
                    'The number you entered is not in the range. Please retry: '
                )
                chosen_word = int(chosen_word)
            print("Your word is finally correct! It is: " +
                  real_suggestions[(chosen_word - 1)])
    repeat()


def repeat():
    print('\nDo you want to check for another word?')
    decide = input('Enter (Y) to continue, other keys to stop: ')
    decide = decide.upper()
    print('\n')
    if decide == 'Y':
        main()
    else:
        print('See you again!')


def main():
    s = input("Put one word: ")  # user input
    s = s.casefold()  # case insensitivity
    w = words()
    check(s, w)  #the check function


print("Welcome to Spellchecker! ")
main()