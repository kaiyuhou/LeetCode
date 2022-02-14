import binascii

with open('lena_color.gif', 'rb') as f:
    print(binascii.hexlify(f.read()))


