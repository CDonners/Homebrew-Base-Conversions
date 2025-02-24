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
        
    def find_highest_bin_value(self, num):# Returns [place_value, remainder]
        i = 0
        while num//2**i != 0: # Find the first power of 2 that doesn't go into num
            i += 1
        i -= 1
        remainder = num - 2**i # Get the remainder of number without the highest binart value that goes into it
        place_value = i
        return [place_value, remainder]

    def bin_beautify(self, binstr):
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
    
    def prep_bin(self, binstr: str): # Removes spaces to be understood by code
        answer = ""
        for i in binstr:
            if i != " ":
                answer = answer + i
        return answer
                
    def bin_to_dec(self, binstr: str):
        binstr = self.prep_bin(binstr) # Converts binstr from human readable to machine readable
        answer = 0
        for i in range(len(binstr)): # iterates through and multiplies value by correct power of 2 and sums together
            answer += int(binstr[i])*2**(len(binstr)-i-1)
        return self.bin_beautify(answer)

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
    
b = base_conversions()
