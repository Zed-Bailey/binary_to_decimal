while True:
    binary = input("Enter binary number to convert to decimal >> ")

    pos = len(binary)
    output = ""
    value = 0
    # option + 8 for •

    for i in binary:
        pos = pos - 1
        output += f"{i}*2^{pos} + "
        value += (int(i) * (2**pos))


    print(output + " = " + str(value))
    # this would be the easier method to convert, use the inbuilt functions: print(int(binary,2))
