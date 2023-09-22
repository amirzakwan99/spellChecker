# Spellchecker program
# Group 5

import sys
from tkinter import *

def vp_start_gui():
    global root
    root = Tk()
    root.title("Spell Checker")
    root.geometry("400x650")
    root.iconbitmap("SC.ico")

    import string

    def main():
        global input1, button1
        label1 = Label(root, text="\nPlease enter a word: ").pack()
        input1 = Entry(root, width=25)
        input1.pack()
        button1 = Button(root, text="Enter", command=algo)
        button1.pack()

    def words():
        with open('ukdictionary.txt', 'r', encoding='cp437') as word:
            W = [wordlist.strip() for wordlist in word.readlines()]
            W = set(W)
        return W

    def check(s, w):
        if s in w:
            ending()
        else:
            giveSuggestion(s, w)

    # find the error when it does not match in dictionary
    def findError(s):

        # split the string
        split = []  # [('t','rash'),('tr','ash')]
        for i in range(len(s) + 1):
            split_word = (s[:i], s[i:])
            split.append(split_word)

        # delete a character
        delete = []  # [rash, tash, trsh, trah, tras]
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
            if right:  # mula2 semua kat kanan
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
        real_suggestions.sort()

        if len(real_suggestions) == 0:
            label2 = Label(root, text="Your word is completely misspelled.").pack()
        else:
            label2 = Label(root, text="\nDid you mean: ").pack()
            w = StringVar()

            for sugg3 in real_suggestions:
                Radiobutton(root, text=sugg3, variable=w, value=sugg3, tristatevalue='x', command=lambda: enableCB(w.get())).pack(anchor=W)

            global chooseB
            chooseB = Button(root, text="Choose this one", command=ending, state=DISABLED)
            chooseB.pack()

    def enableCB(word):
        if word:
            chooseB.config(state=NORMAL)

    def algo():
        s = input1.get()
        s = s.casefold()
        w = words()
        check(s, w)

    def ending():
        correct = Label(root, text="\nCongratulations, your word is spelled correctly !").pack()
        button1.config(state=DISABLED)
        repeat = Button(root, text="Play Again", command=refresh).pack()
        leave = Button(root, text="Exit", command=exit).pack()


    main()
    root.mainloop()


if __name__ == '__main__':
    def refresh():
        root.destroy()
        vp_start_gui()

    vp_start_gui()
