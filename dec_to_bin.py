class base_conversions():
    def __init__(self):
        self.hex_values = {
            10: "A",
            11: "B",
            12: "C",
            13: "D",
            14: "E",
            15: "F",
            "F": 15,
            "E": 14,
            "D": 13,
            "C": 12,
            "B": 11,
            "A": 10
            }
        
    def find_highest_bin_value(self, num: int):# Returns [place_value, remainder]
        i = 0
        while num//2**i != 0: # Find the first power of 2 that doesn't go into num
            i += 1
        i -= 1
        remainder = num - 2**i # Get the remainder of number without the highest binart value that goes into it
        place_value = i
        return [place_value, remainder]

    def bin_beautify(self, binstr: str):
        # Adds 0s at the front in order to make the binary string split nicely
        while len(binstr)%4 != 0:
            binstr = "0"+binstr
        # Split the binary string into nibbles to make easier to read for user
        beautified_bin = ""
        for i in range(len(binstr)):
            if i%4 == 0 and i != 0:
                beautified_bin = beautified_bin + " "
            beautified_bin = beautified_bin + binstr[i]
        return beautified_bin
    
    def bin_debeautify(self, binstr: str):
        debeautified_bin = ""
        for i in binstr:
            if i == " ":
                pass
            elif i == "0" and len(debeautified_bin) != 0:
                debeautified_bin = debeautified_bin + i
            elif i == "1":
                debeautified_bin = debeautified_bin + i
        return debeautified_bin
        

    def dec_to_bin(self, n: int):
        if n == 0: # Return 0 if n is 0
            return "0000"
        # Prepares a 2d List in order to convert to binary
        constructor = []
        while n != 0:
            temp = self.find_highest_bin_value(n)
            n = temp[1]
            constructor.append(temp)
        # Creates a list as long as needed for the binar string
        temp = ["0"]*(int(constructor[0][0])+1)
        # Adds in the ones for the binary string
        for i in constructor:
            temp[len(temp)-1-i[0]] = "1"
        temp = "".join(temp) # Converts list to string
        binary = self.bin_beautify(temp)
        return binary
                
    def bin_to_dec(self, binstr: str):
        binstr = self.debeautified_bin(binstr) # Converts binstr from human readable to machine readable
        answer = 0
        for i in range(len(binstr)): # iterates through and multiplies value by correct power of 2 and sums together
            answer += int(binstr[i])*2**(len(binstr)-i-1)
        return answer

    def bin_to_hex(self, binstr: str):
        binstr = binstr.split(" ") # Split the nibbles into a list
        answer = ""
        # Converts each nibble to hex and adds to answer
        for i in binstr:
            temp = self.bin_to_dec(i)
            if temp > 9:
                temp = self.hex_values[temp]
            answer = answer+str(temp)
        return "#"+answer

    def dec_to_hex(self, num: int):
        binnum = self.dec_to_bin(num)
        return "#"+self.bin_to_hex(binnum)

    def hex_to_bin(self, hexcode: str):
        hexcode = hexcode[1:].upper() if "#" in hexcode else hexcode.upper()
        hexcode = list(hexcode)
        binstr = ""
        for i in hexcode:
            temp = ""
            if i.isnumeric():
                temp = self.dec_to_bin(int(i))
            else:
                temp = self.dec_to_bin(self.hex_values[i])
            binstr = binstr + temp
        return self.bin_beautify(binstr)
    

class binaryAddition(base_conversions):
    def __init__(self):
        super().__init__()
        
    def easyWay(self, binstr1, binstr2):
        num1 = self.bin_to_dec(binstr1)
        num2 = self.bin_to_dec(binstr2)
        numtotal = num1 + num2
        return self.dec_to_bin(numtotal)
    
    def properWay(self, binstr1, binstr2):
        print(binstr1,binstr2)
        binstr1, binstr2 = self.bin_debeautify(binstr1), self.bin_debeautify(binstr2)
        print(binstr1,binstr2)
        longest = len(binstr1) if len(binstr1) > len(binstr2) else len(binstr2)
        binstr1 = "0"*(longest-len(binstr1)) + binstr1
        binstr2 = "0"*(longest-len(binstr2)) + binstr2
        print(binstr1,binstr2)
        binsum = ""
        for i in range(longest-1,-1,-1):
            carry = None
            temp = None
            if (binstr1[i] == "1" or binstr2[i] == "1") and (binstr1[i] != binstr2[i]):
                print(1)
                temp = "1"
            elif binstr1[i] == "0" and binstr2[i] == "0":
                print(2)
                temp = "0" 
            else:
                carry = "1" 
                temp = "0"
            if carry == "1" and temp == "1":
                binsum = binsum + "1"
                carry = "1"
            elif carry == "1" and temp == "0":
                binsum = binsum + "1"
            else:
                binsum = binsum + temp
        print(binsum)
        return binsum
                    
        
b = base_conversions()
ba = binaryAddition()

print(ba.properWay("0011","0001"))