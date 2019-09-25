#!/usr/bin/env python3
from random import choice
from pprint import pprint

import json

from trie import TrieNode

alphabet = list('abcdefghijklmnopqrstuvwxyz') # In english, obviously

def load_dictionary():
    with open('words_dictionary.json', 'r') as infile:
        return json.load(infile)

def create_language_trie(dictionary):
    root = TrieNode()
    root.add('test')
    root.add('testicles')
    return root

def generate_board(n):
    return [[choice(alphabet) for _ in range(n)] for _ in range(n)]

def main():
    print(create_language_trie({}))
    pprint(generate_board(4))

if __name__ == '__main__':
    main()
