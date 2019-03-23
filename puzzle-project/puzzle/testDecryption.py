import os
import random
import string
from unicodedata import normalize
import optparse
import codecs
import sys
import re
import hashlib
import logging
import time

key = 'abcdefghijklmnopqrstuvwxyz'


def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result


t = decrypt(9,sys.argv[1])
print t
