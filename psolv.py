from random import choice
import string
from time import time

# word_list = ['cat', 'dog', 'rabbit']
#
# letter_list = [c for c in "".join(word_list)]
#
# no_dupe = []
# for c in letter_list:
#     if c not in no_dupe:
#         no_dupe.append(c)
#
# set_list = set(letter_list)
#
# print(letter_list)
# print(set_list)
# print(no_dupe)

# Infinite monkey problem

alphabet = string.ascii_lowercase
goal = "methinks it is like a weasel"


def generate_sentence(old_attempt):
    att_list = old_attempt.split(" ")
    goal_list = goal.split(" ")

    new_att_list = []
    if len(att_list) == len(goal_list):
        for att_word, goal_word in zip(att_list, goal_list):
            # If we have that word, continue
            if att_word == goal_word:
                new_att_list.append(att_word)

            elif len(att_word.strip()) == len(goal_word):
                n_word = ""

                for letter_index in range(len(goal_word)):
                    if att_word[letter_index] == goal_word[letter_index]:
                        n_word += att_word[letter_index]
                    else:
                        n_word += choice(alphabet)

                new_att_list.append(n_word)

            else:
                new_att_list.append("".join(choice(alphabet) for _ in goal_word))

        return " ".join(new_att_list)

    else:
        return " ".join(["".join([choice(alphabet) for c in d]) for d in goal.split()])


def score(attempt):
    level = 0
    att_split = attempt.split()
    goal_split = goal.split()

    # Check if we have four words
    if len(att_split) == len(goal_split):
        level += 1

        for c in range(len(goal_split)):
            if att_split[c].strip() == goal_split[c].strip():
                level += 1

    return level / (len(goal_split) + 1) * 100


def main():
    start = time()
    done = False
    counter = 0
    att = ""
    while not done:
        counter += 1
        att = generate_sentence(att)
        sc = score(att)
        done = sc == 100

        if sc >= 50:
            print(f"An attempt is --{att}-- score is {sc}%")

        if counter % 1000 == 0 and sc <= 50:
            print(f"The program has taken {(time() - start) / 60} minutes so far and {counter} attempts")
            print(f"Attempt looks like --{att}--")

    end = time()
    print(f"We got it! -**{att}**-")
    print(f"It only took {(start - end) / 60} minutes and {counter} tries")


if __name__ == '__main__':
    main()
