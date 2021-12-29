import string
import itertools

def istext(filename):
    a = []
    s=open(filename).read(512)
    for b in range(32, 127):
        a.append(chr(b))
    a.append('\n\r\t\b')
    text_characters = "".join(a)
    _null_trans = maketrans("", "")
    if not s:
        # Empty files are considered text
        return True
    if "\0" in s:
        # Files with null bytes are likely binary
        return False
    # Get the non-text characters (maps a character to itself then
    # use the 'remove' option to get rid of the text characters.)
    t = s.translate(_null_trans, text_characters)
    # If more than 30% non-text characters, then
    # this is considered a binary file
    if float(len(t))/float(len(s)) > 0.30:
        return False
    return True

if not istext('file.jfif'):
    with open("file.jfif", "rb") as f:
        byte = f.read(1)
        while byte:
            byte = f.read(1)
            print(byte)

else:
    print("text")

