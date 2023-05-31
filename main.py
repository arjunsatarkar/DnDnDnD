#!/usr/bin/env python3
import argparse
import sys

parser = argparse.ArgumentParser(prog="D&D&D&D", description="Dungeons & Dragons D...")
parser.add_argument("word_num", default=None, nargs="?", type=int)
args = parser.parse_args()
word_num = args.word_num

WORDLIST_FILE_PATH = "nouns.txt"

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
