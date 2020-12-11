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
import ast

alphabet_dec = list(string.ascii_letters + string.digits + string.punctuation + string.whitespace + "\002" + "\003")

def bwt_decode(r):
    table = [""] * len(r)  # Make empty table
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
    s = [row for row in table if row.endswith("\003")][0]  # Find the correct row 
    return s.rstrip("\003").strip("\002")  # Get rid of start and end markers

def mtf_decode(sequence, symboltable):
    chars, pad = [], symboltable[::]
    for indx in list(sequence):
        char = pad[int(indx)]
        chars.append(char)
        pad = [pad.pop(int(indx))] + pad
    return ''.join(chars)

def remove_padding(padded_encoded_text):
    padded_info = padded_encoded_text[:8]
    extra_padding = int(padded_info, 2)
    padded_encoded_text = padded_encoded_text[8:] 
    encoded_text = padded_encoded_text[:-1*extra_padding]

    return encoded_text

def decode_text(encoded_text, reverse_mapping):
    current_code = ""
    decoded_text = []

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_mapping:
            character = reverse_mapping[current_code]
            decoded_text.append(character)
            current_code = ""

    return decoded_text

def decompress(comp_file_name):
    global alphabet_dec
    result_path = os.path.join(os.path.dirname(comp_file_name),"decompressed")
    with open(comp_file_name, 'rb') as file, open(result_path, 'w') as output:
        inp = file.readlines()
        dict_str = inp[0].decode("UTF-8")
        map_decode = ast.literal_eval(dict_str)
        map_decode = {v: k for k, v in map_decode.items()}
        to_do = b''.join(inp[1:])
        bit_string = ""

        for i in to_do:
            bit_string += bin(i)[2:].rjust(8, '0')            
        
        encoded_text = remove_padding(bit_string)
        decompressed_text = bytes(decode_text(encoded_text, map_decode))
        mtf_dec = mtf_decode(decompressed_text, alphabet_dec)
        
        bwt_dec = bwt_decode(mtf_dec)
        output.write(bwt_dec)
        output.close()

decompress(file_name)