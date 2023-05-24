#!/usr/bin/env python3
import sys

try:
    word_num = int(sys.argv[1])
except IndexError:
    word_num = None

WORDLIST_FILE_PATH = "corncob_lowercase.txt"

with open(WORDLIST_FILE_PATH, "r") as wordlist_file:
    valid_words = set(
        [
            word[0].upper() + word.rstrip()[1:]
            for word in wordlist_file.readlines()
            if word.startswith("d")
        ]
    )

sys.stdout.write("Dungeons & Dragons")
for word in valid_words:
    if word_num is not None:
        if word_num <= 0:
            break
        word_num -= 1
    sys.stdout.write(" & " + word)
print()
