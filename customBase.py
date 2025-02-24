class customBase():
    def __init__(self):
        self.base_values = {}
        self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.base_info = []
    
    def create_custom_base(self, base: int):
        letter_repeat_counts = 0
        for i in range(1,base+1):
            if i < 10:
                self.base_values[i] = str(i)
            else:
                temp = i-10
                letter_repeat_counts = temp//26
                remainder = temp % 26
                self.base_values[i] = self.alphabet[remainder] * (letter_repeat_counts)
        self.base_info = [base, self.base_values]
    
    def dec_to_base(self, num):
        pass
        

c = customBase()
c.create_custom_base(79)