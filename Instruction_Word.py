class Instruction_Word:
    def __init__(self) -> None:
        self.op = {
            'addi': self.pad(6,'0'),

        }
        self.register_op = ['add','sgt','slt','and','or']
        self.immediate=['addi','beq']
        self.memory=['sw','lw']
        self.reg = {'$'+i:self.int2bs(i,3) for i in [str(j) for j in range(8)]}
    
    def compile(self,instruction):
        # instructions are only space separated {add, }
        instructions = [i.strip().lower() for i in instruction.split(' ')]
        op_code = self.op[instructions[0]]
        dest = self.int2bs(instructions[1][1:],3)

        if op_code.isin(self.register_op):
            src1=self.reg[instructions[2]]
            src2=self.reg[instructions[3]]
            return self.pad_end(27,op_code+dest+src1+src2)

        elif op_code.isin(self.immediate):
            src1=self.reg[instructions[2]]
            imm = self.int2bs(instructions[3],16)
            return op_code+dest+src1+imm
        elif op_code.isin(self.memory):
            pass
        # machine_op = self.op[instruction[:5]]
        return instructions


    def pad(self,size, strin):
        """ Pads a string with leading zeros to produce a string with desirable length"""
        pad_amt = size-len(strin)
        return ("0"*(pad_amt) + strin)
    
    def pad_end(self,size, strin):
        """ Pads a string with ending zeros to produce a string with desirable length"""
        pad_amt = size-len(strin)
        return (strin+"0"*(pad_amt))

    def int2bs(self, s, n):
        """ Converts an integer string to a 2s complement binary string.

            Args: s = Integer string to convert.to 2s complement binary.
                n = Length of outputted binary string.
            
            Example Input: stpd("4", 4)
            Example Output: "0100"

            Example Input: stpd("-3", 16)
            Example Output: "1111111111111101" """
    
        x = int(s)                              # Convert string to integer, store in x.
        if x >= 0:                              # If not negative, use python's binary converter and strip the "0b"
            ret = str(bin(x))[2:]
            return self.pad(n,ret)     # Pad with 0s to length.
        else:
            ret = 2**n - abs(x)                 # If negative, convert to 2s complement integer
            return bin(ret)[2:]                 # Convert to binary using python's binary converter and strip the "0b"
        
    def bs2hex(self,v):
        """ Converts a binary string into hex.

            Args: v = Binary string to convert to hex

            Example Input: bs2hex("1010000010001111") 
            Example Output: "a08f" """
        return(hex(int(v,2))[2:])
    

if __name__ == "__main__":
    i = Instruction_Word()
    print (i.int2bs('2',5))
    print (i.int2bs('-1',8))
    print (i.bs2hex(i.int2bs('-1',8)))
    print (i.pad(2,i.bs2hex(i.int2bs('2',8))))
    print (i.compile("addi $1 $0 1"))
    print (i.reg)


