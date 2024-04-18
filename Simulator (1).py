import sys
# with open("testcase.txt", 'r') as f:
f = open(sys.argv[1],'r')
lines = f.readlines()
f.close()
# print(lines)
register = {
    "zero": "00000",
    "ra": "00001",
    "sp": "00010",
    "gp": "00011",
    "tp": "00100",
    "t0": "00101",
    "t1": "00110",
    "t2": "00111",
    "s0": "01000",
    "s1": "01001",
    "a0": "01010",
    "a1": "01011",
    "a2": "01100",
    "a3": "01101",
    "a4": "01110",
    "a5": "01111",
    "a6": "10000",
    "a7": "10001",
    "s2": "10010",
    "s3": "10011",
    "s4": "10100",
    "s5": "10101",
    "s6": "10110",
    "s7": "10111",
    "s8": "11000",
    "s9": "11001",
    "s10": "11010",
    "s11": "11011",
    "t3": "11100",
    "t4": "11101",
    "t5": "11110",
    "t6": "11111"
}


reg_val = { 
    "zero": 0b00000000000000000000000000000000,
    "ra": 0b00000000000000000000000000000000,
    "sp": 0b00000000000000000000000100000000,
    "gp": 0b00000000000000000000000000000000,
    "tp": 0b00000000000000000000000000000000,
    "t0": 0b00000000000000000000000000000000,
    "t1": 0b00000000000000000000000000000000,
    "t2": 0b00000000000000000000000000000000,
    "s0": 0b00000000000000000000000000000000,
    "s1": 0b00000000000000000000000000000000,
    "a0": 0b00000000000000000000000000000000,
    "a1": 0b00000000000000000000000000000000,
    "a2": 0b00000000000000000000000000000000,
    "a3": 0b00000000000000000000000000000000,
    "a4": 0b00000000000000000000000000000000,
    "a5": 0b00000000000000000000000000000000,
    "a6": 0b00000000000000000000000000000000,
    "a7": 0b00000000000000000000000000000000,
    "s2": 0b00000000000000000000000000000000,
    "s3": 0b00000000000000000000000000000000,
    "s4": 0b00000000000000000000000000000000,
    "s5": 0b00000000000000000000000000000000,
    "s6": 0b00000000000000000000000000000000,
    "s7": 0b00000000000000000000000000000000,
    "s8": 0b00000000000000000000000000000000,
    "s9": 0b00000000000000000000000000000000,
    "s10": 0b00000000000000000000000000000000,
    "s11": 0b00000000000000000000000000000000,
    "t3": 0b00000000000000000000000000000000,
    "t4": 0b00000000000000000000000000000000,
    "t5": 0b00000000000000000000000000000000,
    "t6": 0b00000000000000000000000000000000
}


memory = { 
    "0x00010000" : 0b00000000000000000000000000000000,
    "0x00010004": 0b00000000000000000000000000000000,
    "0x00010008": 0b00000000000000000000000000000000,
    "0x0001000c": 0b00000000000000000000000000000000,
    "0x00010010": 0b00000000000000000000000000000000,
    "0x00010014": 0b00000000000000000000000000000000,
    "0x00010018": 0b00000000000000000000000000000000,
    "0x0001001c": 0b00000000000000000000000000000000,
    "0x00010020": 0b00000000000000000000000000000000,
    "0x00010024": 0b00000000000000000000000000000000,
    "0x00010028": 0b00000000000000000000000000000000,
    "0x0001002c": 0b00000000000000000000000000000000,
    "0x00010030": 0b00000000000000000000000000000000,
    "0x00010034": 0b00000000000000000000000000000000,
    "0x00010038": 0b00000000000000000000000000000000,
    "0x0001003c": 0b00000000000000000000000000000000,
    "0x00010040": 0b00000000000000000000000000000000,
    "0x00010044": 0b00000000000000000000000000000000,
    "0x00010048": 0b00000000000000000000000000000000,
    "0x0001004c": 0b00000000000000000000000000000000,
    "0x00010050": 0b00000000000000000000000000000000,
    "0x00010054": 0b00000000000000000000000000000000,
    "0x00010058": 0b00000000000000000000000000000000,
    "0x0001005c": 0b00000000000000000000000000000000,
    "0x00010060": 0b00000000000000000000000000000000,
    "0x00010064": 0b00000000000000000000000000000000,
    "0x00010068": 0b00000000000000000000000000000000,
    "0x0001006c": 0b00000000000000000000000000000000,
    "0x00010070": 0b00000000000000000000000000000000,
    "0x00010074": 0b00000000000000000000000000000000,
    "0x00010078": 0b00000000000000000000000000000000,
    "0x0001007c": 0b00000000000000000000000000000000
}


def sign_ext(imm):
    print(imm)
    sign_bit = int(imm[0])

    if sign_bit == 1:
        imm = bin(int('111111111111', 2) << 12 | int(imm, 2))[2:]
        return imm
    else:
        # Positive value, fill with 0s
        imm = bin(int('000000000000', 2) << 12 | int(imm, 2))[2:]
        return imm 

def bin_to_int(imm):
    # Check the sign bit
    sign_bit = imm[0]
    
    # If the sign bit is 0, it's a positive number
    if sign_bit == '0':
        return int(imm, 2)
    # If the sign bit is 1, it's a negative number
    else:
        # Convert the two's complement to integer
        return -int(''.join('1' if bit == '0' else '0' for bit in imm), 2) - 1


def int_to_bin(immi):
    # Check if the integer is negative
    # print("add")
    if immi < 0:
        # Convert the negative integer to its two's complement
        imm = bin((1 << 32) + immi)[2:]
    else:
        # Convert the positive integer to binary
        imm = bin(immi)[2:]

    # Ensure the binary string is exactly 32 bits long by adding leading zeros if necessary
    imm = '0' * (32 - len(imm)) + imm

    return imm

def signed_to_int(binary_str):

    is_negative = binary_str[0] == '1'
    
    integer_value = int(binary_str[1:], 2)

    if is_negative:
        integer_value = -integer_value

    return integer_value

def int_to_twocomp(integer, bit_width):
    if integer >= 0:
        # Convert positive integer to binary representation
        binary_str = bin(integer)[2:].zfill(bit_width)
    else:
        # Convert negative integer to binary representation
        binary_str = bin(2**bit_width + integer)[2:]

    return binary_str
def twos_complement(binary_str):
    # Check if the number is negative
    if binary_str[0] == '1':
        # Perform two's complement by flipping the bits and adding 1
        inverted = ''.join('1' if bit == '0' else '0' for bit in binary_str)
        return -(int(inverted, 2) + 1)
    else:
        return int(binary_str, 2)
    
def make_lsb_zero(pc):
    modified_pc = pc[:-1] + '0'
    return modified_pc

# last_line = lines[-1].strip()
#R type
outfile = open(sys.argv[2],"w")
def R_type(last_line,PC):
    if last_line[-7:]=="0110011":
        func3=last_line[-15:-12]
        func7=last_line[-32:-25]
        rd0 = last_line[-12 :-7]
        rs1_0 = last_line[-20 :-15]
        rs2_0 = last_line[-25 :-20]
        #print(rd0, 'rd')
        # print(rs1_0, 'rs1')
        # print(rs2_0, 'rs2')
        # print(func3)
        #print(func7)

        for i in register:
            if rd0 == register[i]:
                temp1=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp1:
                        rd=int_to_bin(reg_value)
        # print(format(rd, '032b'))

        for i in register:
            if rs1_0 == register[i]:
                temp2=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp2:
                        rs1=int_to_bin(reg_value)
        # print(format(rs1, '032b'))

        for i in register:
            if rs2_0 == register[i]:
                temp3=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp3:
                        rs2=int_to_bin(reg_value)
        # print(format(rs2, '032b'))

        print(rs1)
        print(rs2)
        if func3=="000": #add or sub
            if func7=="0000000":
                #add
                rd=twos_complement(rs1)+twos_complement(rs2)
                rd=int(int_to_bin(rd),2)
                print("add")
                reg_val[temp1]=rd
                # values_list = list(reg_val.values())
                # print(values_list)
                t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
                # t = ' '.join('0b' + str(value).zfill(32) for value in reg_val.values())
                # print(t)
                # print('PC', PC)
                outfile.write('0b'+PC)
                outfile.write(" ")
                outfile.write(t)
                outfile.write(" ")
                outfile.write('\n')

            if func7=="0100000":
                if rs1_0=="00000":
                    #sub(twos comp)
                    # subtract (two's complement)
                    # rs2_twos_complement = (~rs2 + 1) & 0xFFFFFFFF
                    # rd = rs1 + rs2_twos_complement
                    rd= -(int(rs2,2))
                    print("sub")
                    rd=int(int_to_bin(rd),2)
                    # print(rd,'rd')
                    # values_list = list(reg_val.values())
                    # print(values_list)

                    reg_val[temp1]=rd
                    # t = ' '.join(format(value, '032b') for value in reg_val.values())
                    t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
                    # print(t)
                    # print(format(rd, '032b'))
                    outfile.write('0b'+PC)
                    outfile.write(" ")
                    outfile.write(t)
                    outfile.write(" ")
                    outfile.write('\n')

                else:
                    # sub(signed) 
                    print("subsigned")
                    rs2= signed_to_int(rs2)
                    rs2= int_to_twocomp(rs2, 32)
                    # rs2= int_to_twocomp(rs2,32)
                    rs1= signed_to_int(rs1)
                    # rs1= int(rs1)
                    # rs2= int(rs2)
                    # print(rs1, 'rs1')
                    # print(twos_complement(rs2), 'rs2')
                    # print(twos_complement(rs2), 'bin')
                    rd= rs1 - twos_complement(rs2) 
                    # rd= int_to_bin(rd)
                    reg_val[temp1]=rd
                    # print(rd,'j')
                    # values_list = list(reg_val.values())
                    # print(values_list)
                    t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
                    # print(t)
                    outfile.write('0b'+PC)
                    outfile.write(" ")
                    outfile.write(t)
                    outfile.write(" ")
                    outfile.write('\n')


        if func3=="001":
            #sll
            print("sll")
            rd=int(rs1,2)<<int(rs2,2)
            rd=int(int_to_bin(rd),2)
            reg_val[temp1]=rd
            values_list = list(reg_val.values())
            # print(values_list)
            # t=' '.join(format(value,'032b') for value in reg_val.values())
            t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
            # print(t)
            outfile.write('0b'+PC)
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')


        if func3=="010":
            #slt
            print("slt")
            print(rs1)
            if sign_ext(rs1)<sign_ext(rs2):
                rd=0b00000000000000000000000000000001
                reg_val[temp1]=rd
                # print(format(rd, '032b'))
                t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
                # print(t)
                outfile.write('0b'+PC)
                outfile.write(" ")
                outfile.write(t)
                outfile.write(" ")
                outfile.write('\n')

            else:
                rd=0b00000000000000000000000000000000
                reg_val[temp1]=rd
                t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
                # print(t)
                # print(format(rd, '032b'))
                outfile.write('0b'+PC)
                outfile.write(" ")
                outfile.write(t)
                outfile.write(" ")
                outfile.write('\n')



        if func3=="011":
            #sltu
            if int(rs1,2)<int(rs2,2):
                rd=0b00000000000000000000000000000001
                reg_val[temp1]=rd
                # print(format(rd, '032b'))
                t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
                # print(t)
                outfile.write('0b'+PC)
                outfile.write(" ")
                outfile.write(t)
                outfile.write(" ")
                outfile.write('\n')
            else:
                rd=0b00000000000000000000000000000000
                reg_val[temp1]=rd
                t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
                # print(t)
                # print(format(rd, '032b'))
                outfile.write('0b'+PC)
                outfile.write(" ")
                outfile.write(t)
                outfile.write(" ")
                outfile.write('\n')



        if func3=="100":
            #xor
            rd=int(rs1,2)^int(rs2,2)
            rd=int(int_to_bin(rd),2)
            reg_val[temp1]=rd
            values_list = list(reg_val.values())
            # print(values_list)
            # t=' '.join(format(value,'032b') for value in reg_val.values())
            t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
            # print(t)
            outfile.write('0b'+PC)
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')


        if func3=="101":
            #srl
            rd=int(rs1,2)>>int(rs2,2)
            rd=int(int_to_bin(rd),2)
            reg_val[temp1]=rd
            values_list = list(reg_val.values())
            # print(values_list)
            # t=' '.join(format(value,'032b') for value in reg_val.values())
            t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
            # print(t)
            outfile.write('0b'+PC)
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')


        if func3=="110":
            #or
            rd=int(rs1,2)|int(rs2,2)
            rd=int(int_to_bin(rd),2)
            reg_val[temp1]=rd
            # values_list = list(reg_val.values())
            # print(values_list)
            # t=' '.join(format(value,'032b') for value in reg_val.values())
            t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
            # print(t)
            outfile.write('0b'+PC)
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')

        if func3=="111":
            #and
            rd=int(rs1,2)&int(rs2,2)
            rd=int(int_to_bin(rd),2)
            reg_val[temp1]=rd
            values_list = list(reg_val.values())
            # print(values_list)
            # t=' '.join(format(value,'032b') for value in reg_val.values())
            t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
            # print(t)
            outfile.write('0b'+PC)
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')



# def store_mem(imm):
#     global memory, count
#     if 'count' not in globals():
#         count = 0
#     address = list(memory.keys())[count]  # Get the address at the count index
#     memory[address] = int_to_bin(imm)
    
#     # return address 
#     temp = address
#     count+=1 
#     return temp

#I_type
def I_type(last_line,PC):
        func3=last_line[-15:-12]
        rd0 = last_line[-12 :-7]
        rs1_0 = last_line[-20 :-15]
        imm= last_line[-32:-20]
        opcode= last_line[-7:]
        # print(opcode)

        for i in register:
            if rd0 == register[i]:
                temp1=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp1:
                        rd=format(reg_value, '032b')
        # print(rd, 'rd')

        for i in register:
            if rs1_0 == register[i]:
                temp2=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp2:
                        rs1=format(reg_value, '032b')
        # print(rs1, "j")
        

        if opcode=="0000011":
            # Lw
            # print("hi")
            mem_index = ('0x'+ format(((twos_complement(rs1)) + twos_complement(imm)), '08x'))
            # print(mem_index, 'm')
            for key, value in memory.items():
                if key == mem_index:
                    temp_val = value
            rd=temp_val
            print(rd , "HEERRREEEE")
            # rd=twos_complement(rd)
            # print(rd, 'rd')
            reg_val[temp1]=rd

            t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
            # t = ' '.join('0b{:032}'.format(value) for value in reg_val.values())
            # m = '\n'.join('0b'+format(value,'032b') for value in memory.values())
            # print (t)
            outfile.write('0b'+PC)
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')
            # outfile.write(m)
            # return PC

        if opcode=="0010011" and func3=="000":
            #Addi
            print("Addi")
            print(imm, 'imm')
            # print('hi')
            print(twos_complement(rs1),twos_complement(imm) , "SEE HBERE")
            rd = twos_complement(rs1) + twos_complement(imm)
            print(rd, 'rd')

            # result &= 0xFFFFFFFF 
            # rd = format(result, '032b')
            # rd=twos_complement(rd)
            # print(rd)
            reg_val[temp1]=rd
            # a=-4
            # print("hi")
            t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
            # t = ' '.join('0b{:032}'.format(value) for value in reg_val.values())
            # m = '\n'.join('0b'+format(value,'032b') for value in memory.values())
            # print(t)
            outfile.write('0b'+PC)
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')
            # outfile.write(m)
            # return PC

        if opcode=="0010011" and func3=="011":
            #sltiu
            if int(rs1,2)< int(imm, 2):
                rd=1
            else:
                rd=0
            reg_val[temp1]=rd
            t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
            # print (t, "t")
            # m = '\n'.join('0b'+format(value,'032b') for value in memory.values())
            outfile.write('0b'+PC)
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')
            
            # outfile.write(m)
            

        # if opcode=="1100111":
        # #     #jalr
        #     # new_PC = twos_complement(rs1)+ int(imm,2)
        #     # new_PC = format(new_PC ,'032b')
        #     # new_PC =new_PC[:-1]+'0' # sset LSb to 0
        #     # PC= new_PC
        #     # let_x =int(PC,2)+4
        #     # rd = format(let_x, '032b') # rd ko update kiya 
        #     # reg_val[temp1] =rd
        #     # print(rd)
        #     temp= PC
        #     rd= (int(PC,2))+4
        #     # print(rd)
        #     reg_val[temp1]=rd
        #     # Pc=t1+imm
        #     for reg_name, reg_value in reg_val.items():
        #             if reg_name=="t1":
        #                 t1=format(reg_value, '032b')
        #     PC= (twos_complement(t1)+  twos_complement(imm)) #(acc to project, pc=pc+4)
        #     # PC=PC//4
            
        #     t = ' '.join('0b' + format(value,'032b') for value in reg_val.values())
        #     # m = '\n'.join('0b{:032}'.format(value) for value in memory.values())
        #     outfile.write('0b'+temp)
        #     outfile.write(" ")
        #     outfile.write(t)
        #     outfile.write('\n')
        #     print(PC, 'pc')
        #     return PC
        #     # outfile.write(m)
        #     # outfile.write('\n')
            
            
def I_type_jalr(last_line,PC):
        func3=last_line[-15:-12]
        rd0 = last_line[-12 :-7]
        rs1_0 = last_line[-20 :-15]
        imm= last_line[-32:-20]
        opcode= last_line[-7:]
        # print(opcode)

        for i in register:
            if rd0 == register[i]:
                temp1=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp1:
                        rd=format(reg_value, '032b')
        # print(format(rd, '032b'))

        for i in register:
            if rs1_0 == register[i]:
                temp2=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp2:
                        rs1=format(reg_value, '032b')
        
        
        if opcode=="1100111":
            # print(2)
        #     #jalr
            # new_PC = twos_complement(rs1)+ int(imm,2)
            # new_PC = format(new_PC ,'032b')
            # new_PC =new_PC[:-1]+'0' # sset LSb to 0
            # PC= new_PC
            # let_x =int(PC,2)+4
            # rd = format(let_x, '032b') # rd ko update kiya 
            # reg_val[temp1] =rd
            # print(rd)
            print("jalr")
            rd= twos_complement(PC)+4
            # print(rd)
            reg_val[temp1]=rd
            # Pc=t1+imm
            # if PC[-1] != '0':
            #     PC= make_lsb_zero(PC)
            # for reg_name, reg_value in reg_val.items():
            #         if reg_name=="t1":
            #             t1=format(reg_value, '032b')
            print(twos_complement(rs1),twos_complement(imm), "jalr")
            PC= (twos_complement(rs1)+  twos_complement(imm)) #(acc to project, pc=pc+4)
            # PC=PC//4
            reg_val["zero"] = 0
            PC= int_to_bin(PC)
            if PC[-1] != '0':
                PC= make_lsb_zero(PC)
            t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
            # m = '\n'.join('0b{:032}'.format(value) for value in memory.values())
            outfile.write('0b'+PC)
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')
            # print(PC, 'pc')
            return PC
            # outfile.write(m)
            # outfile.write('\n')
            


def S_type(last_line, PC): #sw
    if last_line[-7:]=="0100011":
        func3=last_line[-15:-12]
        imm_0 = last_line[-12 :-7]
        rs1_0 = last_line[-20 :-15]
        rs2_0 = last_line[-25 :-20]
        imm_1 = last_line[-32:-25]
        imm= imm_1+imm_0


        for i in register:
            if rs1_0 == register[i]:
                temp2=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp2:
                        rs1=format(reg_value, '032b')

        for i in register:
            if rs2_0 == register[i]:
                temp3=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp3:
                        rs2=format(reg_value, '032b')

        mem_index = ('0x'+ format(((twos_complement(rs1)) + twos_complement(imm)), '08x'))
        print(mem_index)
        rs2=twos_complement(rs2)
        for key, value in memory.items():
                if key == mem_index:
                    memory[key]=rs2
        t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
        # m = '\n'.join('0b{:032}'.format(value) for value in memory.values())
        outfile.write('0b'+PC)
        outfile.write(" ")
        outfile.write(t)
        outfile.write(" ")
        outfile.write('\n')
        # outfile.write(m)
        


        # print(rs2)
        # print(rd)
        # reg_val[temp1]=rd




    # Open the output file for writing
    # Write the lines to the output file
# temp = ""
# B type instruction
def B_type(last_line,PC,isb):
    if last_line[-7:]=="1100011":
        func3=last_line[-15:-12]
        imm1 =last_line[-12:-8]
        imm2= last_line[-31:-25]
        imm3=last_line[-8]
        imm4=last_line[-32]
        imm5=imm3+imm2+imm1
        # print(imm5, 'i')
        # print(last_line[-32], 'j')
        # print("imm",imm)
        imm=imm5+'0'
        print(imm, "imm")
        # print(imm, 'i')
        rs1_0 = last_line[-20 :-15]
        rs2_0 = last_line[-25 :-20]


        for i in register:
            if rs1_0 == register[i]:
                temp2=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp2:
                        rs1=format(reg_value, '032b')

        for i in register:
            if rs2_0 == register[i]:
                temp3=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp3:
                        rs2=format(reg_value, '032b')
                        
        if func3=="000": #beq
            print("hello ridhi")
            # temp= PC
            print(PC, 'PC')
            print(twos_complement(rs1),twos_complement(rs2))
            if twos_complement(rs1)==twos_complement(rs2) and twos_complement(imm)!=0:
                # isb= True
                PC = twos_complement(PC) + twos_complement(imm)
                print ("imm 1 : ",imm)
                # PC= int_to_bin(PC)
                print("pc is  : ",PC)
            # else:
            # PC = twos_complement(PC)+4
            # print(PC)
            t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
            # print(t)
            # values_list = list(reg_val.values()) 
            # print(values_list)
            outfile.write(('0b'+PC))
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')
            return PC
        
        if func3=="001": #bne
            print("hello suhana")
            temp= PC
            print(PC, 'PC')
            print(twos_complement(rs1),twos_complement(rs2))
            print(twos_complement(rs1), "rs1")
            print(twos_complement(rs2), "rs2")
            print(twos_complement(imm), "imm")
            if twos_complement(rs1)!=twos_complement(rs2):
                 if twos_complement(imm)!=0:
                    # isb=True
                    isb[0]="True"
                    print(PC,"pc right now")
                    PC = int_to_bin(twos_complement(PC) + twos_complement(imm)-4)
                    print("Hiiiee")
                    print ("imm 1 : ",imm)
                    # PC= int_to_bin(PC))
                    print(PC, "normal pc")
                    # print("pc is  : ",int_to_bin(PC))
                
            t = ' '.join('0b'+format(value if value >= 0 else (1 << 31) + value,'032b') for value in reg_val.values())
            # print(t)
            # values_list = list(reg_val.values()) 
            # print(values_list)
            print(PC, "hi")
            # tempo = (PC)
            # print (tempo , " tempo ") 

            # print(int_to_bin(PC), "heree")
            # outfile.write(" ")j
            outfile.write(('0b'+ PC))
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')
            print(PC , "YOOOOOOOOOOOOOOOOOOOOOOOOO")
            return PC
        
        if func3=="100": #blt
            # print("hello")
            temp= PC
            print(PC, 'PC')
            print(twos_complement(rs1),twos_complement(rs2))
            if twos_complement(rs1)<twos_complement(rs2) and twos_complement(imm)!=0:
                # isb=True
                PC = twos_complement(PC) + twos_complement(imm)
                print ("imm 1 : ",imm)
                # PC= int_to_bin(PC)
                print("pc is  : ",PC)
                
            t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
            # print(t)
            # values_list = list(reg_val.values()) 
            # print(values_list)
            outfile.write(('0b'+int_to_bin(PC)))
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')
            return PC
        
        if func3=="101": #bge
            # print("hello")
            temp= PC
            print(PC, 'PC')
            if twos_complement(rs1)>=twos_complement(rs2) and twos_complement(imm)!=0:
                # isb=True
                print("bge over here")
                PC = twos_complement(PC) + twos_complement(imm)
                print ("imm 1 : ",imm)
                # PC= int_to_bin(PC)
                print("pc is  : ",PC)
                
            t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
            # print(t)
            # values_list = list(reg_val.values()) 
            # print(values_list)
            outfile.write(('0b'+int_to_bin(PC)))
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')
            return PC
        
        if func3=="111":# bgeu
            # print("hello")
            temp= PC
            print(PC, 'PC')
            if int(rs1)!=int(rs2) and twos_complement(imm)!=0:
                # isb=True
                PC = twos_complement(PC) + signed_to_int(imm)
                print ("imm 1 : ",imm)
                # PC= int_to_bin(PC)
                print("pc is  : ",PC)
                
            t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
            # print(t)
            # values_list = list(reg_val.values()) 
            # print(values_list)
            outfile.write(('0b'+int_to_bin(PC)))
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')
            return PC
        
        if func3=="110":# bltu
            # print("hello")
            temp= PC
            print(PC, 'PC')
            if int(rs1)<int(rs2) and twos_complement(imm)!=0:
                # isb=True
                print("hieee")
                PC = twos_complement(PC) + twos_complement(imm)
                print ("imm 1 : ",imm)
                # PC= int_to_bin(PC)
                print("pc is  : ",PC)
                
            t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
            # print(t)
            # values_list = list(reg_val.values()) 
            # print(values_list)
            outfile.write(('0b'+int_to_bin(PC)))
            outfile.write(" ")
            outfile.write(t)
            outfile.write(" ")
            outfile.write('\n')
            return PC
        
            
        
def U_type(last_line,PC):
    if last_line[-7:]=="0110111": #lui
        print("LUI")
        imm_0 = last_line[-20 :-12]
        rd0 = last_line[-12 :-7]
        imm=imm_0+"000000000000"
        print(imm, 'IMM')


        for i in register:
            if rd0 == register[i]:
                temp1=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp1:
                        rd=format(reg_value, '032b')
        rd=twos_complement(imm)
        print(PC,"pc")
        print(int_to_bin(rd))
        reg_val[temp1]=rd   
        values_list = list(reg_val.values())
        t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
        # m = '\n'.join('0b{:032}'.format(value) for value in memory.values())
        outfile.write('0b'+PC)
        outfile.write(" ")
        outfile.write(t)
        outfile.write(" ")
        outfile.write('\n')
     
        
    #if last_line[-7:]=="0010111":
     #   imm_0 = last_line[-32 :-12]
      #  rd0 = last_line[-20 :-15]
       # imm=imm_0+"000000000000"  
    if last_line[-7:]=="0010111": #auipc
        # print("AUIPC")
        imm_0 = last_line[-32 :-12]
        rd0 = last_line[-12 :-7]
        imm=imm_0+"000000000000"
        # print(imm)


        for i in register:
            if rd0 == register[i]:
                temp1=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp1:
                        rd=format(reg_value, '032b')
        rd0=twos_complement(PC) + twos_complement(imm) -4
        print(int_to_bin(rd0))
        reg_val[temp1]=rd0
        values_list = list(reg_val.values())
        t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
        # m = '\n'.join('0b{:032}'.format(value) for value in memory.values())
        outfile.write('0b'+PC)
        outfile.write(" ")
        outfile.write(t)
        outfile.write(" ")
        outfile.write('\n')  
     
        # outfile.write(m)
 
def J_type(last_line,PC, isb):
    if last_line[-7:]=="1101111": #jal
        print("JAL")
        rd0 = last_line[-12 :-7]
        imm1=last_line[-31:-21]
        # print(imm1,"imm1_Jtype")
        imm2=last_line[-21]
        imm3=last_line[-20:-12]
        # print(imm3, 'imm3')
        imm4=last_line[-32]
        print(imm1, "imm1")
        print(imm2, "imm2")
        print(imm3, "imm3")
        print(imm4, "imm4")
        # imm=imm4+imm3+imm2+imm1+'0'
        imm= imm3+imm2+ imm1+ "0"
        print(imm, 'imm_jtype')
        
        for i in register:
            if rd0 == register[i]:
                temp1=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp1:
                        rd=format(reg_value, '032b')

        # temp= PC
        rd= twos_complement(PC)
        # print(rd)
        reg_val[temp1]=rd
        # Pc=t1+imm
        # if imm!=0 then PC will change so isb==true
        reg_val["zero"] = 0
        print(twos_complement(imm), "DFREGREGHFDSFGJIEY")
        if twos_complement(imm)!=0: 
            isb[0] ="True"      
            PC= (twos_complement(PC)+  twos_complement(imm)-4) #(acc to project, pc=pc+4)
            PC= int_to_bin(PC)
            if PC[-1] != '0':
                PC= make_lsb_zero(PC)
        # PC=PC//4
        print(PC, 'pc')
        
        t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
        # m = '\n'.join('0b{:032}'.format(value) for value in memory.values())
        outfile.write('0b'+int_to_bin(twos_complement(PC)))
        outfile.write(" ")
        outfile.write(t)
        outfile.write(" ")
        outfile.write('\n')
        # print(PC, 'pc')
        return PC
        # outfile.write(m)
        # outfile.write('\n')
        


    
         
        
start_index=0
# k=0\
line = 0
print(len(lines))
while(line < len(lines)):
    isb = []
    isb.append("False") 
    # print("len of lines is ",len(lines), '4')
    # print(line, '2')
    # print("inside for")
    # print(line)
    l=line*4+4
    # print("l to check ",l)
    l = format(l,'032b')
    # k=k+1ṇ
    # print('loop', k)
    # print(line,l)
    if lines [line].strip() =="00000000000000000000000001100011":
        l = twos_complement(l)-4
        l = int_to_bin(l)
        outfile.write("0b"+l)
        outfile.write(" ")
        t = ' '.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in reg_val.values())
        outfile.write(t)
        outfile.write(" ")
        outfile.write('\n')
        break
    elif lines[line][-8:].strip() == "0110011":
        R_type(lines[line].strip(),l)
    elif lines[line][-8:].strip() == "1100111":
        # isb=False
        l=I_type_jalr(lines[line].strip(), l)
        line =twos_complement(l)//4-1
        # if isb == True:
        #     line = (line + (int(l)//4))-1 
        
        # print(line , "L")
        # print(l, 'a'   
    elif lines[line][-8:].strip() in ["0000011", "0010011"]:
        I_type(lines[line].strip(),l)
    elif lines[line][-8:].strip() == "0100011":
        S_type(lines[line].strip(),l) 
    elif lines[line][-8:].strip() == "1100011":
        l=B_type(lines[line].strip(),l,isb)
        # print(l,"l is")
        # print(line, 'l')
        # print(l)
        if isb[0] == "True":
            line = twos_complement(l)//4
            print("UPDATEDDDDDDDDDDDDDDDDDDDDDDDDD")
            print(line)
    
        # print(line, 'l')
    # elif lines[line][-8:].strip() == "0110111":
    #     U_type(lines[line].strip(),l) 
        
    elif lines[line][-8:].strip() in ["0110111", "0010111"]:
        U_type(lines[line].strip(),l) 
        
    elif lines[line][-8:].strip() == "1101111":
        # isb= [False]
        l=J_type(lines[line].strip(),l, isb) 
        print(l,"HERRREEEEEEEEEEEEE")
        print(isb , "ISBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
        if isb[0]=="True":
            print(line)
            print(twos_complement(l))
            line = (twos_complement(l)//4)
            print("UPDATEDDDEDDDDDDDDD")
            print(line)
    # print(line)
    if isb[0] == "False":
        line = line+1

# m = '\n'.join('0b{:032}'.format(value) for value in memory.values())
# m = '\n'.join('0b'+format(value,'032b') for value in memory.values())
# m = '\n'.join('0b'+format(value if value >= 0 else (1 << 32) + value,'032b') for value in memory.values())
# values_list = list(memory.values()) 
# print(values_list)
for keys in memory:
    m = "0b"+int_to_bin(memory[keys])
    outfile.write(keys)
    outfile.write(":")
    outfile.write(m)
    outfile.write('\n')  
outfile.close()