import sys
import binascii
import json
#
# [X] Add error handle (ie: not in db.json)
# [ ] Add function adding new magic number to db.json
#  
# magic number search url: https://filesignatures.net/
#
# magic_numbers = { "4d 5a 90 00":"Binary: MZ, Windows executable file.", "47 49 46 38":"Binary: GIF file"}
# mn_json = json.dumps(magic_numbers, indent = 4)
# with open('mn_db.json','w') as mn_database:
#     json.dump(mn_json, mn_database)
#
# get json db file and convert into dict
#
def usage():
    print("Usage:\n")

if (len(sys.argv) == 1):
    usage()
    exit()

def usage():
    print("Usage:\n")
    
with open('mn_db.json') as magic_numbers_db_json:
    magic_numbers_db = json.load(magic_numbers_db_json) # It is typed string
    magic_numbers = json.loads(magic_numbers_db) # convert str to dict
#
# check if binary
textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
#
#
if is_binary_string(open(sys.argv[1], 'rb').read(1024)):
    with open(sys.argv[1], "rb") as f:
        byte = f.read(4)
        data = binascii.hexlify(byte, ' ').decode('ascii')
        print("Magic number of ", sys.argv[1], " is:")
        try:
            print(data, ": ", magic_numbers[data], "\n")
        except:
            print(data)

            if input("Add this magic number to db.json? (o/n)") == "o":
                description = input("Description: ")
                magic_numbers[data] = description
                print(magic_numbers)
            else:
                exit()

