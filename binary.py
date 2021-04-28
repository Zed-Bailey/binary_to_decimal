

def main():

    while True:
        make_table()


def make_table():
    binary = []
    num = input("enter decimal number to convert to decimal to binary table >> ")
    quotient = 0
    num = int(num) 
    # display  header
    print("value\t| quotient\t| remainder")

    if num % 2 == 0:
        binary.insert(0,0)
        quotient = int(num / 2)
        print(f'{num}/2\t| {quotient}\t\t| 0')

    else:
        quotient  = int(num / 2)
        binary.insert(0,1)
        print(f'{num}/2\t | {quotient}\t\t| 1')

    while True:
        if (quotient % 2) == 0:
            binary.insert(0,0)
            q = int(quotient / 2)
            print(f'{quotient}/2\t| {q}\t\t| 0')
            quotient = q
        else:
            q = int(quotient / 2)
            binary.insert(0,1)
            print(f'{quotient}/2\t| {q}\t\t| 1')
            quotient = q
        if quotient == 0:
            break
   
   # insert an extra 0 to pad the binary to 8 bits like we want
    if len(binary) != 8:
        padding = 8 - len(binary)
        #print("add a '0' to the front to bad it to 8 bits!")
        for i in range(0,padding):
            binary.insert(0,0)
            print(f'0/2\t| 0\t\t| 0')
        
        print("pad with 0's to make 8 bits")

    binary = ''.join(map(str, binary))
    print(f'{num} in binary = {binary}')

    


if __name__ == '__main__':
    main()
