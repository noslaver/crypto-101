#!/usr/bin/python
from __future__ import division
import operator

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
relative_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def sort_dict(dict):
    return sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

def load_cipher():
    with open("cipher.txt") as f:
        cipher = f.read()
        return cipher

def decrypt(ciphertext):
    dict = {}
    for char in alphabet:
        freq = (ciphertext.count(char) / len(ciphertext)) * 100
        print "%s: %d times = %f percent" % (char, ciphertext.count(char), freq)
        dict[char] = freq 

    dict = sort_dict(dict)

    for index in range(0, 26):
        ciphertext = ciphertext.replace(dict[index][0], relative_freq[index])

    print ciphertext
        

decrypt(load_cipher())
