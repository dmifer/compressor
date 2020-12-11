from tkinter import filedialog
from tkinter import *

# Select file

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file")
file_name = root.filename

# Compressing

import numpy as np
import string 
from heapq import heappush, heappop, heapify
from collections import Counter
import os

alphabet_enc = list((string.ascii_letters + string.digits + string.punctuation + string.whitespace + "\002" + "\003").encode())


def mtf_encode(strng, symboltable):
    sequence, pad = [], symboltable[::]
    for char in strng:
        indx = pad.index(char)
        sequence.append(indx)
        pad = [pad.pop(indx)] + pad
    return bytes(sequence)

def bwt_encode(s):
    s = b"\002" + s + b"\003"  # Add start and end of text marker
    table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
    last_column = [row[-1:] for row in table]  # Last characters of each row
    return b"".join(last_column)  # Convert list of characters into string
 

def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return dict(sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))


# functions for compress
def get_encoded_text(text):
    encoded_text = ""
    symb2freq = Counter(text)
    huff = encode(symb2freq)
    for char in text:
        encoded_text += huff[char]
    return encoded_text, huff


def pad_encoded_text(encoded_text):
    extra_padding = 8 - len(encoded_text) % 8
    for i in range(extra_padding):
        encoded_text += "0"

    padded_info = "{0:08b}".format(extra_padding)
    encoded_text = padded_info + encoded_text
    return encoded_text


def get_byte_array(padded_encoded_text):
    b = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
        byte = padded_encoded_text[i:i+8]
        b.append(int(byte, 2))
    return b


def compress(init_path):
    global alphabet_enc
    result_path = os.path.join(os.path.dirname(init_path),"compressed")
    with open(init_path, 'rb') as file, open(result_path, 'wb') as output:
        text = file.read()
        text = bwt_encode(text)
        text = mtf_encode(text, alphabet_enc)
        encoded_text, map_codes = get_encoded_text(text)
        padded_encoded_text = pad_encoded_text(encoded_text)
        b = get_byte_array(padded_encoded_text)

        output.write(str(map_codes).encode() + b"\n" + bytes(b))
        output.close()


compress(file_name)
