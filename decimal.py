



while True:
    binary = input("Enter binary number to convert to decimal >> ")

    pos = len(binary)
    output = ""
    value = 0
    # option + 8 for •
    
    for i in binary:
        output += f"{i}*2^{pos} + "
        value += int(i) * 2^pos
        pos = pos - 1

    print(output + " = " + str(value))
        
