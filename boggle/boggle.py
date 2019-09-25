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
    for key in dictionary:
        root.add(key)
    return root

def generate_board(n):
    return [[choice(alphabet) for _ in range(n)] for _ in range(n)]

def adjacent(i, j, n):
    return [(x, y) for x, y in [(i + 1, j), (i, j + 1), (i + 1, j + 1), (i - 1, j), (i, j - 1), (i - 1, j - 1)]
            if x > -1 and x < n and y > -1 and y < n]

def add_words(i, j, n, board, lang, words):
    prefixes = []
    prefixes.append((board[i][j], i, j))
    while len(prefixes) > 0:
        s, x, y = prefixes.pop()
        if lang.isword(s, prefix=True):
            if s in lang:
                words.add(s)
            for l, k in adjacent(x, y, n):
                sx = s + board[l][k]
                if lang.isword(sx, prefix=True):
                    prefixes.append((sx, l, k))

def main():
    #print(create_language_trie(load_dictionary()))
    lang = create_language_trie({'key'})
    n = 4
    #board = generate_board(4)
    board = [list('dail'), list('isai'), list('dkey'), list('yhnr')]
    print('key' in lang)
    pprint(board)
    words = set()
    for i in range(n):
        for j in range(n):
            add_words(i, j, n, board, lang, words)
    pprint(words)

if __name__ == '__main__':
    main()
