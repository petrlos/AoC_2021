#Advent of Code 2021: Day 16

#TODO: not working at all, dont know how yet

def decodeLiteralValue(binaryData):
    decoded = ""
    for index in range(0,len(binaryData), 5):
        decoded += binaryData[index + 1:index + 5]
        if binaryData[index] == "0":
            break
    return int(decoded, 2)

def decodeOperatorPacket(binaryData):
    subPacketLength = 0
    subPacketCount = 0
    if binaryData[0] == "0":
        subPacketLength = int(binaryData[1:16], 2)
    else:
        subPacketCount = int(binaryData[1:12], 2)

    print(subPacketLength, subPacketCount)

def encodePacket(binaryData):
    packetType = int(binaryData[0:3], 2)
    packetID = int(binaryData[3:6], 2)
    if packetID == 4:
        value = decodeLiteralValue(binaryData[6:])
        print(value)
    else:
        value = decodeOperatorPacket(binaryData[6:])


#MAIN
#generate hex -> bin dictionary
with open("bindict.txt") as file:
    lines = file.read().splitlines()
    binDict = {}
    for line in lines:
        key, value = line.split(" = ")
        binDict[key] = value

hexString = "EE00D40C823060"

binaryData = ""
for char in hexString:
    binaryData += binDict[char]

encodePacket(binaryData)