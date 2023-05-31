#!/usr/bin/env sh
RAW_NOUNLIST_FILES='english-nouns.txt nounlist.txt Wordlist-Nouns-All.txt'
cd noun_lists_raw && cat $RAW_NOUNLIST_FILES | grep -v '[^[:lower:]]' | sort -u > ../nouns.txt
