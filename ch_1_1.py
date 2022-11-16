from base64 import b64encode, b64decode

# hex -> base64
s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
b64 = b64encode(bytes.fromhex(s)).decode()
print('cafebabe in base64:', b64)

# base64 -> hex
s2 = b64decode(b64.encode()).hex()
print('yv66vg== in hex is:', s2)
assert s == s2

