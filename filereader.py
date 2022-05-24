import sys
import binascii
import json
#
# [X] Add function adding new magic number to db.csv
# [ ] FInd logic to get data to send to addMagic function
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

def isBinary(bytes):
    textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
    return bool(bytes.translate(None, textchars))

def getMagic(magic_number):
    with open('mn_db.csv','r') as file:
        for line in file:
            a = line.split(';')
            if a[0] == magic_number:
                return a[1]
        return "Magic number not in local database."

def addMagic(magic_number, description):
    with open('mn_db.csv','a+') as file:
        data = magic_number + ";" + description
        file.write(data)

####

if (len(sys.argv) == 1):
    usage()
    exit()
#
# Get first 1024 bytes and first 4 bytes
#
with open(sys.argv[1], 'rb') as file:
    oneK = file.read(1024)
    file.seek(0)
    fourB = file.read(4)
#
# Check if file is binary
if isBinary(oneK):
    data = binascii.hexlify(fourB, ' ').decode('ascii')
    print("Magic number of", sys.argv[1], "is:")
    try:
        mn = getMagic(data)
        print(data, ": ", mn, "\n")
        if mn == "Magic number not in local database.":
            if input('Do you want to add this magic number description in local database? (o/n): ') == "o":
                description = input('What is the description? ')
                addMagic(data, description)

    except:
        print("An error occured while attempting to identify this magic number:",data)
else:
	print(sys.argv[1], "is a text file.")
