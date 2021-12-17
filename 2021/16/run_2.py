import os, sys, copy
from collections import Counter
import numpy as np

#filename = "input_test.txt"
filename = "input_final.txt"

with open(filename) as file:
    lines = file.readlines()
    packet = lines[0].strip()

lookup = {
        '0' : '0000', 
        '1' : '0001', 
        '2' : '0010', 
        '3' : '0011', 
        '4' : '0100', 
        '5' : '0101', 
        '6' : '0110', 
        '7' : '0111', 
        '8' : '1000', 
        '9' : '1001', 
        'A' : '1010', 
        'B' : '1011', 
        'C' : '1100', 
        'D' : '1101', 
        'E' : '1110', 
        'F' : '1111', 
        }

def decode(packet):
    final = ""
    for char in packet:
        final += lookup[char]
    return final

#packet = 'C200B40A82'
#packet = '880086C3E88112'
#packet = 'D8005AC2A8F0B'
#packet = 'F600BC2D8F'
#packet = '9C005AC2F8F0'
#packet = '9C0141080250320F1802104A08'
#print(packet)
decoded_packet = decode(packet)
#decoded_packet = "11101110000000001101010000001100100000100011000001100000"
#decoded_packet = "00111000000000000110111101000101001010010001001000000000"
#decoded_packet = "110100101111111000101000"
print("Packet {}, Len {}".format(packet, len(packet)))
print("Decoded Packet {}, Len {}".format(decoded_packet, len(decoded_packet)))

g_version_sum = 0

def readLiteral(packet):
    # Literal value
    lastPacket = False
    final_number = ""
    index = 0
    while lastPacket != True:
        if packet[index:index+1] == '0':
            lastPacket = True
        number = packet[index+1:index+5]
        final_number += str(number)
        index += 5
    return packet[index:], int(final_number,2)

def readPacket(packet, literals):
    print("1 Literals {}".format(literals))
    print("Packet {}".format(packet))
    if packet == "" or all(c in '0' for c in packet):
        print("2 Literals {}".format(literals))
        return "", literals

    pkt_version = int(packet[0:3],2)
    global g_version_sum
    g_version_sum += pkt_version
    pkt_type = int(packet[3:6],2)
    print("Version {}, Type {}".format(pkt_version, pkt_type))
    index = 6

    if pkt_type == 4:
        print("3 Literals {}".format(literals))
        packet, literal = readLiteral(packet[index:])
        literals.append(literal)
        print("4 Literals {}".format(literals))
        return packet, literals
    else:
        print("5 Literals {}".format(literals))
        local_literals = []
        # Operator
        length_type_id = int(packet[index])
        index += 1

        if length_type_id == 1:
            number_of_subpackets = int(packet[index:index + 11], 2)
            index += 11
            #print("number_of_subpackets {} ".format(number_of_subpackets))
            packet = packet[index:]
            for i in range(number_of_subpackets):
                # Pass whole packet as we don't know end
                print("Here 1 {}".format(local_literals))
                packet, local_literals = readPacket(packet, local_literals)
        elif length_type_id == 0:
            bits_in_subpackets = int(packet[index:index + 15], 2)
            index += 15
            #print(packet)
            #print("bits_in_subpackets {} ".format(bits_in_subpackets))
            read_string = packet[index:index + bits_in_subpackets]
            while len(read_string) > 0:
                # Pass fixed number of bits as we don't need whole packet
                print("Here 2 {}".format(local_literals))
                read_string, local_literals = readPacket(read_string, local_literals)
            if read_string != "":
                print('Problem')

            packet = packet[index + bits_in_subpackets:]
        print("6 Literals {}".format(literals))

        answer = 0
        if pkt_type == 0:
            answer += sum(local_literals)
        elif pkt_type == 1:
            answer = 1
            for literal in local_literals:
                answer *= literal
        elif pkt_type == 2:
            answer += min(local_literals)
        elif pkt_type == 3:
            answer += max(local_literals)
        elif pkt_type == 5:
            answer += 1 if local_literals[0] > local_literals[1] else 0
        elif pkt_type == 6:
            answer += 1 if local_literals[0] < local_literals[1] else 0
        elif pkt_type == 7:
            answer += 1 if local_literals[0] == local_literals[1] else 0
        print("7 Literals {}".format(literals))

        print("Answer {}".format(answer))
        literals.append(answer)
        print("8 Literals {}".format(literals))
        return packet, literals

literals2 = []
final_packet, literals2 = readPacket(decoded_packet, literals2)

print(literals2)

#print("Version sum {}".format(g_version_sum))

#1137 too low
