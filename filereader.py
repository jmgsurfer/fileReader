import sys
import binascii
import json
#
# magic number search url: https://filesignatures.net/
#
# magic_numbers = { "4d 5a 90 00":"Binary: MZ, Windows executable file.", "47 49 46 38":"Binary: GIF file"}
# mn_json = json.dumps(magic_numbers, indent = 4)
# with open('mn_db.json','w') as mn_database:
#     json.dump(mn_json, mn_database)
#
# get json db file and convert into dict
with open('mn_db.json') as magic_numbers_db_json:
    magic_numbers_db = json.load(magic_numbers_db_json)
print(magic_numbers_db)
# check if binary
textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
#
#
if is_binary_string(open(sys.argv[1], 'rb').read(1024)):
    with open(sys.argv[1], "rb") as f:
        byte = f.read(4)
        data = binascii.hexlify(byte, ' ').decode('ascii')
        print(data)

else:
    print("Text file.")

