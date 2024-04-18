inst = {
    "name": [
        "lui", "auipc", "jal", "jalr", "beq", "bne", "blt", "bge", "bltu", "bgeu",
        "lw", "sw", "addi", "sltiu", "add", "sub", "sll", "slt", "sltu", "xor", "srl", "or", "and"
    ],
    "opcode": [
        "0110111", "0010111", "1101111", "1100111", "1100011", "1100011", "1100011", "1100011", "1100011", "1100011",
        "0000011", "0100011", "0010011", "0010011", "0110011", "0110011", "0110011", "0110011", "0110011", "0110011",
        "0110011", "0110011", "0110011"
    ],
    "funct3": [
        None, None, None, "000", "000", "001", "100", "101", "110", "111", "010", "010",
        "000", "011", "000", "000", "001", "010", "011", "100", "101", "110", "111"
    ],
    "funct7": [
        None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, "0000000", "0100000",
        "0000000", "0000000", "0000000", "0000000", "0000000", "0000000", "0000000"
    ]
}

register = {
    "x": [
        "x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7",
        "x8", "x9", "x10", "x11", "x12", "x13", "x14", "x15",
        "x16", "x17", "x18", "x19", "x20", "x21", "x22", "x23",
        "x24", "x25", "x26", "x27", "x28", "x29", "x30", "x31",
    ],
    "name": [
        "zero", "ra", "sp", "gp", "tp", "t0", "t1", "t2",
        "s0", "s1", "a0", "a1", "a2", "a3", "a4", "a5",
        "a6", "a7", "s2", "s3", "s4", "s5", "s6", "s7",
        "s8", "s9", "s10", "s11", "t3", "t4", "t5", "t6"
    ],
    "value": [
        "00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111",
        "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111",
        "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111",
        "11000", "11001", "11010", "11011", "11100", "11101", "11110", "11111"
    ]
}

f = open("inp.txt")
lines = f.readlines()
input_data = [line.strip() for line in lines]
f.close()

name = []
for i in range(len(input_data)):
    if ':' in input_data[i]:
        name.append([input_data[i].split(":")[0], 4 * i])
        input_data[i] = input_data[i].split(":")[1].strip()
        
input_data_1 = []
for i in range(len(input_data)):
    input_data_1.append(input_data[i].split(" ", 1))


op_code = []
func_3 = []
func_7 = []
for x in input_data_1:
    i = inst['name'].index(x[0])
    op_code.append(inst['opcode'][i])
    func_3.append(inst['funct3'][i])
    func_7.append(inst['funct7'][i])

input_data2 = []
for x in input_data_1:
    parts = x[1].replace(',', ' ').replace('(', ' ').replace(')', ' ').split()
    input_data2.append(parts)


for x in input_data2:
    if len(x) > 3:
        x.pop()

list_1 = []
for i in range(len(op_code)):
    if op_code[i] == "0110111" or op_code[i] == "0010111":
        rd = register['value'][register['name'].index(input_data2[i][0])]
        if int(input_data2[i][1]) >= 0:
            imm = '{:020b}'.format(int(input_data2[i][1]))
        else:
            imm = '{:020b}'.format(2**12 + int(input_data2[i][1]))
        list_1.append(int(imm + rd + op_code[i], base=2))

    elif op_code[i] == "1101111":
        rd = register['value'][register['name'].index(input_data2[i][0])]
        for x in name:
            if x[0] == input_data2[i][1]:
                if x[1] >= 4 * i:
                    imm = '{:020b}'.format(int((x[1] - 4 * i) / 2))
                else:
                    imm = '{:020b}'.format(2**12 + int((x[1] - 4 * i) / 2))
        list_1.append(int(imm[0] + imm[-10:] + imm[10] + imm[1:9] + rd + op_code[i], base=2))

    elif op_code[i] == "1100111":
        rd = register['value'][register['name'].index(input_data2[i][0])]
        rs1 = register['value'][register['name'].index(input_data2[i][1])]
        if int(input_data2[i][2]) >= 0:
            imm = '{:012b}'.format(int(input_data2[i][2]))
        else:
            imm = '{:012b}'.format(2**12 + int(input_data2[i][2]))
        list_1.append(int(imm + rs1 + func_3[i] + rd + op_code[i], base=2))

    
    elif op_code[i] == "1100011":
        rs1 = register['value'][register['name'].index(input_data2[i][0])]
        rs2 = register['value'][register['name'].index(input_data2[i][1])]
        for x in name:
            if x[0] == input_data2[i][2]:
                branch_offset = x[1] - (4 * i)
                if branch_offset >= 0:
                    imm = '{:012b}'.format(branch_offset // 2)
                else:
                    imm = '{:012b}'.format(2**12 + (branch_offset // 2))
                list_1.append(int(imm[0] + imm[2:8] + rs2 + rs1 + func_3[i] + imm[8:] + imm[1] + op_code[i], base=2))


    elif op_code[i] == "0000011":
        rd = register['value'][register['name'].index(input_data2[i][0])]
        if int(input_data2[i][1]) >= 0:
            imm = '{:012b}'.format(int(input_data2[i][1]))
        else:
            imm = '{:012b}'.format(2**12 + int(input_data2[i][1]))
        rs1 = register['value'][register['name'].index(input_data2[i][2])]
        list_1.append(int((imm + rs1 + func_3[i] + rd + op_code[i]), base=2))

    elif op_code[i] == "0110011":
        rd = register['value'][register['name'].index(input_data2[i][0])]
        rs1 = register['value'][register['name'].index(input_data2[i][1])]
        rs2 = register['value'][register['name'].index(input_data2[i][2])]
        list_1.append(int(func_7[i] + rs2 + rs1 + func_3[i] + rd + op_code[i], base=2))
        
    elif op_code[i] == "0100011":
        rs2 = register['value'][register['name'].index(input_data2[i][0])]
        if int(input_data2[i][1]) >= 0:
            imm = '{:012b}'.format(int(input_data2[i][1]))
        else:
            imm = '{:012b}'.format(2**12 + int(input_data2[i][1]))
        rs1 = register['value'][register['name'].index(input_data2[i][2])]
        list_1.append(int(imm[0:7] + rs2 + rs1 + func_3[i] + imm[7:] + op_code[i], base=2))

    elif op_code[i] == "0010011":
        rd = register['value'][register['name'].index(input_data2[i][0])]
        if int(input_data2[i][2]) >= 0:
            imm = '{:012b}'.format(int(input_data2[i][2]))
        else:
            imm = 2**12 + int(input_data2[i][2])
        rs1 = register['value'][register['name'].index(input_data2[i][1])]
        if func_7[i] is None:
            print(type(imm))
            print(type(func_3[i]))
            print(type(rd))
            print(type(op_code[i]))
           

            
            
        else:
            list_1.append(int((func_7[i] + imm[7:] + rs1 + func_3[i] + rd + op_code[i]), base=2))        



with open('Output.txt', 'w') as output_file:
    for instruction in list_1:
        output_file.write(format(instruction, '032b') + '\n')
