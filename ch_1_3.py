import statistics
### https://www.gutenberg.org/files/1342/1342-0.txt
import string
import math
import re

letters = string.ascii_uppercase
input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
results = {}
# read in English letter frequencies
d = {k: math.log(float(v)/100) for k, v in (l.strip().split('\t') for l in open("/Users/peterbouman/Desktop/pycrypt/frequencies"))}
Ninput = int(input, base=16)
for i in range(1, 256):
    coder = ("{0:#0{1}x}".format(i, 4)[2:])*int(len(input)/2)
    codenum = int(coder, base=16)
    decrypt = Ninput ^ codenum
    plainhex = hex(decrypt)[2:]
    plainchars = [chr(int(plainhex[i:i+2],16)) for i in range(0,len(plainhex),2)]
    plaintext = "".join(plainchars)
    upper_alpha = [char1.upper() for char1 in plainchars if char1.upper() in letters]
    scored_alphas = list(map(lambda letter: d[letter], upper_alpha)) 
    dkey = statistics.mean(scored_alphas) if len(scored_alphas) > 0 else -999
    print("".join(upper_alpha), dkey)
    results[dkey] = plaintext

#for key, value in sorted(results.items()):
#    print("{} : {}".format(key, value))
best = max(results.keys())
