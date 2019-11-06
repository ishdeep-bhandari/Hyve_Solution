in_file = open("input.bin","r")                                 # Input file read
out_file = open("output.bin","w")                               # output file write

input_list = ["{:02x}".format(ord(c)) for c in in_file.read()]  # Retrieve hexadecimal values

USE_TRIVIAL_IMPLEMENTATION = 0

def hex_to_int(inp):                                            # hexadecimal to decimal
    return int(inp, 16)


def decode_encode(in_list,imp):                                 # Decode the list and encode
    result = []
    x = 0
    if imp == 1:                                                # Trivial implementation when pi = 0
        for x in range(0,len(in_list),2):
            if hex_to_int(in_list[x]+in_list[x+1]) == hex_to_int(in_list[x+1]): # Check whether result in decimal
                result.append(in_list[x+1])


    # Does not check for invalid pairs
    else:                                                       # Non-Trivial implementation
        while x < len(in_list):
            if hex_to_int(in_list[x]) == 0:
                if hex_to_int(in_list[x]+in_list[x+1]) == hex_to_int(in_list[x+1]):
                    result.append(in_list[x + 1])
                    x = x + 2

            elif hex_to_int(in_list[x]) > 0 and hex_to_int(in_list[x+1]) > 0:  # Check if p and q are greater than 0
                for y in range((len(result) - (hex_to_int(in_list[x]))),
                               (len(result) - hex_to_int(in_list[x])) + hex_to_int(in_list[x + 1])): # add the value after q positions from p
                    result.append(result[y])
                x = x + 2
            elif x == len(in_list) - 1:  # if the list is odd number i.e. last input is incomplete
                result.append("3f")

    return result


output = decode_encode(input_list,USE_TRIVIAL_IMPLEMENTATION)        # Call the encoding function

in_file.close()                                                     # Close input file

for i in output:                                                    # Write the encoded file as output
    out_file.write(i)
    out_file.write(" ")

out_file.close()                                                    # Close output File






