"""
First question asks user for a number and converts it to binary and hex in 32 bits.
If the number is negative the binary displayed is in two's complement.
"""
def questionOne():
    integer = int(input("Enter a positive or negative number in base 10: "))
    binaryList = []
    num = integer

    #Keeps dividing number by 2 to get the remainder for the binary number
    if integer > 0:
        while integer >= 1:
            difference = str(integer%2)
            integer = integer//2
            binaryList.insert(0,difference) #Adds 1 or 0 to the binary
    elif integer == 0: #Returns 0 if entered number is 0
        binaryList = ['0']
    else: #Makes a negative number positive first
        integer = integer *-1
        while integer >= 1:
            difference = str(integer%2)
            integer = integer//2
            binaryList.insert(0,difference)

    #Pads number with zeroes if not already 32 bits
    while len(binaryList)!=32:
        binaryList.insert(0,'0')
    #Two's complement if number is negative
    if num < 0:
        i = 0
        #Flips bits
        for x in binaryList:
            if x == '0':
                binaryList[i] = '1'
            else:
                binaryList[i] = '0'
            i+=1
        y = 1
        #Adds 1
        while y < 32:
            if binaryList[32-y]=='0':
                binaryList[32-y]='1'
                break
            else:
                binaryList[32-y]='0'
            y+=1
    binary = ''.join(binaryList) #Makes everything in the binary list into a string
    print("Binary:", binary)
    digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hexNum = ''
    num = []
    r = 0
    #Breaks up binary into four bits
    while r<4:
        num.append(binaryList[r])
        r+=1
    digit = 0
    i = 3
    #Iterates through the four bits
    for x in num:
        if x =='1':
            digit+=pow(2,i) #takes 2 to the power of the index of the number
        i-=1
    hexNum+=digits[digit] #Finds the character in the list using the index and adds it to the hex
    num = []
    r = 4
    #Repeats the above for all 8 groups of 4 bits
    while r<8:
        num.append(binaryList[r])
        r+=1
    digit = 0
    i = 3
    for x in num:
        if x =='1':
            digit+=pow(2,i)
        i-=1
    hexNum+=digits[digit]
    num = []
    r = 8
    while r<12:
        num.append(binaryList[r])
        r+=1
    digit = 0
    i = 3
    for x in num:
        if x =='1':
            digit+=pow(2,i)
        i-=1
    hexNum+=digits[digit]
    num = []
    r = 12
    while r<16:
        num.append(binaryList[r])
        r+=1
    digit = 0
    i = 3
    for x in num:
        if x =='1':
            digit+=pow(2,i)
        i-=1
    hexNum+=digits[digit]
    num = []
    r = 16
    while r<20:
        num.append(binaryList[r])
        r+=1
    digit = 0
    i = 3
    for x in num:
        if x =='1':
            digit+=pow(2,i)
        i-=1
    hexNum+=digits[digit]
    num = []
    r = 20
    while r<24:
        num.append(binaryList[r])
        r+=1
    digit = 0
    i = 3
    for x in num:
        if x =='1':
            digit+=pow(2,i)
        i-=1
    hexNum+=digits[digit]
    num = []
    r = 24
    while r<28:
        num.append(binaryList[r])
        r+=1
    digit = 0
    i = 3
    for x in num:
        if x =='1':
            digit+=pow(2,i)
        i-=1
    hexNum+=digits[digit]
    num = []
    r = 28
    while r<32:
        num.append(binaryList[r])
        r+=1
    digit = 0
    i = 3
    for x in num:
        if x =='1':
            digit+=pow(2,i)
        i-=1
    hexNum+=digits[digit]
    print("Hexadecimal:",hexNum,sep='')
questionOne()

"""
Takes a hex number and returns it as a decimal.
Iterates through each character of the hex, finds its value based on the digits list and then uses a power function to find the total.
"""
def questionTwo():
    digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hexa = str(input("Enter a hexadecimal number: "))
    hexList = list(hexa) #Make input into a list
    num = 0
    i = len(hexList)-1
    #Iterates through each value of the entered number
    for x in hexList:
        num+=(digits.index(x))*pow(16,i) #Uses base 16 and index of character to calculate value
        i-=1
    print("Decimal:",num)
questionTwo()
