import random
import re

def hangman():
    file = open('20k.txt', 'r')
    l = file.readlines()
    l = list(map(lambda x: x[:-1], l))
    l.sort()

    word = l[random.randint(0, len(l))]
    while len(word) < 5:
        word = l[random.randint(0, len(l))]
    mistery = word[0] + ' '
    blank = ' '.join(['_' for i in range (len(word) - 2)])
    mistery = mistery + blank + ' ' +word[-1]
    mistery = list(mistery)
    letters_tried = {word[0], word[-1]}

    for index in [m.start() for m in re.finditer(word[0], word)]:
        mistery[2 * int(index)] = word[int(index)]
    for index in [m.start() for m in re.finditer(word[-1], word)]:
        mistery[2 * int(index)] = word[int(index)]
    print(word,"  ", "".join(mistery), "        Tries left: 8")
    i = 8

    while i > 0:
        guess = ''
        while len(guess) != 1:
            guess = input()
            if guess == 'guess':
                guess = input()
                print("So, you think that the word is ", guess, " ?")
                if guess == word:
                    print('Yes, you are right!')
                    return
                else:
                    print('Sorry, but you are wrong')
                    A = set([x for x in guess])
                    B = set([x for x in word])
                    i = i - len(A.difference(B))
                    if i <= 0:
                        print('You failed')
                        return
                    letters_tried.union(A)
                    if i >= 1:
                        print("Tries left: ", i)
            elif len(guess) != 1:
                print("Type just a letter!")
        if guess in letters_tried:
           print("You have already tried that. Try something different")
        elif guess not in set(word):
            i = i - 1
            print("Sorry, pal, try again","        Tries left: ", i)
            letters_tried.add(guess)
        else:
            for index in [m.start() for m in re.finditer(guess, word)]:
                mistery[2 * int(index)] = word[int(index)]
            letters_tried.add(word[int(index)])
            print("".join(mistery), "        Tries left: ", i)
        if '_' not in mistery:
            print("You won! Congratulations!")
            return
    else:
        print('No more tries! You failed')

hangman()
