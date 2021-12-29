import string

textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))

if is_binary_string(open('test.exe', 'rb').read(1024)):
    with open("test.exe", "rb") as f:
        byte = f.read(4)
        print(byte)

else:
    print("text")

