
string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"

val2 = int(string2, base=16)
val1 = int(string1, base=16)

val3 = val1 ^ val2
print(hex(val3))
