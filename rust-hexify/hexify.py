import sys, getopt, binascii

h = sys.argv[1]
if len(h) % 2 != 0:
    h = '0'+h

h = [h[i:i+2] for i in range(0, len(h), 2)]
h = map(lambda x: '0x'+x, h)
h = '[' + ', '.join(h) + ']'
print(h)
